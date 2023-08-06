import numpy as np
import tensorflow as tf

from ..tcnn_1ds2 import tCNN1ds2


class tCNN1ds2TestCase(tf.test.TestCase):

    def tearDown(self):
        tf.reset_default_graph()

    def test_input_with_tensor(self):
        with self.test_session() as sess:
            batch_size = 100
            output_size = 128
            maxlen = 107
            input_value = tf.truncated_normal(
                shape=[batch_size, 512],
                mean=0.0,
                stddev=1.0,
            )
            filter_structures = [
                (3, 128), (3, 512), (5, 1024),
                (7, 128), (9, 52),
            ]
            output_logits, output_word_indices = tCNN1ds2(
                input_=input_value,
                input_dropout=0.7,
                maxlen=maxlen,
                filter_structures=filter_structures,
                output_size=output_size,
            )
            sess.run(tf.global_variables_initializer())
            self.assertAllEqual(
                (batch_size, maxlen, output_size),
                output_logits.eval().shape,
            )
            self.assertEqual(tf.float32, output_logits.dtype)
            self.assertAllEqual(
                (batch_size, maxlen),
                output_word_indices.eval().shape,
            )
            self.assertEqual(tf.int32, output_word_indices.dtype)

    def test_input_with_placeholder(self):
        with self.test_session() as sess:
            output_size = 128
            maxlen = 107
            input_value = tf.placeholder(
                shape=[None, 512],
                dtype=tf.float32,
            )
            filter_structures = [
                (3, 512),
                (5, 1024),
                (7, 128),
            ]
            output_logits, output_word_indices = tCNN1ds2(
                input_=input_value,
                input_dropout=0.7,
                maxlen=maxlen,
                filter_structures=filter_structures,
                output_size=output_size,
            )
            sess.run(tf.global_variables_initializer())
            output_logits, output_word_indices = sess.run(
                [output_logits, output_word_indices],
                feed_dict={
                    input_value:
                        np.random.rand(2, 512).astype('float32'),
                },
            )
            self.assertAllEqual((2, maxlen, output_size), output_logits.shape)
            self.assertAllEqual((2, maxlen), output_word_indices.shape)
            self.assertEqual(np.float32, output_logits.dtype)
            self.assertEqual(np.int32, output_word_indices.dtype)
