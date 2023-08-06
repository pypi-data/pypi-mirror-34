from os.path import abspath, join, dirname, isdir
from shutil import rmtree

import numpy as np
import tensorflow as tf

from ..lstm2lstm import VAELstm2Lstm
from .test_train import TrainTestCase

ROOT_DIR = dirname(abspath(__file__))


class VAELstm2LstmTestCase(TrainTestCase, tf.test.TestCase):

    def setUp(self):
        self.model_name = 'VAELstm2Lstm'
        self.data()
        self.tf_summary_output_dir = join(
            self.root_dir,
            "tf_model_test_{}/".format(self.model_name),
        )
        self.params = {
            'embedding_table': self.embedding,
            'n_steps': self.n_steps,
            'model_name': self.model_name,
        }
        self.model_class = VAELstm2Lstm
        self.model = VAELstm2Lstm(**self.params)

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
        self.model_path = join(ROOT_DIR, 'model_test/' + self.model_name)
        self.init_learning_rate = np.float32(0.01)

    def tearDown(self):
        tf.reset_default_graph()
        if 'output_dir' in self.model.__dict__:
            if isdir(self.model.output_dir):
                rmtree(self.model.output_dir)
        if isdir(dirname(self.model_path)):
            rmtree(dirname(self.model_path))
