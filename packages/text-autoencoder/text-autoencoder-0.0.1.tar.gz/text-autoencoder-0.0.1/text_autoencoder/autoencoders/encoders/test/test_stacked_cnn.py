import tensorflow as tf

from .data import Data
from ..stacked_cnn import StackedCNN


class StackedCNNTestCase(Data, tf.test.TestCase):

    def setUp(self):
        self.get_data()

    def tearDown(self):
        tf.reset_default_graph()

    def test_input_with_tensor(self):
        with self.test_session() as sess:
            latent = StackedCNN(
                input_=tf.convert_to_tensor(self.input_),
                embedding_table=self.embedding,
                input_dropout=0.1,
                output_size=128,
                filter_structures=[
                    (3, 1, 128),
                    (5, 2, 256),
                ],
                is_training=False,
            )
            sess.run(tf.global_variables_initializer())
            self.assertAllEqual((5, 128), latent.eval().shape)
            self.assertEqual(tf.float32, latent.dtype)
            self.assertEqual('latent_vector:0', latent.name)

    def test_input_with_placeholder(self):
        with self.test_session() as sess:
            latent = StackedCNN(
                input_=self.input_place,
                embedding_table=self.embedding,
                input_dropout=0.1,
                output_size=128,
                filter_structures=[
                    (3, 1, 128),
                    (5, 2, 256),
                ],
                is_training=False,
            )
            sess.run(tf.global_variables_initializer())
            output_latent = sess.run(
                latent,
                feed_dict={
                    self.input_place: self.input_,
                },
            )
            self.assertAllEqual((5, 128), output_latent.shape)
