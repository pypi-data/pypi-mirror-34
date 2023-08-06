from typing import List, Tuple, Dict
import logging
import shutil
import pickle as pkl
from abc import abstractmethod
from os.path import dirname, join
from tempfile import mkdtemp

import tensorflow as tf
import numpy as np
from bistiming import SimpleTimer
from mkdir_p import mkdir_p

from text_autoencoder.learning.callbacks import (
    get_improvement,
    ModelCheckpoint,
    EarlyStopping,
    ReduceLearningRate,
)
from text_autoencoder.batching.batch_loader import BatchLoader
from text_autoencoder.learning.train_test_split import train_test_split


LOGGER = logging.getLogger(__name__)


class VAELearningManager(object):

    def __init__(
            self,
            logger=LOGGER,
        ) -> None:
        #### ADDING PARAMs RELATED TO MODEL ####
        self.callback_is_set = False

        self.logger = logger
        self.seed_base = 2017

        ## counter
        self.subtrain_count = 0
        self.valid_count = 0

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
            max_to_keep=None,
        )

    def set_callback(
            self,
            improvement_epsilon: float = 1e-3,
            output_dir: str = None,
            save_interval: int = 1,
            save_best_only: bool = False,
            lr_decay_rate: float = 0.3,
            reduce_lr_patience: int = 3,
            reduce_lr_cooldown: int = 3,
            min_learning_rate: float = 1e-5,
            early_stop_patience: int = 10,
        ):
        self.callback_is_set = True
        self.min_loss = 1e+10
        self.improvement_epsilon = improvement_epsilon

        if output_dir:
            mkdir_p(output_dir)
            self.model_cp = ModelCheckpoint(
                sess=self.sess,
                saver=self.saver,
                output_dir=output_dir,
                period=save_interval,
                save_best_only=save_best_only,
            )
        else:
            self.model_cp = None
        self.early_stop = EarlyStopping(
            patience=early_stop_patience,
        )
        self.reduce_lr = ReduceLearningRate(
            reduce_rate=lr_decay_rate,
            patience=reduce_lr_patience,
            cooldown=reduce_lr_cooldown,
            min_learning_rate=min_learning_rate,
        )

    def run_callback(
            self,
            monitor_loss: float,
            epoch: int,
            learning_rate: float,
        ):
        if not self.callback_is_set:
            return False, learning_rate

        self.min_loss, improvement = get_improvement(
            current_loss=monitor_loss,
            min_loss=self.min_loss,
            epsilon=self.improvement_epsilon,
        )
        stop_or_not = self.early_stop(improvement)
        if stop_or_not:
            return True, None
        else:
            if self.model_cp:
                self.model_cp(
                    epoch=epoch,
                    model_name=self.gen_model_name(epoch),
                    improvement=improvement,
                )
            learning_rate, _ = self.reduce_lr(
                improvement=improvement,
                learning_rate=learning_rate,
            )
            return False, learning_rate

    @abstractmethod
    def build_graph(self):
        raise NotImplementedError

    def fit(
            self,
            subtrain_x: np.ndarray,
            subtrain_seqlen: np.ndarray,
            init_learning_rate: float = 0.001,
            batch_size: int = 32,
            epochs: int = 100,
            valid_ratio: float = 0.0,
            valid_x: np.ndarray = None,
            valid_seqlen: np.ndarray = None,
            improvement_epsilon: float = 1e-3,
            output_dir: str = mkdtemp(),
            summary_output_dir: str = None,
            save_interval: int = 1,
            save_best_only: bool = False,
            lr_decay_rate: float = 0.3,
            reduce_lr_patience: int = 3,
            reduce_lr_cooldown: int = 3,
            min_learning_rate: float = 1e-5,
            early_stop_patience: int = 10,
            index2word: Dict[int, str] = None,
            seed: int = 2017,
            verbose: int = 1,
        ) -> None:
        if (valid_ratio > 0.0) and (valid_x is None):
            split_result = train_test_split(
                iterables=[subtrain_x, subtrain_seqlen],
                ratio=valid_ratio,
                seed=seed,
            )
            subtrain_x, subtrain_seqlen = split_result["train"]
            valid_x, valid_seqlen = split_result["test"]

        subtrain_batch_loader = BatchLoader(
            [subtrain_x, subtrain_seqlen],
            batch_size=batch_size,
        )
        subtrain_x = subtrain_seqlen = None  # free subtrain_X and Y

        if (valid_x is not None) and (valid_seqlen is not None):
            valid_batch_loader = BatchLoader(
                [valid_x, valid_seqlen],
                batch_size=batch_size,
            )
            valid_x = valid_seqlen = None
        else:
            valid_batch_loader = None

        self.fit_generator(
            subtrain_batch_loader=subtrain_batch_loader,
            valid_batch_loader=valid_batch_loader,
            init_learning_rate=init_learning_rate,
            epochs=epochs,
            improvement_epsilon=improvement_epsilon,
            output_dir=output_dir,
            save_interval=save_interval,
            save_best_only=save_best_only,
            lr_decay_rate=lr_decay_rate,
            reduce_lr_patience=reduce_lr_patience,
            reduce_lr_cooldown=reduce_lr_cooldown,
            min_learning_rate=min_learning_rate,
            early_stop_patience=early_stop_patience,
            index2word=index2word,
            verbose=verbose,
        )

    def fit_generator(
            self,
            subtrain_batch_loader: object,
            init_learning_rate: float = 0.001,
            epochs: int = 100,
            valid_batch_loader: object = None,
            improvement_epsilon: float = 1e-3,
            output_dir: str = mkdtemp(),
            save_interval: int = 1,
            save_best_only: bool = False,
            lr_decay_rate: float = 0.3,
            reduce_lr_patience: int = 3,
            reduce_lr_cooldown: int = 3,
            min_learning_rate: float = 1e-5,
            early_stop_patience: int = 10,
            index2word: Dict[int, str] = None,
            verbose: int = 1,
        ) -> None:

        self.output_dir = output_dir

        subtrain_summary_writer = tf.summary.FileWriter(
            logdir=join(self.output_dir, "summary/subtrain/"),
            graph=self.sess.graph,
        )
        valid_summary_writer = tf.summary.FileWriter(
            logdir=join(self.output_dir, "summary/valid/"),
            graph=self.sess.graph,
        )

        self.set_callback(
            improvement_epsilon=improvement_epsilon,
            output_dir=join(self.output_dir, "model/"),
            save_interval=save_interval,
            save_best_only=save_best_only,
            lr_decay_rate=lr_decay_rate,
            reduce_lr_patience=reduce_lr_patience,
            reduce_lr_cooldown=reduce_lr_cooldown,
            min_learning_rate=min_learning_rate,
            early_stop_patience=early_stop_patience,
        )
        learning_rate = init_learning_rate

        if valid_batch_loader is not None:
            valid = True
            monitor_loss = "mean_valid_loss"
        else:
            valid = False
            monitor_loss = "mean_subtrain_loss"

        for epoch in range(epochs):
            with SimpleTimer(
                "Fitting at epoch {}".format(epoch),
                verbose_start=True if verbose > 0 else False,
                verbose_end=True if verbose > 0 else False,
            ):
                subtrain_loss, data_size = self._train_on_single_epoch(
                    subtrain_batch_loader=subtrain_batch_loader,
                    subtrain_summary_writer=subtrain_summary_writer,
                    learning_rate=learning_rate,
                    epoch=epoch,
                    valid=valid,
                    valid_batch_loader=valid_batch_loader,
                    valid_summary_writer=valid_summary_writer,
                    index2word=index2word,
                    decoder_assist=1 if epoch < 100 else 0,
                    verbose=verbose,
                )

            mean_subtrain_loss = subtrain_loss / data_size
            mean_valid_loss = self.validate_generator(
                data_generator=valid_batch_loader,
                is_valid=valid,
            )
            if verbose > 0:
                print(
                    "...(learning_rate = {:.5g}) : ".format(learning_rate),
                    "training loss = {:.5g}, validation loss = {:.5g} ".format(
                        mean_subtrain_loss, mean_valid_loss,
                    ),
                    "\n ------------------------------------------",
                )
            stop_or_not, learning_rate = self.run_callback(
                monitor_loss=locals()[monitor_loss],
                epoch=epoch,
                learning_rate=learning_rate,
            )
            if stop_or_not:
                print("Early Stopping!")
                break

        if save_best_only and (self.output_dir is not None):
            self.saver.restore(
                sess=self.sess,
                save_path=join(
                    self.output_dir,
                    "model/{}-0".format(self.model_name),
                ),
            )
            shutil.rmtree(join(self.output_dir, "model/"))

    def _train_on_single_epoch(
            self,
            subtrain_batch_loader: object,
            subtrain_summary_writer: tf.summary.FileWriter,
            learning_rate: int,
            epoch: int,
            valid: bool = False,
            valid_batch_loader: object = None,
            valid_summary_writer: tf.summary.FileWriter = None,
            index2word: Dict[int, str] = None,
            decoder_assist: int = 0,
            verbose: int = 1,
        ):
        batch_loss_sum = 0
        data_size = 0
        for num, (x_batch, seqlen_batch) in enumerate(subtrain_batch_loader(), 1):
            with SimpleTimer(
                "...Fitting at epoch {} batch {}".format(epoch, num),
                verbose_start=True if verbose > 1 else False,
                verbose_end=True if verbose > 1 else False,
            ):
                if index2word is not None:
                    self.show_decoder_output(
                        word_indices=x_batch,
                        index2word=index2word,
                        iter_n=num,
                        mode='real',
                    )

                self.subtrain_count += 1
                mean_subtrain_loss, other_info = \
                    self._train_on_batch(
                        x_batch=x_batch,
                        seqlen_batch=seqlen_batch,
                        learning_rate=np.float32(learning_rate),
                        step=self.subtrain_count,
                        decoder_assist=decoder_assist,
                        summary_writer=subtrain_summary_writer,
                    )
                batch_loss_sum += mean_subtrain_loss * x_batch.shape[0]
                data_size += x_batch.shape[0]

                if index2word is not None:
                    self.show_decoder_output(
                        word_indices=other_info['decoder_output_indices'],
                        index2word=index2word,
                        iter_n=num,
                        mode='decode',
                    )

            if verbose > 1:
                mean_valid_loss = self.validate_generator(
                    data_generator=valid_batch_loader,
                    summary_writer=valid_summary_writer,
                    is_valid=valid,
                )
                print(
                    "...(epoch {:d} batch {:d}) : ".format(epoch, num),
                    "training loss = {:.5g}, validation loss = {:.5g} ".format(
                        mean_subtrain_loss, mean_valid_loss,
                    ),
                )
        return batch_loss_sum, data_size

    @staticmethod
    def show_decoder_output(
            word_indices: np.ndarray,
            index2word: Dict[int, str],
            iter_n: int,
            period: int = 100,
            mode: str = 'read',
        ) -> None:
        if iter_n % period == 0:
            output_seqs = [""] * len(word_indices)
            for row_i in range(len(word_indices)):
                seq = word_indices[row_i, :]
                for char in seq:
                    output_seqs[row_i] += index2word[char]
            print('==={}============================='.format(mode))
            print("\n".join(output_seqs))
            print("\n")

    def validate_generator(
            self,
            data_generator: object = None,
            summary_writer: tf.summary.FileWriter = None,
            is_valid: bool = False,
        ):
        if is_valid and (data_generator is not None):
            return self.evaluate_generator(
                data_generator=data_generator,
                summary_writer=summary_writer,
                mode="validate",
            )
        else:
            return -65536.9999

    def get_latent_vector(
            self,
            x: np.ndarray,
            seqlen: np.ndarray,
            batch_size: int = 1,
        ) -> List[Tuple[np.ndarray, float]]:
        batch_loader = BatchLoader(
            [x, seqlen],
            batch_size=batch_size,
            shuffle=False,
        )
        output = []
        for x_batch, seqlen_batch in batch_loader():
            batch_result = self._get_latent_vector_on_batch(
                x_batch=x_batch,
                seqlen_batch=seqlen_batch,
            )
            output.extend(batch_result)
        return output

    def encode(
            self,
            x: np.ndarray,
            seqlen: np.ndarray,
            batch_size: int = 1,
        ):
        batch_loader = BatchLoader(
            [x, seqlen],
            batch_size=batch_size,
            shuffle=False,
        )
        output = []
        for x_batch, seqlen_batch in batch_loader():
            batch_result = self._encode_on_batch(
                x_batch=x_batch,
                seqlen_batch=seqlen_batch,
            )
            output.extend(batch_result)
        return output

    def save(
            self,
            path: str,
            hyper_params: dict,
            verbose: int = 1,
        ) -> None:
        """
        hyper_params = {
            "input_dim": 300,
            "output_dim": 10,
        }
        """
        mkdir_p(dirname(path))
        with SimpleTimer(
            "Saving model to {}".format(path),
            verbose_start=True if verbose > 0 else False,
            verbose_end=True if verbose > 0 else False,
        ):
            hyper_param_path, variable_path = self.gen_path(path)
            with open(hyper_param_path, "wb") as fw:
                pkl.dump(hyper_params, fw)
            self.saver.save(self.sess, variable_path)

            # moving summary dir to new output dir
            shutil.move(
                join(self.output_dir, "summary/"),
                dirname(path),
            )
        # remove self.output_dir
        shutil.rmtree(self.output_dir)

    @classmethod
    def load(
            cls,
            path: str,
            verbose: int = 1,
        ) -> object:
        """Load trained parameters.
        Use this method when load model to the cache.
        >>> clf = XXX.load("path/to/model")
        >>> y = clf.predict(x)
        """
        with SimpleTimer(
            "Loading model from {}".format(path),
            verbose_start=True if verbose > 0 else False,
            verbose_end=True if verbose > 0 else False,
        ):
            hyper_param_path, variable_path = cls.gen_path(path)
            with open(hyper_param_path, "rb") as f:
                params = pkl.load(f)
            model = cls(**params)
            model.saver.restore(model.sess, variable_path)
        return model

    def evaluate(
            self,
            x: np.ndarray,
            seqlen: np.ndarray,
            batch_size: int = 32,
            mode: str = "evaluate",
        ) -> float:
        batch_loader = BatchLoader(
            [x, seqlen],
            batch_size=batch_size,
        )
        return self.evaluate_generator(
            data_generator=batch_loader,
            mode=mode,
        )

    def evaluate_generator(
            self,
            data_generator: object,
            summary_writer: tf.summary.FileWriter = None,
            mode: str = "evaluate",
        ) -> float:
        loss = []
        data_size = 0
        for x_batch, seqlen_batch in data_generator():
            if mode == "validate":
                self.valid_count += 1
            loss.append(
                self._evaluate_on_batch(
                    x_batch=x_batch,
                    seqlen_batch=seqlen_batch,
                    step=self.valid_count,
                    summary_writer=summary_writer,
                    mode=mode,
                )[0],
            )
            data_size += x_batch.shape[0]
        mean_loss = np.sum(loss) / data_size
        return mean_loss

    @abstractmethod
    def gen_model_name(self, epoch):
        raise NotImplementedError

    @staticmethod
    def gen_path(path):
        hyper_param_path = path + "-param.pkl"
        variable_path = path + "-variable.model"
        return hyper_param_path, variable_path

    def __del__(self):
        """GC, session recycle, etc."""
        self.sess.close()
        del self.sess
        del self.graph
        del self.saver
        del self.__dict__
