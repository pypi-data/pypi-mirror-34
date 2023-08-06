import tensorflow as tf


def tf_linear(
        input_value: tf.Tensor,
        name: str,
        output_width: int,
        trainable: bool = True,
        initializer: tf.initializers = tf.truncated_normal_initializer(),
        dtype: tf.DType = tf.float32,
    ) -> tf.Tensor:

    weights = tf.get_variable(
        name="{}_weights".format(name),
        shape=[input_value.shape[-1], output_width],
        dtype=dtype,
        initializer=initializer,
        trainable=trainable,
    )
    bias = tf.get_variable(
        name="{}_bias".format(name),
        shape=[output_width],
        dtype=dtype,
        initializer=tf.zeros_initializer(),
        trainable=trainable,
    )
    output = input_value @ weights + bias
    output = tf.identity(output, name=name)
    return output
