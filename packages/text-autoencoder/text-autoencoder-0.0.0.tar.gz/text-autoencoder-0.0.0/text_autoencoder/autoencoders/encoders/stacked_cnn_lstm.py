from typing import List, Tuple

import tensorflow as tf

from layers.basic_lstm_cell_with_dropout import basic_lstm_cell_with_dropout


def StackedCNN_LSTM(
        input_: tf.Tensor,
        seqlen: tf.Tensor,
        embedding_table: tf.Tensor,  # np.ndarray
        input_dropout: float,
        state_size: int,
        filter_structures: List[Tuple[int]],
        is_training: bool = False,
        lstm_output_dropout: float = 0.1,
        dtype: tf.DType = tf.float32,
        seed: int = 2018,
    ) -> Tuple[tf.Tensor, tf.contrib.rnn.LSTMStateTuple]:
    '''
    filter_structures: filter_size, stride, output_channels
    '''
    batch_size = tf.shape(input_)[0]

    input_with_embedding = tf.nn.embedding_lookup(
        params=embedding_table,
        ids=input_,
    )
    input_with_dropout = tf.nn.dropout(
        x=input_with_embedding,
        keep_prob=(1.0 - input_dropout),
    )
    mid_value = input_with_dropout

    for i, (filter_size, stride, output_channels) in enumerate(
        filter_structures):
        input_channels = mid_value.shape[-1]
        filter_variable = tf.get_variable(
            name='cnn_filter_{}'.format(i),
            shape=[filter_size, input_channels, output_channels],
            dtype=dtype,
            initializer=tf.random_normal_initializer(
                stddev=0.1,
                seed=seed,
            ),
        )
        conv = tf.nn.conv1d(
            mid_value,
            filter_variable,
            stride=stride,
            padding='SAME',
            data_format='NWC',
            name='conv_{}'.format(i),
        )
        normed_conv = tf.contrib.layers.batch_norm(
            conv,
            decay=0.99,
            center=True,
            scale=True,
            is_training=is_training,
            scope='batch_norm_{}'.format(i),
        )
        mid_value = tf.nn.relu(
            features=normed_conv,
            name='activated_conv_{}'.format(i),
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
        inputs=tf.concat(
            values=[mid_value, input_with_dropout],
            axis=2,
        ),
        initial_state=init_state,
        sequence_length=seqlen,
        dtype=tf.float32,
    )
    output_latent_vector = tf.identity(
        output_state.h,
        name="latent_vector",
    )
    return output_latent_vector, output_state
