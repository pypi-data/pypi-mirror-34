import tensorflow as tf

from .data import Data
from ..dynamic_bidir_lstm import DynamicBiDirLSTM


class DynamicBiDirLSTMTestCase(Data, tf.test.TestCase):

    def setUp(self):
        self.get_data()

    def tearDown(self):
        tf.reset_default_graph()

    def test_input_with_tensor(self):
        with self.test_session() as sess:

            latent, state = DynamicBiDirLSTM(
                input_=tf.convert_to_tensor(self.input_),
                seqlen=tf.convert_to_tensor(self.seqlen),
                input_dropout=0.1,
                state_size=128,
                embedding_table=self.embedding,
            )

            sess.run(tf.global_variables_initializer())
            self.assertAllEqual((5, 256), latent.eval().shape)
            self.assertEqual(tf.float32, latent.dtype)
            self.assertEqual('latent_vector:0', latent.name)

            self.assertAllEqual((5, 256), state.h.eval().shape)
            self.assertEqual(tf.float32, state.h.dtype)

            self.assertAllEqual((5, 256), state.c.eval().shape)
            self.assertEqual(tf.float32, state.c.dtype)

    def test_input_with_placeholder(self):
        with self.test_session() as sess:
            latent, state = DynamicBiDirLSTM(
                input_=tf.convert_to_tensor(self.input_),
                seqlen=tf.convert_to_tensor(self.seqlen),
                input_dropout=0.1,
                state_size=128,
                embedding_table=self.embedding,
            )
            sess.run(tf.global_variables_initializer())
            output_latent, output_state = sess.run(
                [latent, state],
                feed_dict={
                    self.input_place: self.input_,
                    self.seqlen_place: self.seqlen,
                },
            )
            self.assertAllEqual((5, 256), output_latent.shape)
            self.assertAllEqual((5, 256), output_state.h.shape)
            self.assertAllEqual((5, 256), output_state.c.shape)
