from typing import Tuple

import tensorflow as tf


def basic_lstm_cell_with_dropout(
        state_size: int,
        batch_size: int,
        output_dropout: float,
        state_dropout: float,
        input_dropout: float = 0.0,
        init_state: object = None,
        dtype: tf.DType = tf.float32,
    ) -> Tuple[object, tf.nn.rnn_cell.LSTMStateTuple]:

    lstm_cell = tf.contrib.rnn.BasicLSTMCell(
        num_units=state_size,
        forget_bias=1.0,
    )
    lstm_cell = tf.contrib.rnn.DropoutWrapper(
        cell=lstm_cell,
        input_keep_prob=(1.0 - input_dropout),
        output_keep_prob=(1.0 - output_dropout),
        state_keep_prob=(1.0 - state_dropout),
        dtype=dtype,
    )
    if init_state is None:
        init_state = lstm_cell.zero_state(
            batch_size=batch_size,
            dtype=dtype,
        )
    return lstm_cell, init_state
