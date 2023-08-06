from typing import Tuple

import tensorflow as tf

from layers.linear import tf_linear


def basic_lstm_cell_with_dropout(
        state_size: int,
        batch_size: int,
        output_dropout: float,
        state_dropout: float,
        input_dropout: float = 0.0,
        init_state: object = None,
        dtype: tf.DType = tf.float32,
    ):
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


def DynamicBidirLSTM(
        input_: tf.Tensor,
        seqlen: tf.Tensor,
        input_dropout: float,
        lstm_state_dropout: float,
        lstm_output_dropout: float,
        state_size: int,
        latent_size: int,
        embedding_table: tf.Tensor,  # np.ndarray,
        dtype: tf.DType = tf.float32,
    ) -> Tuple[tf.Tensor, tf.Tensor]:

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
            state_dropout=lstm_state_dropout,
            output_dropout=lstm_output_dropout,
            dtype=dtype,
        )

    with tf.variable_scope('backward'):
        bw_lstm_cell, bw_init_state = basic_lstm_cell_with_dropout(
            state_size=state_size,
            batch_size=batch_size,
            state_dropout=lstm_state_dropout,
            output_dropout=lstm_output_dropout,
            dtype=dtype,
        )

    with tf.variable_scope('bidir_lstm'):
        _, hidden_states = tf.nn.bidirectional_dynamic_rnn(
            cell_fw=fw_lstm_cell,
            cell_bw=bw_lstm_cell,
            inputs=input_with_dropout,
            sequence_length=seqlen,
            initial_state_fw=fw_init_state,
            initial_state_bw=bw_init_state,
            dtype=dtype,
        )
    concated_final_state = tf.concat(
        values=[hidden_states[0].h, hidden_states[1].h],
        axis=1,
        name='hidden_output_concat',
    )
    output_mean = tf.nn.selu(
        features=tf_linear(
            input_value=concated_final_state,
            name="mean_state",
            output_width=latent_size,
            initializer=tf.keras.initializers.lecun_uniform(seed=2017),
        ),
        name="mean_vector",
    )
    output_std = tf.nn.selu(
        features=tf_linear(
            input_value=concated_final_state,
            name="std_state",
            output_width=latent_size,
            initializer=tf.keras.initializers.lecun_uniform(seed=2018),
        ),
        name="std_vector",
    )
    return output_mean, output_std
