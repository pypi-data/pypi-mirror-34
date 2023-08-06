from typing import Tuple

import tensorflow as tf

from layers.basic_lstm_cell_with_dropout import basic_lstm_cell_with_dropout


def DynamicBiDirLSTM(
        input_: tf.Tensor,
        seqlen: tf.Tensor,
        input_dropout: float,
        state_size: int,
        embedding_table: tf.Tensor,  # np.ndarray,
        dtype: tf.DType = tf.float32,
    ) -> Tuple[tf.Tensor, tf.nn.rnn_cell.LSTMStateTuple]:

    batch_size = tf.shape(input_)[0]

    input_with_embedding = tf.nn.embedding_lookup(
        params=embedding_table,
        ids=input_,
    )

    input_with_dropout = tf.nn.dropout(
        x=input_with_embedding,
        keep_prob=(1.0 - input_dropout),
    )

    with tf.variable_scope('forward'):
        fw_lstm_cell, fw_init_state = basic_lstm_cell_with_dropout(
            state_size=state_size,
            batch_size=batch_size,
            state_dropout=0.0,
            output_dropout=0.0,
            dtype=dtype,
        )

    with tf.variable_scope('backward'):
        bw_lstm_cell, bw_init_state = basic_lstm_cell_with_dropout(
            state_size=state_size,
            batch_size=batch_size,
            state_dropout=0.0,
            output_dropout=0.0,
            dtype=dtype,
        )

    with tf.variable_scope('bidir_lstm'):
        _, output_state = tf.nn.bidirectional_dynamic_rnn(
            cell_fw=fw_lstm_cell,
            cell_bw=bw_lstm_cell,
            inputs=input_with_dropout,
            sequence_length=seqlen,
            initial_state_fw=fw_init_state,
            initial_state_bw=bw_init_state,
            dtype=dtype,
        )
    concated_h = tf.concat(
        values=[output_state[0].h, output_state[1].h],
        axis=1,
        name='concated_h',
    )
    concated_c = tf.concat(
        values=[output_state[0].c, output_state[1].c],
        axis=1,
        name='concated_c',
    )
    concated_output_state = tf.contrib.rnn.LSTMStateTuple(
        *(concated_h, concated_c),
    )
    latent = tf.identity(concated_h, name='latent_vector')
    return latent, concated_output_state
