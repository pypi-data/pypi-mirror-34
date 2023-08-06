from typing import Tuple, Dict
import logging
import copy
from collections import OrderedDict as OD

import numpy as np
import tensorflow as tf
from serving_utils import Client, PredictInput

from .base_autoencoder import BaseAutoencoder
from .encoders import DynamicLSTM
from .decoders import LSTM_LatentVec_InitState
from losses import (  # noqa
    l2_regularization,
    mean_reconstruction_loss,
)
from .managers.learning_manager import LearningManager
from layers.embedding import get_embedding
from toolkit.result_collection_structure import (
    LossCollection,
    ArrayCollection,
)
from autoencoders import TENSOR_NAMES

LOGGER = logging.getLogger(__name__)


class AE1(LearningManager, BaseAutoencoder):

    def __init__(
            self,
            embedding_table: np.ndarray,  # np.float32
            n_steps: int = 10,
            latent_size: int = 50,
            input_dropout_ratio: float = 0.2,
            l2_reg_scale: float = 1e-4,
            logger: logging.Logger = LOGGER,
        ) -> None:

        self.embedding_table = embedding_table.astype(np.float32)
        self.n_steps = n_steps

        self.input_dropout_ratio = input_dropout_ratio
        self.latent_size = latent_size
        self.l2_reg_scale = l2_reg_scale

        self.hyper_params = copy.deepcopy(self.__dict__)

        self.vocab_size, self.embedding_size = embedding_table.shape

        super(AE1, self).__init__(
            logger=logger,
        )
        self._get_tensors()

    def build_graph(self):
        input_X = tf.placeholder(
            name=TENSOR_NAMES["X_PLACE"],
            dtype=tf.int32,
            shape=[None, self.n_steps],
        )
        seqlen = tf.placeholder(
            name=TENSOR_NAMES["SEQLEN_PLACE"],
            dtype=tf.int32,
            shape=[None],
        )
        is_training_place = tf.placeholder_with_default(
            False,
            shape=(),
            name=TENSOR_NAMES["IS_TRAINING_PLACE"],
        )
        assist_place = tf.placeholder_with_default(
            0,
            shape=(),
            name=TENSOR_NAMES["DECODER_ASSIST_PLACE"],
        )
        lr_place = tf.placeholder(
            dtype=tf.float32,
            name=TENSOR_NAMES["LR_PLACE"],
        )
        embedding_tensor = get_embedding(
            embedding_array=self.embedding_table,
            trainable=TENSOR_NAMES["IS_TRAINING_PLACE"],
        )
        is_training = tf.cast(is_training_place, tf.float32)
        with tf.variable_scope("encoder"):
            latent, _ = DynamicLSTM(
                input_=input_X,
                seqlen=seqlen,
                input_dropout=(self.input_dropout_ratio * is_training),
                state_size=self.latent_size,
                embedding_table=embedding_tensor,
            )
        with tf.variable_scope("decoder"):
            output_logits, output_word_indices = LSTM_LatentVec_InitState(
                latent_input=latent,  # batch_size * state_size
                real_indices=input_X,  # batch_size * maxlen
                embedding_table=embedding_tensor,
                state_size=self.latent_size,
                assist=assist_place,
            )

        mean_reconstruction_loss(
            pred_logits=output_logits,
            true_indices=input_X,
            num_indices=self.vocab_size,
            seqlen=seqlen,
            name="{}_reconstruction".format(TENSOR_NAMES["OP_LOSS"]),
        )

        l2_regularization(scale=self.l2_reg_scale)

        loss_for_train = tf.add_n(
            tf.get_collection('losses'),
            name="{}_total".format(TENSOR_NAMES["OP_LOSS"]),
        )
        tvars = tf.trainable_variables()

        optimizer = tf.train.AdamOptimizer(lr_place)

        gradvar = optimizer.compute_gradients(
            loss=loss_for_train,
            var_list=tvars,
        )
        clipped_grad = [
            (tf.clip_by_value(grad, -1., 1.), var) for grad, var in gradvar]
        train_op = optimizer.apply_gradients(  # noqa
            clipped_grad,
            name=TENSOR_NAMES["OP_TRAIN"],
        )

    def _get_tensors(self):

        self.x_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["X_PLACE"] + ":0",
        )
        self.seqlen_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["SEQLEN_PLACE"] + ":0",
        )
        self.is_training_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["IS_TRAINING_PLACE"] + ":0",
        )
        self.assist_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["DECODER_ASSIST_PLACE"] + ":0",
        )
        self.lr_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["LR_PLACE"] + ":0",
        )

        self.latent_tensor = self.graph.get_tensor_by_name(
            name="encoder/latent_vector:0",
        )
        self.decoded_output_indices_tensor = self.graph.get_tensor_by_name(
            name="decoder/word_indices:0",
        )
        self.total_loss_tensor = self.graph.get_tensor_by_name(
            name="{}_total:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        self.recon_loss_tensor = self.graph.get_tensor_by_name(
            name="{}_reconstruction:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        self.train_op = self.graph.get_operation_by_name(
            name=TENSOR_NAMES["OP_TRAIN"],
        )

    def _encode_on_batch(
            self,
            x_batch: np.ndarray,
            seqlen_batch: np.ndarray,
        ) -> np.ndarray:

        batch_latent_vectors = self.sess.run(
            fetches=self.latent_tensor,
            feed_dict={
                self.x_place: x_batch,
                self.seqlen_place: seqlen_batch,
                self.is_training_place: False,
            },
        )
        return batch_latent_vectors

    def _train_on_batch(
            self,
            x_batch: np.ndarray,
            seqlen_batch: np.ndarray,
            learning_rate: np.float32,
            decoder_assist: int = 0,
        ) -> Tuple[float, Dict[str, np.ndarray]]:

        decoder_output_indices, \
            batch_recon_loss, \
            total_loss, \
            _ = self.sess.run(
                fetches=[
                    self.decoded_output_indices_tensor,
                    self.recon_loss_tensor,
                    self.total_loss_tensor,
                    self.train_op,
                ],
                feed_dict={
                    self.x_place: x_batch,
                    self.seqlen_place: seqlen_batch,
                    self.lr_place: learning_rate,
                    self.is_training_place: True,
                    self.assist_place: decoder_assist,
                },
            )

        return total_loss, {
            "loss": LossCollection(
                OD({"reconstruction_loss": batch_recon_loss}),
            ),
            "decoder_output": ArrayCollection(
                OD({"decoded_word_indices": decoder_output_indices}),
            ),
        }

    def _evaluate_on_batch(
            self,
            x_batch: np.ndarray,
            seqlen_batch: np.ndarray,
            decoder_assist: int = 0,
        ) -> Tuple[float, Dict[str, np.ndarray]]:

        decoder_output_indices,\
            batch_recon_loss, \
            total_loss = self.sess.run(
                fetches=[
                    self.decoded_output_indices_tensor,
                    self.recon_loss_tensor,
                    self.total_loss_tensor,
                ],
                feed_dict={
                    self.x_place: x_batch,
                    self.seqlen_place: seqlen_batch,
                    self.is_training_place: False,
                    self.assist_place: decoder_assist,
                },
            )

        return total_loss, {
            "loss": LossCollection(
                OD({"reconstruction_loss": batch_recon_loss}),
            ),
            "decoder_output": ArrayCollection(
                OD({"decoded_word_indices": decoder_output_indices}),
            ),
        }

    def save(self, path: str):
        super().save(
            path=path,
            hyper_params=self.hyper_params,
        )

    def define_signature(self):
        signature_def_map = {
            'encode':
                tf.saved_model.signature_def_utils.predict_signature_def(
                    inputs={
                        'x': self.x_place,
                        'seqlen': self.seqlen_place,
                    },
                    outputs={
                        'vector': self.latent_tensor,
                    },
                ),
        }
        return signature_def_map

    @staticmethod
    def encode_tf_serving(
            tf_serving_client: Client,
            x: np.array,
            seqlen: np.array,
            dir_name: str,
        ) -> np.array:

        serving_output_dict = tf_serving_client.predict(
            model_signature_name='encode',
            data=[
                PredictInput(name='x', value=x),
                PredictInput(name='seqlen', value=seqlen),
            ],
            model_name=dir_name,
            output_names=['vector'],
        )
        return serving_output_dict['vector']
