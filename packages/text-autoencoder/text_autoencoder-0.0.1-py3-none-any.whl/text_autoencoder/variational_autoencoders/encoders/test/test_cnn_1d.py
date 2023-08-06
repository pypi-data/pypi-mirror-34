import numpy as np
import tensorflow as tf

from ..cnn_1d import CNN1D


class CNN1DTestCase(tf.test.TestCase):

    def tearDown(self):
        tf.reset_default_graph()

    def test_input_with_tensor(self):
        with self.test_session() as sess:
            batch_size = 2
            output_size = 128
            input_value = tf.random_uniform(
                shape=[batch_size, 51],
                minval=0,
                maxval=1000,
                dtype=tf.int32,
            )
            embedding = tf.truncated_normal(
                shape=[2000, 300],
                mean=0.0,
                stddev=1.0,
            )
            filter_structures = [(3, 2, 128), (5, 3, 512)]
            output_mean, output_std = CNN1D(
                input_=input_value,
                input_dropout=0.3,
                filter_structures=filter_structures,
                output_size=output_size,
                embedding_table=embedding,

            )
            sess.run(tf.global_variables_initializer())
            self.assertAllEqual(
                (batch_size, output_size),
                output_mean.eval().shape,
            )
            self.assertAllEqual(
                (batch_size, output_size),
                output_std.eval().shape,
            )

    def test_input_with_placeholder(self):
        with self.test_session() as sess:
            output_size = 128
            input_value = tf.placeholder(
                shape=[None, 51],
                dtype=tf.int32,
            )
            embedding = tf.truncated_normal(
                shape=[2000, 300],
                mean=0.0,
                stddev=1.0,
            )
            filter_structures = [(5, 3, 128), (2, 1, 512)]
            output_mean, output_std = CNN1D(
                input_=input_value,
                input_dropout=0.3,
                filter_structures=filter_structures,
                output_size=output_size,
                embedding_table=embedding,

            )
            sess.run(tf.global_variables_initializer())
            output_mean, output_std = sess.run(
                [output_mean, output_std],
                feed_dict={
                    input_value:
                        np.random.randint(2000, size=(2, 51)).astype('int32'),
                },
            )
            self.assertAllEqual((2, output_size), output_mean.shape)
            self.assertAllEqual((2, output_size), output_std.shape)
