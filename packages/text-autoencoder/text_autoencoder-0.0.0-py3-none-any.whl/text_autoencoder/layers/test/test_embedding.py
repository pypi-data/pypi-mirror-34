import numpy as np
import tensorflow as tf

from ..embedding import get_embedding


class EmbeddingTestCase(tf.test.TestCase):

    def test_get_embedding(self):
        with self.test_session() as sess:
            embed_1 = get_embedding(
                embedding_array=np.random.rand(10, 300),
            )
            sess.run(tf.global_variables_initializer())
            self.assertAllEqual((10, 300), embed_1.eval().shape)
            self.assertEqual('embedding:0', embed_1.name)

        with self.test_session() as sess:
            embed_2 = get_embedding(
                vocab_size=100,
                embedding_size=30,
                name='123',
            )
            sess.run(tf.global_variables_initializer())
            self.assertAllEqual((100, 30), embed_2.eval().shape)
            self.assertEqual('123:0', embed_2.name)
