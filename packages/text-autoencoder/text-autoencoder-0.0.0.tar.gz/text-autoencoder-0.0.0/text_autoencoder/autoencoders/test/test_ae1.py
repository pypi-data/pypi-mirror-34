from os.path import abspath, join, dirname, isdir
from shutil import rmtree

import numpy as np
import tensorflow as tf

from ..ae_1 import AE1
from .test_train import TrainTestCase

ROOT_DIR = dirname(abspath(__file__))


class AE1TestCase(TrainTestCase, tf.test.TestCase):

    def setUp(self):
        self.data()
        self.params = {
            'embedding_table': self.embedding,
            'n_steps': self.n_steps,
            'latent_size': self.latent_size,
        }
        self.model_class = AE1
        self.model = AE1(**self.params)

    def data(self):
        self.root_dir = ROOT_DIR
        self.embedding = np.random.rand(50, 300)
        self.x_train = np.array(
            [
                [1, 4, 10, 3],
                [1, 7, 3, 0],
                [1, 20, 3, 0],
                [1, 20, 44, 3],
                [1, 11, 23, 3],
            ],
            dtype=np.int32,
        )
        self.seqlen_train = np.array([4, 3, 3, 4, 4], np.int32)
        self.x_test = np.array(
            [
                [1, 7, 12, 3],
                [1, 15, 3, 0],
            ],
            dtype=np.int32,
        )
        self.seqlen_test = np.array([4, 3], dtype=np.int32)
        self.n_steps = 4
        self.latent_size = 30
        self.model_path = join(ROOT_DIR, 'model_test/example')
        self.init_learning_rate = np.float32(0.01)

    def tearDown(self):
        tf.reset_default_graph()
        if isdir(dirname(self.model_path)):
            rmtree(dirname(self.model_path))

    def test_encode_on_batch(self):
        latent_vec = self.model._encode_on_batch(
            x_batch=self.x_train,
            seqlen_batch=self.seqlen_train,
        )
        self.assertEqual((5, self.latent_size), latent_vec.shape)

    def test_evaluate_on_batch(self):
        loss, info = self.model._evaluate_on_batch(
            x_batch=self.x_train,
            seqlen_batch=self.seqlen_train,
            decoder_assist=1,
        )
        self.assertIsInstance(loss, np.float32)
        self.assertEqual((), loss.shape)

    def test_train_on_batch_assist(self):
        loss, info = self.model._train_on_batch(
            x_batch=self.x_train,
            seqlen_batch=self.seqlen_train,
            learning_rate=1e-3,
            decoder_assist=1,
        )
        self.assertIsInstance(loss, np.float32)
        self.assertEqual((), loss.shape)

    def test_train_on_batch_without_assist(self):
        loss, info = self.model._train_on_batch(
            x_batch=self.x_train,
            seqlen_batch=self.seqlen_train,
            learning_rate=1e-3,
            decoder_assist=0,
        )
        self.assertIsInstance(loss, np.float32)
        self.assertEqual((), loss.shape)
