from typing import List, Tuple
import logging
from abc import abstractmethod
from os.path import dirname, abspath
import json
import sys

import tensorflow as tf
import numpy as np

ROOT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, ROOT_DIR)


from batching.batch_generator import BatchGenerator
from batching.batch_loader import BatchLoader
from learning.train_test_split import train_test_split
from .storage_manager import StorageManager


LOGGER = logging.getLogger(__name__)


class LearningManager(StorageManager):

    def __init__(
            self,
            logger: logging.Logger = LOGGER,
        ) -> None:

        self.logger = logger
        self.hyper_params_saved = False

        self.graph = tf.Graph()
        with self.graph.as_default():
            self.build_graph()

        #### INITIAL SESS AND SAVER ####
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True

        self.sess = tf.Session(graph=self.graph, config=config)
        self.sess.run(
            tf.variables_initializer(
                var_list=self.graph.get_collection("variables"),
            ),
        )
        self.saver = tf.train.Saver(
            var_list=self.graph.get_collection(
                tf.GraphKeys.TRAINABLE_VARIABLES,
            ),
            max_to_keep=999999999,
        )

    @abstractmethod
    def build_graph(self):
        raise NotImplementedError

    def fit(
            self,
            x: np.array,
            seqlen: np.array,
            output_path: str,
            valid_ratio: float = 0.1,
            batch_size: int = 32,
            init_learning_rate: float = 1e-4,
            epochs: int = 100,
            assist_max_epoch: int = 5,
            save_tf_serving: bool = False,
        ) -> None:

        if save_tf_serving:
            tf_serving_saver = self.set_tf_serving_saver(
                dirname(output_path))

        split_result = train_test_split(
            iterables=[x, seqlen],
            ratio=valid_ratio,
            seed=2018,
        )
        subtrain_x, subtrain_seqlen = split_result["train"]
        valid_x, valid_seqlen = split_result["test"]

        subtrain_batch_loader = BatchLoader(
            [subtrain_x, subtrain_seqlen],
            batch_size=batch_size,
            shuffle=True,
        )
        valid_batch_loader = BatchLoader(
            [valid_x, valid_seqlen],
            batch_size=batch_size,
            shuffle=False,
        )
        min_valid_loss = 1e+12

        for epoch in range(epochs):
            decoder_assist = int(epoch < assist_max_epoch)
            subtrain_loss_list = []

            for batch_x, batch_seqlen in subtrain_batch_loader():
                subtrain_loss, _ = self._train_on_batch(
                    x_batch=batch_x,
                    seqlen_batch=batch_seqlen,
                    decoder_assist=decoder_assist,
                    learning_rate=init_learning_rate,
                )
                subtrain_loss_list.append(subtrain_loss)

            valid_loss, _ = self.evaluate_loader(
                batch_loader=valid_batch_loader,
                decoder_assist=decoder_assist,
            )

            self.logger.info(
                'Epoch {} - train_loss: {}, valid_loss: {}, decoder_assist: {}'.format(
                    epoch,
                    np.mean(subtrain_loss_list),
                    valid_loss,
                    decoder_assist,
                ),
            )

            if valid_loss < min_valid_loss:
                min_valid_loss = valid_loss

                if save_tf_serving:
                    self.save_tf_serving(
                        tf_serving_saver=tf_serving_saver)
                else:
                    self.save(path=output_path)

    def fit_generator(
            self,
            subtrain_batch_generator: BatchGenerator,
            valid_batch_loader: BatchLoader,
            output_path: str,
            init_learning_rate: float = 1e-4,
            max_iter: int = 20000,
            assist_max_iter: int = 1000,
            display_period: int = 100,
            save_tf_serving: bool = False,
            **kwargs  # noqa
        ) -> None:

        if save_tf_serving:
            tf_serving_saver = self.set_tf_serving_saver(
                dirname(output_path))

        min_valid_loss = 1e+12
        for iter_n, (x, seqlen) in enumerate(
            subtrain_batch_generator(max_iter)):
            decoder_assist = int(iter_n < assist_max_iter)

            train_loss, train_info = self._train_on_batch(
                x_batch=x,
                seqlen_batch=seqlen,
                learning_rate=init_learning_rate,
                decoder_assist=1,
            )
            if iter_n % display_period == 0:
                valid_loss, valid_info = self.evaluate_loader(
                    batch_loader=valid_batch_loader,
                    decoder_assist=decoder_assist,
                )
                self.logger.info(
                    'Iteration {} - train_loss: {}, valid_loss: {}, decoder_assist: {}'.format(
                        iter_n, train_loss, valid_loss, decoder_assist),
                )
                self.logger.info(
                    'other train loss: {}'.format(
                        json.dumps(train_info['loss'].summary()),
                    ),
                )
                self.logger.info(
                    'other valid loss: {}'.format(
                        json.dumps(valid_info['loss']),
                    ),
                )
            if valid_loss < min_valid_loss:
                min_valid_loss = valid_loss

                if save_tf_serving:
                    self.save_tf_serving(tf_serving_saver=tf_serving_saver)
                else:
                    self.save(path=output_path)

    def evaluate(
            self,
            x: np.array,
            seqlen: np.array,
            batch_size: int = 32,
            decoder_assist: int = 0,
            shuffle: bool = False,
        ) -> Tuple[float, List[dict]]:

        batch_loader = BatchLoader(
            [x, seqlen],
            batch_size=batch_size,
            shuffle=shuffle,
        )
        return self.evaluate_loader(
            batch_loader=batch_loader,
            decoder_assist=decoder_assist,
        )

    def evaluate_loader(
            self,
            batch_loader,
            decoder_assist: int = 0,
        ) -> Tuple[float, List[dict]]:

        loss_list = []
        eval_output_info = None
        for i, (x_batch, seqlen_batch) in enumerate(batch_loader()):
            batch_loss, eval_info = self._evaluate_on_batch(
                x_batch=x_batch,
                seqlen_batch=seqlen_batch,
                decoder_assist=decoder_assist,
            )
            if i == 0:
                eval_output_info = eval_info
            else:
                for k, _ in eval_output_info.items():
                    eval_output_info[k].merge(eval_info[k])
            loss_list.append(batch_loss)

        if eval_output_info is not None:
            for k in eval_output_info:
                eval_output_info[k] = eval_output_info[k].summary()
            return np.mean(loss_list), eval_output_info
        return 65537.77, {}

    def encode(
            self,
            x: np.array,
            seqlen: np.array,
            batch_size: int = 32,
        ) -> np.array:

        batch_loader = BatchLoader(
            [x, seqlen],
            batch_size=batch_size,
            shuffle=False,
        )
        return self.encode_loader(batch_loader=batch_loader)

    def encode_loader(
            self,
            batch_loader,
        ) -> np.array:
        latent_vector = []
        for x_batch, seqlen_batch in batch_loader():
            batch_latent_vector = self._encode_on_batch(
                x_batch=x_batch,
                seqlen_batch=seqlen_batch,
            )
            latent_vector.append(batch_latent_vector)
        return np.vstack(latent_vector)
