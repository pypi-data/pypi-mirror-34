import numpy as np
import tensorflow as tf

from ..dynamic_lstm import dynamicLSTM


class dynamicLSTMTestCase(tf.test.TestCase):

    def setUp(self):
        self.input_ = np.array(
            [
                [1, 4, 10, 3],
                [1, 7, 3, 0],
                [1, 20, 3, 0],
                [1, 20, 44, 3],
                [1, 11, 23, 3],
            ],
            dtype=np.int32,
        )
        self.seqlen = np.array([4, 3, 3, 4, 4], np.int32)
        self.embedding = np.random.rand(50, 300).astype('float32')

    def tearDown(self):
        tf.reset_default_graph()

    def test_build_encoder(self):
        with self.test_session() as sess:
            z_mean, z_std, state = dynamicLSTM(
                input_=tf.convert_to_tensor(self.input_),
                seqlen=tf.convert_to_tensor(self.seqlen),
                input_dropout=0.2,
                lstm_state_dropout=0.1,
                lstm_output_dropout=0.1,
                state_size=128,
                embedding_table=self.embedding,
            )
            sess.run(tf.global_variables_initializer())
            self.assertAllEqual((5, 128), z_mean.eval().shape)
            self.assertEqual(tf.float32, z_mean.dtype)
            self.assertAllEqual((5, 128), z_std.eval().shape)
            self.assertEqual(tf.float32, z_std.dtype)

            self.assertAllEqual((5, 128), state.h.eval().shape)
            self.assertEqual(tf.float32, state.h.dtype)
            self.assertAllEqual((5, 128), state.c.eval().shape)
            self.assertEqual(tf.float32, state.c.dtype)
