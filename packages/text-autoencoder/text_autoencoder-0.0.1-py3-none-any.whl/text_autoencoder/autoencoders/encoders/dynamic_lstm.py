from typing import Tuple

import tensorflow as tf

from layers.basic_lstm_cell_with_dropout import basic_lstm_cell_with_dropout


def DynamicLSTM(
        input_: tf.Tensor,
        seqlen: tf.Tensor,
        embedding_table: tf.Tensor,  # np.ndarray,
        input_dropout: float = 0.1,
        lstm_output_dropout: float = 0.2,
        state_size: int = 256,
        seed: int = 2017,
        dtype: tf.DType = tf.float32,
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
    _, output_state = tf.nn.dynamic_rnn(
        cell=lstm_cell,
        inputs=input_with_dropout,
        initial_state=init_state,
        sequence_length=seqlen,
        dtype=dtype,
    )
    output_latent_vector = tf.identity(
        output_state.h,
        name="latent_vector",
    )
    return output_latent_vector, output_state
