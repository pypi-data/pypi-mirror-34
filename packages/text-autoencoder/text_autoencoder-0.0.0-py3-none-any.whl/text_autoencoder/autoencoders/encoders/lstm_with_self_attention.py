from typing import Tuple

import tensorflow as tf

from layers.structured_self_attention import (
    tf_structured_self_attention,
    tf_structured_self_attention_penalty,
)
from layers.linear import tf_linear
from layers.basic_lstm_cell_with_dropout import basic_lstm_cell_with_dropout


def LSTMWithSelfAttention(
        input_: tf.Tensor,
        seqlen: tf.Tensor,
        embedding_table: tf.Tensor,  # np.ndarray,
        input_dropout: float = 0.1,
        lstm_output_dropout: float = 0.2,
        state_size: int = 256,
        attention_hops: int = 5,
        attention_hidden_size: int = 1024,
        dtype: tf.DType = tf.float32,
        seed: int = 2017,
    ) -> Tuple[tf.Tensor, tf.nn.rnn_cell.LSTMStateTuple]:

    batch_size = tf.shape(input_)[0]

    ### index to embedded
    input_with_embedding = tf.nn.embedding_lookup(
        params=embedding_table,
        ids=input_,
    )
    ### embedding_dropout
    input_with_dropout = tf.nn.dropout(
        x=input_with_embedding,
        keep_prob=(1.0 - input_dropout),
    )

    ### lstm cell
    lstm_cell, init_state = basic_lstm_cell_with_dropout(
        state_size=state_size,
        batch_size=batch_size,
        state_dropout=0.0,
        output_dropout=lstm_output_dropout,
        dtype=dtype,
    )

    output_word, output_state = tf.nn.dynamic_rnn(
        cell=lstm_cell,
        inputs=input_with_dropout,
        initial_state=init_state,
        sequence_length=seqlen,
        dtype=dtype,
    )

    ### self attention ###
    attentive_input, annotation_matrix = tf_structured_self_attention(
        input_=output_word,
        hidden_size=attention_hidden_size,
        hops=attention_hops,
        dtype=dtype,
    )
    tf_structured_self_attention_penalty(
        annotation_matrix=annotation_matrix,
    )
    output_latent_vector = tf_linear(
        input_value=tf.reshape(
            attentive_input,
            shape=[-1, state_size * attention_hops],
        ),
        output_width=state_size,
        dtype=dtype,
        name='attention_to_linear',
    )
    output_latent_vector = tf.nn.tanh(
        output_latent_vector, name='latent_vector')

    return output_latent_vector, output_state
