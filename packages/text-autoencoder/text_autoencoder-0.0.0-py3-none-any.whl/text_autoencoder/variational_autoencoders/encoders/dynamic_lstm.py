from typing import Tuple

import tensorflow as tf

from layers.linear import tf_linear


def dynamicLSTM(
        input_: tf.Tensor,
        seqlen: tf.Tensor,
        input_dropout: float,
        lstm_state_dropout: float,
        lstm_output_dropout: float,
        state_size: int,
        embedding_table: tf.Tensor,  # np.ndarray,
        dtype: tf.DType = tf.float32,
    ) -> Tuple[tf.Tensor, tf.Tensor]:

    batch_size = tf.shape(input_)[0]

    # lstm cell
    lstm_cell = tf.contrib.rnn.BasicLSTMCell(
        num_units=state_size,
        forget_bias=1.0,
    )
    lstm_cell = tf.contrib.rnn.DropoutWrapper(
        cell=lstm_cell,
        input_keep_prob=1.0,
        output_keep_prob=(1.0 - lstm_output_dropout),
        state_keep_prob=(1.0 - lstm_state_dropout),
        dtype=dtype,
    )
    init_state = lstm_cell.zero_state(
        batch_size=batch_size,
        dtype=dtype,
    )

    input_with_embedding = tf.nn.embedding_lookup(
        params=embedding_table,
        ids=input_,
    )

    ### embedding_dropout
    input_with_dropout = tf.nn.dropout(
        x=input_with_embedding,
        keep_prob=(1.0 - input_dropout),
    )
    _, final_state = tf.nn.dynamic_rnn(
        cell=lstm_cell,
        inputs=input_with_dropout,
        initial_state=init_state,
        sequence_length=seqlen,
        dtype=dtype,
    )
    output_mean = tf.nn.selu(
        features=tf_linear(
            input_value=final_state.h,
            name="mean_state",
            output_width=state_size,
            initializer=tf.keras.initializers.lecun_uniform(seed=2017),
        ),
        name="mean_vector",
    )
    output_std = tf.nn.selu(
        features=tf_linear(
            input_value=final_state.h,
            name="std_state",
            output_width=state_size,
            initializer=tf.keras.initializers.lecun_uniform(seed=2018),
        ),
        name="std_vector",
    )
    return output_mean, output_std, final_state
