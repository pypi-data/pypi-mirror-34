import tensorflow as tf

from ..linear import tf_linear


class LinearTestCase(tf.test.TestCase):

    def test_tf_linear(self):
        with self.test_session() as sess:
            result = tf_linear(
                input_value=tf.random_normal((100, 1024)),
                name='test',
                output_width=13,
                initializer=tf.truncated_normal_initializer(stddev=0.1),
                trainable=False,
            )
            sess.run(tf.global_variables_initializer())
            self.assertAllEqual((100, 13), result.eval().shape)
            self.assertEqual('test:0', result.name)
            self.assertEqual(tf.float32, result.dtype)
