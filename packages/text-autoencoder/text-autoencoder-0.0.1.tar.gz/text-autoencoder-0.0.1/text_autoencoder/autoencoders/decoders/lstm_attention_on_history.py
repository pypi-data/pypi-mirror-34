from typing import Tuple
import numpy as np
import tensorflow as tf

from layers.schedule_sampling import schedule_sampling
from layers.structured_self_attention import (
    tf_structured_self_attention,
    # tf_structured_self_attention_penalty,
)
from layers.basic_lstm_cell_with_dropout import basic_lstm_cell_with_dropout
from layers.linear import tf_linear


def history_attention(
        history_word_indices: tf.Tensor,  # batch_size * seq_len
        attention_hidden_size: int,
        attention_hops: int,
        output_size: int,
        embedding_table: tf.Tensor,
        # step: int,
        dtype: tf.DType = tf.float32,
    ) -> tf.Tensor:

    history_embedded_words = tf.nn.embedding_lookup(
        params=embedding_table,
        ids=history_word_indices,
    )
    ### self attention ###
    attentive_input, annotation_matrix = tf_structured_self_attention(
        input_=history_embedded_words,
        hidden_size=attention_hidden_size,
        hops=attention_hops,
        dtype=dtype,
    )
    # tf_structured_self_attention_penalty(
    #     annotation_matrix=annotation_matrix,
    #     name='self_attention_penalty_{}'.format(),
    # )
    history_vector = tf_linear(
        input_value=tf.reshape(
            attentive_input,
            shape=[-1, attentive_input.shape[2] * attention_hops],
        ),
        output_width=output_size,
        dtype=dtype,
        name='attention_to_linear',
    )
    history_vector = tf.nn.tanh(
        history_vector, name='history_vector')
    return history_vector


def LSTM_LatentVec_InitState_AttentiveHistory(
        latent_input: tf.Tensor,  # batch_size * latent_size
        real_indices: tf.Tensor,  # batch_size * maxlen
        embedding_table: np.ndarray,
        history_size: int,
        attention_hidden_size: int,
        attention_hops: int = 5,
        init_state: tf.contrib.rnn.LSTMStateTuple = None,
        state_size: int = None,
        assist: int = 0,
        dtype: tf.DType = tf.float32,
    ) -> Tuple[tf.Tensor, tf.Tensor]:

    batch_size = tf.shape(latent_input)[0]

    if init_state is not None:
        state_size = init_state.h.shape[1].value
    else:
        if state_size is None:
            raise ValueError('zero init state needs state_size !!!')

    vocab_size, embedding_size = embedding_table.shape
    maxlen = real_indices.shape[1]

    weights = tf.get_variable(
        name='weights',
        shape=[state_size, vocab_size],
        initializer=tf.truncated_normal_initializer(),
    )
    bias = tf.get_variable(
        name='bias',
        shape=[vocab_size],
        initializer=tf.zeros_initializer(),
    )

    lstm_cell, init_state = basic_lstm_cell_with_dropout(
        state_size=state_size,
        batch_size=batch_size,
        state_dropout=0.0,
        output_dropout=0.0,
        init_state=init_state,
        dtype=dtype,
    )
    init_input_vectors = tf.nn.embedding_lookup(
        params=embedding_table,
        ids=real_indices[:, 0],
    )
    logits_collection = tf.one_hot(
        indices=tf.reshape(
            real_indices[:, 0],
            shape=[1, batch_size],
        ),
        depth=vocab_size,
    )

    count = tf.constant(1)
    stopping_criteria = lambda count, \
        input_vectors,\
        init_state,\
        word_indices_collection: count < maxlen

    def _predict_next_word(
            count,
            input_vectors,
            previous_state,
            logits_collection,
        ):
        attentive_history = history_attention(
            history_word_indices=tf.argmax(
                tf.transpose(
                    logits_collection,
                    perm=[1, 0, 2],
                ),
                axis=2,
                output_type=tf.int32,
            ),
            attention_hidden_size=attention_hidden_size,
            attention_hops=attention_hops,
            output_size=history_size,
            embedding_table=embedding_table,
            # step=count,
            dtype=dtype,
        )
        next_step, next_state = lstm_cell(
            inputs=tf.concat(
                [latent_input, input_vectors, attentive_history],
                axis=1,
            ),
            state=previous_state,
        )
        logits = tf.nn.elu(
            features=next_step @ weights + bias,
        )
        output = tf.nn.softmax(logits)

        predicted_next_word_indices = tf.cast(
            tf.argmax(output, axis=1),
            dtype=tf.int32,
        )
        next_word_indices = schedule_sampling(
            real_word=real_indices[:, count],
            predicted_word=predicted_next_word_indices,
            assist=assist,
        )
        next_embedded_words = tf.nn.embedding_lookup(
            params=embedding_table,
            ids=next_word_indices,
        )
        output_logits = tf.reshape(
            logits,
            shape=[1, tf.shape(logits)[0], tf.shape(logits)[1]],
        )
        return count + 1, \
            next_embedded_words, \
            next_state, \
            tf.concat([logits_collection, output_logits], axis=0)

    _, _, _, output_logits = tf.while_loop(
        cond=stopping_criteria,
        body=_predict_next_word,
        loop_vars=[
            count,
            init_input_vectors,
            init_state,
            logits_collection,
        ],
        shape_invariants=[
            count.get_shape(),
            tf.TensorShape([None, embedding_size]),
            tf.contrib.rnn.LSTMStateTuple(
                *(
                    tf.TensorShape([None, state_size]),
                    tf.TensorShape([None, state_size]),
                ),
            ),
            tf.TensorShape(
                [
                    None,
                    logits_collection.get_shape()[1],
                    vocab_size,
                ],
            ),
        ],
    )
    output_logits = tf.transpose(
        output_logits,
        perm=[1, 0, 2],
        name='logits',
    )
    output_word_indices = tf.argmax(
        output_logits,
        axis=2,
        name='word_indices',
        output_type=tf.int32,
    )
    return output_logits, output_word_indices
