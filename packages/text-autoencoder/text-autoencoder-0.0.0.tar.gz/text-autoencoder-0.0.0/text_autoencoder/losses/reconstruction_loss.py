import tensorflow as tf
from tensorflow.python.framework import ops


def batch_reconstruction_loss(
        pred_logits: tf.Tensor,  # float32
        true_indices: tf.Tensor,  # int32
        num_indices: int,
        seqlen: tf.Tensor = None,
        dtype: tf.DType = tf.float32,
        name: str = 'batch_reconstruction_loss',
    ) -> tf.Tensor:
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(
        logits=pred_logits,
        labels=tf.one_hot(
            true_indices,
            depth=num_indices,
        ),
        dim=2,
    )
    if seqlen is not None:
        mask = tf.sequence_mask(
            lengths=seqlen,
            maxlen=true_indices.shape[1],
            dtype=dtype,
            name='seq_mask',
        )
        cross_entropy = mask * cross_entropy

    batch_recon_loss = tf.reduce_sum(
        input_tensor=cross_entropy,
        axis=1,
        name=name,
    )
    return batch_recon_loss


def mean_reconstruction_loss(
        pred_logits: tf.Tensor,  # float32
        true_indices: tf.Tensor,  # int32
        num_indices: int,
        seqlen: tf.Tensor = None,
        dtype: tf.DType = tf.float32,
        name: str = 'mean_reconstruction_loss',
        loss_collection: str = ops.GraphKeys.LOSSES,
    ) -> tf.Tensor:
    batch_recon_loss = batch_reconstruction_loss(
        pred_logits=pred_logits,
        true_indices=true_indices,
        num_indices=num_indices,
        seqlen=seqlen,
        dtype=dtype,
    )
    if seqlen is not None:
        mean_recon_loss = tf.reduce_mean(
            tf.divide(
                batch_recon_loss,
                tf.cast(seqlen, dtype=dtype),
            ),
            name=name,
        )
    else:
        mean_recon_loss = tf.reduce_mean(
            batch_recon_loss,
            name=name,
        )
    tf.add_to_collection(
        name=loss_collection,
        value=mean_recon_loss,
    )
    return mean_recon_loss
