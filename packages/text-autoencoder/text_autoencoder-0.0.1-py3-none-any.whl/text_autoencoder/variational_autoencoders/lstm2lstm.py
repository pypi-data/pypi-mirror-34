from typing import Tuple, List, Dict

import numpy as np
import tensorflow as tf

from .base_model import BaseVariationalAutoencoder
from .learning_manager import VAELearningManager
from text_autoencoder.variational_autoencoders import TENSOR_NAMES
from .encoders import dynamicLSTM
from .decoders import LSTM_LatentVectorAsInitState
from text_autoencoder.layers.embedding import get_embedding


class VAELstm2Lstm(VAELearningManager, BaseVariationalAutoencoder):

    def __init__(
            self,
            embedding_table: np.ndarray,  # np.float32
            n_steps: int = 10,
            encoder_state_size: int = 50,
            latent_size: int = 30,
            input_dropout_ratio: float = 0.2,
            encoder_lstm_output_dropout_ratio: float = 0.1,
            encoder_lstm_state_dropout_ratio: float = 0.0,
            decoder_lstm_input_dropout_ratio: float = 0.0,
            decoder_lstm_output_dropout_ratio: float = 0.2,
            decoder_lstm_state_dropout_ratio: float = 0.0,
            l2_regularization: float = 1e-4,
            kl_lambda: object = None,
            max_grad_norm: float = 5.0,
            model_name: str = "VAELstm2Lstm",
            initialize_graph: bool = True,
        ) -> None:
        self.embedding_table = embedding_table.astype(np.float32)
        self.vocab_size, self.embedding_size = embedding_table.shape
        self.n_steps = n_steps
        self.batch_size = 50

        self.input_dropout_ratio = input_dropout_ratio
        self.encoder_lstm_output_dropout_ratio = encoder_lstm_output_dropout_ratio
        self.encoder_lstm_state_dropout_ratio = encoder_lstm_state_dropout_ratio
        self.decoder_lstm_input_dropout_ratio = decoder_lstm_input_dropout_ratio
        self.decoder_lstm_output_dropout_ratio = decoder_lstm_output_dropout_ratio
        self.decoder_lstm_state_dropout_ratio = decoder_lstm_state_dropout_ratio

        self.latent_size = latent_size
        self.decoder_state_size = latent_size
        self.decoder_output_size = self.vocab_size

        self.model_name = model_name
        self.l2_regularization = l2_regularization
        self.max_grad_norm = max_grad_norm

        if kl_lambda is None:
            self.kl_lambda = self._kl_lambda
        else:
            self.kl_lambda = kl_lambda

        self.initialize_graph = initialize_graph
        if self.initialize_graph:
            super(VAELstm2Lstm, self).__init__(
            )

    def build_graph(self):
        x_place = tf.placeholder(
            dtype=tf.int32,
            shape=[None, self.n_steps],
            name=TENSOR_NAMES["X_PLACE"],
        )
        seqlen_place = tf.placeholder(
            dtype=tf.int32,
            shape=[None],
            name=TENSOR_NAMES["MASK_PLACE"],
        )
        decoder_assist_place = tf.placeholder_with_default(
            0,
            shape=(),
            name=TENSOR_NAMES["DECODER_ASSIST_PLACE"],
        )
        learning_rate_place = tf.placeholder(
            dtype=tf.float32,
            name=TENSOR_NAMES["LR_PLACE"],
        )
        input_dropout_place = tf.placeholder_with_default(
            0.0,
            shape=(),
            name="input_{}".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        encoder_lstm_output_dropout_place = tf.placeholder_with_default(
            0.0,
            shape=(),
            name="encoder_lstm_output_{}".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        encoder_lstm_state_dropout_place = tf.placeholder_with_default(
            0.0,
            shape=(),
            name="encoder_lstm_state_{}".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        decoder_lstm_input_dropout_place = tf.placeholder_with_default(
            0.0,
            shape=(),
            name="decoder_lstm_input_{}".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        decoder_lstm_output_dropout_place = tf.placeholder_with_default(
            0.0,
            shape=(),
            name="decoder_lstm_output_{}".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        decoder_lstm_state_dropout_place = tf.placeholder_with_default(
            0.0,
            shape=(),
            name="decoder_lstm_state_{}".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        self.batch_size = tf.shape(x_place)[0]

        self.embedding_tensor = get_embedding(
            embedding_array=self.embedding_table,
        )

        with tf.variable_scope("encoder"):
            z_mean, z_std, _ = dynamicLSTM(
                input_=x_place,
                seqlen=seqlen_place,
                input_dropout=input_dropout_place,
                lstm_state_dropout=encoder_lstm_state_dropout_place,
                lstm_output_dropout=encoder_lstm_output_dropout_place,
                state_size=self.latent_size,
                embedding_table=self.embedding_tensor,
            )
        z = self.sample_from_gaussion(mean=z_mean, std=z_std)
        z = tf.identity(z, name=TENSOR_NAMES["OP_LATENT_VEC"])

        with tf.variable_scope("decoder"):
            output_logits, _ = LSTM_LatentVectorAsInitState(
                latent_vectors=z,
                real_indices=x_place,
                lstm_input_dropout=decoder_lstm_input_dropout_place,
                lstm_output_dropout=decoder_lstm_output_dropout_place,
                lstm_state_dropout=decoder_lstm_state_dropout_place,
                embedding_table=self.embedding_tensor,
                assist=decoder_assist_place,
            )

        step = tf.train.get_or_create_global_step(graph=self.graph)

        mean_vae_loss, mean_recon_loss, mean_kl_div = self.compute_loss(
            x=x_place,
            z_mean=z_mean,
            z_std=z_std,
            decoder_output_logits=output_logits,
            step=step,
        )

        ##### train #####
        tvars = tf.trainable_variables()
        l2_regularizer = tf.contrib.layers.l2_regularizer(
            scale=self.l2_regularization,
        )
        regularization_term = tf.contrib.layers.apply_regularization(
            regularizer=l2_regularizer,
            weights_list=tvars,
        )

        loss_for_train = mean_vae_loss + regularization_term
        loss_for_train = tf.identity(
            loss_for_train,
            name="{}_total".format(TENSOR_NAMES["OP_LOSS"]),
        )

        grads, _ = tf.clip_by_global_norm(
            t_list=tf.gradients(loss_for_train, tvars),
            clip_norm=self.max_grad_norm,
        )
        self.summary(
            tensor_dict={
                "mean_KL_divergent": mean_kl_div,
                "mean_reconstruction_loss": mean_recon_loss,
                "mean_vae_loss": mean_vae_loss,
                "regularize_loss": regularization_term,
                "mean_vae_loss_with_regularization": loss_for_train,
            },
        )

        optimizer = tf.train.RMSPropOptimizer(learning_rate_place)
        train_op = optimizer.apply_gradients(  # noqa
            zip(grads, tvars),
            global_step=step,
            name=TENSOR_NAMES["OP_TRAIN"],
        )

    @staticmethod
    def sample_from_gaussion(
            mean: tf.Tensor,
            std: tf.Tensor,
        ) -> tf.Tensor:

        eps = tf.random_normal(shape=tf.shape(mean))
        return mean + tf.exp(std / 2) * eps

    @staticmethod
    def _kl_lambda(
            step: tf.Tensor,
            max_value: float = 0.1,
            n_iterations: int = 200,
        ) -> tf.Tensor:
        """
         0 < max_value < 1
         step: tf.float32
        """
        return max_value / (1 + tf.exp(n_iterations - tf.cast(step, tf.float32)))

    def compute_loss(
            self,
            x: tf.Tensor,
            z_mean: tf.Tensor,
            z_std: tf.Tensor,
            decoder_output_logits: tf.Tensor,
            step: tf.Tensor,
        ) -> Tuple[tf.Tensor, tf.Tensor, tf.Tensor]:
        with tf.variable_scope("loss"):
            # reconstruction loss: E[log P(X|z)]
            recon_loss = tf.reduce_mean(
                input_tensor=tf.nn.softmax_cross_entropy_with_logits_v2(
                    logits=decoder_output_logits,
                    labels=tf.one_hot(x, depth=self.vocab_size),
                    dim=2,
                ),
                axis=1,
                name="{}_reconstruction".format(TENSOR_NAMES["OP_LOSS"]),
            )
            # D_KL(Q(z|X) || P(z));
            kl_divergent_loss = 0.5 * tf.reduce_sum(
                tf.exp(z_std) + z_mean**2 - 1. - z_std,
                axis=1,
                name="{}_kl_div".format(TENSOR_NAMES["OP_LOSS"]),
            )
            # VAE loss
            vae_loss = recon_loss + self.kl_lambda(step=step) * kl_divergent_loss
            vae_loss = tf.identity(
                vae_loss,
                name="{}_vae".format(TENSOR_NAMES["OP_LOSS"]),
            )
        return tf.reduce_mean(vae_loss), \
            tf.reduce_mean(recon_loss), \
            tf.reduce_mean(kl_divergent_loss)

    @staticmethod
    def summary(tensor_dict: Dict[str, tf.Tensor]):
        for name, tensor in tensor_dict.items():
            tf.summary.scalar(name=name, tensor=tensor)
        tf.summary.merge_all()

    def _encode_on_batch(
            self,
            x_batch: np.ndarray,
            seqlen_batch: np.ndarray,
        ) -> List[Tuple[np.ndarray, np.ndarray]]:

        x_place = self.graph.get_tensor_by_name(
            TENSOR_NAMES["X_PLACE"] + ":0",
        )
        seqlen_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["MASK_PLACE"] + ":0",
        )

        mean_vector_tensor = self.graph.get_tensor_by_name(
            name="encoder/mean_vector:0",
        )  # z_mean
        std_vector_tensor = self.graph.get_tensor_by_name(
            name="encoder/std_vector:0",
        )  # z_std

        batch_mean_vectors, batch_std_vectors = self.sess.run(
            fetches=[
                mean_vector_tensor,
                std_vector_tensor,
            ],
            feed_dict={
                x_place: x_batch,
                seqlen_place: seqlen_batch,
            },
        )
        output = []
        for mean_vec, std_vec in zip(batch_mean_vectors, batch_std_vectors):
            output.append((mean_vec, std_vec))
        return output

    def _train_on_batch(
            self,
            x_batch: np.ndarray,
            seqlen_batch: np.ndarray,
            learning_rate: np.float32,
            decoder_assist: int = 0,
            step: np.int32 = 0,
            summary_writer: tf.summary.FileWriter = None,
        ) -> Tuple[float, Dict[str, np.ndarray]]:

        x_place = self.graph.get_tensor_by_name(
            TENSOR_NAMES["X_PLACE"] + ":0",
        )
        seqlen_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["MASK_PLACE"] + ":0",
        )
        decoder_assist_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["DECODER_ASSIST_PLACE"] + ":0",
        )
        input_dropout_place = self.graph.get_tensor_by_name(
            name="input_{}:0".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        encoder_lstm_output_dropout_place = self.graph.get_tensor_by_name(
            name="encoder_lstm_output_{}:0".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        encoder_lstm_state_dropout_place = self.graph.get_tensor_by_name(
            name="encoder_lstm_state_{}:0".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        decoder_lstm_output_dropout_place = self.graph.get_tensor_by_name(
            name="decoder_lstm_output_{}:0".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        decoder_lstm_state_dropout_place = self.graph.get_tensor_by_name(
            name="decoder_lstm_state_{}:0".format(
                TENSOR_NAMES["DROPOUT_PLACE"],
            ),
        )
        lr_place = self.graph.get_tensor_by_name(
            name="{}:0".format(TENSOR_NAMES["LR_PLACE"]),
        )

        decoder_output_indices_tensor = self.graph.get_tensor_by_name(
            name="decoder/word_indices:0",
        )
        vae_loss_tensor = self.graph.get_tensor_by_name(
            name="loss/{}_vae:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        recon_loss_tensor = self.graph.get_tensor_by_name(
            name="loss/{}_reconstruction:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        kl_divergent_tensor = self.graph.get_tensor_by_name(
            name="loss/{}_kl_div:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        total_loss_tensor = self.graph.get_tensor_by_name(
            name="{}_total:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        merged_summary_tensor = self.graph.get_tensor_by_name(
            name="Merge/MergeSummary:0",
        )
        train_op = self.graph.get_operation_by_name(
            name=TENSOR_NAMES["OP_TRAIN"],
        )

        decoder_output_indices, \
            batch_recon_loss, \
            batch_kl_div, \
            batch_vae_loss, \
            total_loss, \
            train_summary, _ = self.sess.run(
                fetches=[
                    decoder_output_indices_tensor,
                    recon_loss_tensor,
                    kl_divergent_tensor,
                    vae_loss_tensor,
                    total_loss_tensor,
                    merged_summary_tensor,
                    train_op,
                ],
                feed_dict={
                    x_place: x_batch,
                    seqlen_place: seqlen_batch,
                    input_dropout_place: self.input_dropout_ratio,
                    encoder_lstm_output_dropout_place:
                        self.encoder_lstm_output_dropout_ratio,
                    encoder_lstm_state_dropout_place:
                        self.encoder_lstm_state_dropout_ratio,
                    decoder_assist_place: decoder_assist,
                    decoder_lstm_output_dropout_place:
                        self.decoder_lstm_output_dropout_ratio,
                    decoder_lstm_state_dropout_place:
                        self.decoder_lstm_state_dropout_ratio,
                    lr_place: learning_rate,
                },
            )
        if summary_writer is not None:
            summary_writer.add_summary(
                summary=train_summary,
                global_step=step,
            )
        return total_loss, {
            "decoder_output_indices": decoder_output_indices,
            "reconstruction_loss": batch_recon_loss,
            "kl_divergent": batch_kl_div,
            "vae_loss": batch_vae_loss,
            "total_loss": total_loss,  # mean_vae + regularization
        }

    def _evaluate_on_batch(
            self,
            x_batch: np.ndarray,
            seqlen_batch: np.ndarray,
            step: np.int32 = 0,
            summary_writer: tf.summary.FileWriter = None,
            mode: str = "evaluate",
        ) -> Tuple[float, Dict[str, np.ndarray]]:

        x_place = self.graph.get_tensor_by_name(
            TENSOR_NAMES["X_PLACE"] + ":0",
        )
        seqlen_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["MASK_PLACE"] + ":0",
        )

        decoder_output_indices_tensor = self.graph.get_tensor_by_name(
            name="decoder/word_indices:0",
        )
        vae_loss_tensor = self.graph.get_tensor_by_name(
            name="loss/{}_vae:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        recon_loss_tensor = self.graph.get_tensor_by_name(
            name="loss/{}_reconstruction:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        kl_divergent_tensor = self.graph.get_tensor_by_name(
            name="loss/{}_kl_div:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        total_loss_tensor = self.graph.get_tensor_by_name(
            name="{}_total:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        merged_summary_tensor = self.graph.get_tensor_by_name(
            name="Merge/MergeSummary:0",
        )

        decoder_output_indices,\
            batch_recon_loss, \
            batch_kl_div, \
            batch_vae_loss, \
            total_loss, \
            evaluate_summary = self.sess.run(
                fetches=[
                    decoder_output_indices_tensor,
                    recon_loss_tensor,
                    kl_divergent_tensor,
                    vae_loss_tensor,
                    total_loss_tensor,
                    merged_summary_tensor,
                ],
                feed_dict={
                    x_place: x_batch,
                    seqlen_place: seqlen_batch,
                },
            )
        if (mode == "validate") and (summary_writer is not None):
            summary_writer.add_summary(
                summary=evaluate_summary,
                global_step=step,
            )
        return total_loss, {
            "decoder_output_indices": decoder_output_indices,
            "reconstruction_loss": batch_recon_loss,
            "kl_divergent": batch_kl_div,
            "vae_loss": batch_vae_loss,
            "total_loss": total_loss,  # mean_vae + regularization
        }

    def _get_latent_vector_on_batch(
            self,
            x_batch: np.ndarray,
            seqlen_batch: np.ndarray,
        ) -> List[Tuple[np.ndarray, np.float32]]:

        x_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["X_PLACE"] + ":0",
        )
        seqlen_place = self.graph.get_tensor_by_name(
            name=TENSOR_NAMES["MASK_PLACE"] + ":0",
        )
        latent_tensor = self.graph.get_tensor_by_name(
            name="{}:0".format(TENSOR_NAMES["OP_LATENT_VEC"]),
        )
        kl_divergent_tensor = self.graph.get_tensor_by_name(
            name="loss/{}_kl_div:0".format(TENSOR_NAMES["OP_LOSS"]),
        )
        batch_latent_vectors, batch_kl_div = self.sess.run(
            fetches=[
                latent_tensor,
                kl_divergent_tensor,
            ],
            feed_dict={
                x_place: x_batch,
                seqlen_place: seqlen_batch,
            },
        )
        output = []
        for latent_vec, kl in zip(batch_latent_vectors, batch_kl_div):
            output.append((latent_vec, kl))
        return output

    def save(self, path: str):
        hyper_params = {
            "embedding_table": self.embedding_table,
            "n_steps": self.n_steps,
            "latent_size": self.latent_size,
            "input_dropout_ratio": self.input_dropout_ratio,
            "encoder_lstm_output_dropout_ratio":
                self.encoder_lstm_output_dropout_ratio,
            "encoder_lstm_state_dropout_ratio":
                self.encoder_lstm_state_dropout_ratio,
            "decoder_lstm_input_dropout_ratio":
                self.decoder_lstm_input_dropout_ratio,
            "decoder_lstm_output_dropout_ratio":
                self.decoder_lstm_output_dropout_ratio,
            "decoder_lstm_state_dropout_ratio":
                self.decoder_lstm_state_dropout_ratio,
            "l2_regularization": self.l2_regularization,
            "kl_lambda": self.kl_lambda,
            "max_grad_norm": self.max_grad_norm,
            "model_name": self.model_name,
        }
        super().save(
            path=path,
            hyper_params=hyper_params,
        )

    def gen_model_name(self, epoch):
        class_name = (self.__class__.__name__).lower()
        if self.model_name is not None:
            return self.model_name
        else:
            return class_name + "_model"

    def __del__(self):
        if self.initialize_graph:
            super(VAELstm2Lstm, self).__del__()
