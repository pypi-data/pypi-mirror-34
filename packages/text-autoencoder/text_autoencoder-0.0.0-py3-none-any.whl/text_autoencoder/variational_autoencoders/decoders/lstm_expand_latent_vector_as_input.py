import numpy as np
import tensorflow as tf

from layers.linear import tf_linear
from layers.schedule_sampling import schedule_sampling


def expand_latent(
        latent_vectors: tf.Tensor,
        maxlen: int,
        initializer: tf.initializers = tf.truncated_normal_initializer(),
    ) -> tf.Tensor:
    batch_size = tf.shape(latent_vectors)[0]
    latent_size = latent_vectors.shape[1]

    latent_seq = tf_linear(
        input_value=latent_vectors,
        name='latent_sequence',
        output_width=maxlen * latent_size,
        initializer=initializer,
        trainable=True,
        dtype=tf.float32,
    )
    latent_seq = tf.nn.leaky_relu(
        features=latent_seq,
        alpha=0.2,
        name='nonlinear_latent_sequence',
    )
    latent_mtx = tf.reshape(
        latent_seq,
        shape=[batch_size, maxlen, latent_size],
    )
    return latent_mtx


def LSTM_ExpandLatentVectorAsInput(
        latent_vectors: tf.Tensor,
        real_indices: tf.Tensor,  # batch_size * maxlen
        lstm_input_dropout: float,
        lstm_output_dropout: float,
        lstm_state_dropout: float,
        state_size: int,
        embedding_table: np.ndarray,
        assist: int = 0,
    ) -> tf.Tensor:

    batch_size = tf.shape(latent_vectors)[0]
    vocab_size, embedding_size = embedding_table.shape
    maxlen = real_indices.shape[1]

    latent_mtx = expand_latent(
        latent_vectors=latent_vectors,
        maxlen=maxlen,
    )

    weights = tf.get_variable(
        name='weights',
        shape=[state_size, vocab_size],
        initializer=tf.keras.initializers.lecun_uniform(seed=2017),
    )
    bias = tf.get_variable(
        name='bias',
        shape=[vocab_size],
        initializer=tf.zeros_initializer(),
    )
    lstm_cell = tf.contrib.rnn.BasicLSTMCell(
        num_units=state_size,
        forget_bias=1.0,
    )
    lstm_cell = tf.contrib.rnn.DropoutWrapper(
        cell=lstm_cell,
        input_keep_prob=1.0,
        output_keep_prob=(1.0 - lstm_output_dropout),
        state_keep_prob=(1.0 - lstm_state_dropout),
        dtype=tf.float32,
    )
    init_state = lstm_cell.zero_state(
        batch_size=batch_size,
        dtype=tf.float32,
    )

    input_vectors = tf.nn.embedding_lookup(
        params=embedding_table,
        ids=real_indices[:, 0],
    )
    input_vectors = tf.reshape(
        input_vectors,
        shape=[batch_size, 1, embedding_size],
    )
    logits_collection = tf.one_hot(
        indices=tf.reshape(
            real_indices[:, 0],
            shape=[1, batch_size],
        ),
        depth=vocab_size,
    )

    count = tf.constant(0)
    stopping_criteria = lambda count, \
        input_vectors,\
        init_state,\
        word_indices_collection: count < maxlen - 1

    def _predict_next_word(
            count,
            input_vectors,
            previous_state,
            logits_collection,
        ):
        _, next_state = tf.nn.dynamic_rnn(
            cell=lstm_cell,
            inputs=tf.concat(
                [latent_mtx[:, count: count + 1, :], input_vectors],
                axis=2,
            ),
            initial_state=previous_state,
            dtype=tf.float32,
            sequence_length=tf.ones([batch_size], dtype=tf.int32),
        )
        logits = next_state.h @ weights + bias
        output = tf.nn.softmax(logits)

        predicted_next_word_indices = tf.cast(
            tf.argmax(output, axis=1),
            dtype=tf.int32,
        )
        next_word_indices = schedule_sampling(
            real_word=real_indices[:, count + 1],
            predicted_word=predicted_next_word_indices,
            assist=assist,
        )
        next_embedded_words = tf.nn.embedding_lookup(
            params=embedding_table,
            ids=next_word_indices,
        )
        em_shape = tf.shape(next_embedded_words)
        next_embedded_words = tf.reshape(
            next_embedded_words,
            shape=[em_shape[0], 1, embedding_size],
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
            input_vectors,
            init_state,
            logits_collection,
        ],
        shape_invariants=[
            count.get_shape(),
            tf.TensorShape([None, 1, embedding_size]),
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
