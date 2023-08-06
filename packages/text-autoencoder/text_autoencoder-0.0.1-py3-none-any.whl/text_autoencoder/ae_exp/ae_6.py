from comet_ml import Experiment
import tensorflow as tf
import numpy as np

from utils import add_parent_path
add_parent_path()

from autoencoders.encoders import StackedCNN_LSTM
from autoencoders.decoders import LSTM_LatentVec_InitState
from losses import (  # noqa
    l2_regularization,
    mean_reconstruction_loss,
)
from toolkit.common import get_embedding

from utils import show_decoder_output, load_data


API_KEY = 'GiVOADfGHvpZ8KVjEg1iJHB2x'
experiment = Experiment(api_key=API_KEY, project_name='text-autoencoder')

BATCH_SIZE = 128
MAXLEN = 30
DISPLAY_ITER = 200
TRAIN_ITER = 20000
INIT_LR = 1e-3


def build_model(maxlen: int, embedding_table: np.array):
    input_X = tf.placeholder(
        dtype=tf.int32,
        shape=[None, maxlen],
    )
    seqlen = tf.placeholder(
        dtype=tf.int32,
        shape=[None],
    )
    assist_place = tf.placeholder(
        dtype=tf.int32,
        shape=(),
    )
    embedding_table = get_embedding(
        embedding_array=embedding_table,
        trainable=True,
    )
    with tf.variable_scope("encoder"):
        latent, _ = StackedCNN_LSTM(
            input_=input_X,
            seqlen=None,
            embedding_table=embedding_table,  # np.ndarray
            input_dropout=0.1,
            state_size=256,
            filter_structures=[
                (3, 1, 256),
                (3, 1, 512),
                # (3, 1, 512),
                # (5, 1, 1024),
            ],
            is_training=True,
            lstm_output_dropout=0.1,
        )

    with tf.variable_scope("decoder"):
        output_logits, output_word_indices = LSTM_LatentVec_InitState(
            init_state=tf.contrib.rnn.LSTMStateTuple(
                *(
                    latent,
                    tf.zeros(
                        shape=[tf.shape(latent)[0], latent.shape[1].value],
                        dtype=tf.float32,
                    ),
                ),
            ),
            latent_input=latent,  # batch_size * latent_size
            real_indices=input_X,  # batch_size * maxlen
            embedding_table=embedding_table,
            assist=assist_place,
        )
    recon_loss = mean_reconstruction_loss(
        pred_logits=output_logits,
        true_indices=input_X,
        num_indices=embedding_table.shape[0],
        seqlen=seqlen,
    )
    l2_regularization(scale=1e-5)

    loss_for_train = tf.add_n(
        tf.get_collection('losses'),
        name="total_loss",
    )
    tvars = tf.trainable_variables()

    optimizer = tf.train.AdamOptimizer(INIT_LR)
    gradvar = optimizer.compute_gradients(
        loss=loss_for_train,
        var_list=tvars,
    )
    clipped_grad = [
        (tf.clip_by_value(grad, -1., 1.), var) for grad, var in gradvar]
    train_op = optimizer.apply_gradients(  # noqa
        clipped_grad,
    )
    return input_X, seqlen, assist_place, train_op, recon_loss, output_word_indices


def train():
    data, subtrain_batch_gen, valid_batch_gen = load_data(
        batch_size=BATCH_SIZE, iterations=TRAIN_ITER, maxlen=MAXLEN)

    graph = tf.Graph()
    with graph.as_default():
        input_place, seqlen_place, assist_place, \
            train_op, recon_loss, word_indices = build_model(
                maxlen=MAXLEN,
                embedding_table=data.word_embedding,
            )

    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(graph=graph, config=config)

    def validate(assist):
        valid_loss_sum = []
        for valid_X, valid_seq in valid_batch_gen():
            loss = sess.run(
                recon_loss,
                feed_dict={
                    input_place: valid_X,
                    seqlen_place: valid_seq,
                    assist_place: assist,
                },
            )
            valid_loss_sum.append(loss)
        return np.mean(valid_loss_sum)

    with experiment.train():
        sess.run(
            tf.variables_initializer(
                var_list=graph.get_collection("variables"),
            ),
        )
        for count, (input_, seqlen) in enumerate(subtrain_batch_gen()):
            experiment.set_step(count)
            assist = int(count < 1000)
            train_loss, _ = sess.run(
                [recon_loss, train_op],
                feed_dict={
                    input_place: input_,
                    seqlen_place: seqlen,
                    assist_place: assist,
                },
            )
            experiment.log_metric("train_loss", train_loss, step=count)

            if count % DISPLAY_ITER == 0:
                decoded_word_indices = sess.run(
                    word_indices,
                    feed_dict={
                        input_place: input_,
                        seqlen_place: seqlen,
                        assist_place: assist,
                    },
                )
                valid_loss = validate(assist)
                print(
                    'Iteration {} - train_loss: {}, valid_loss: {}, assist: {}'.format(
                        count, train_loss, valid_loss, assist),
                )
                show_decoder_output(
                    real_word_indices=input_[0: 16],
                    gen_word_indices=decoded_word_indices[0: 16],
                    seqlen=seqlen[0: 16],
                    index2word=data.index2word,
                )
                experiment.log_metric("valid_loss", valid_loss, step=count)
    sess.close()


if __name__ == '__main__':
    train()
