TENSOR_NAMES = {  # noqa
    "X_PLACE": "input_x_placeholder",
    "SEQLEN_PLACE": "input_seqlen_placeholder",
    "LR_PLACE": "input_lr_placeholder",
    "IS_TRAINING_PLACE": "input_is_training_placeholder",
    "DECODER_ASSIST_PLACE": "decoder_assist_place",
    "DROPOUT_PLACE": "dropout_placeholder_with_default_0",
    "OP_LATENT_VEC": "op_latent_vector",
    "OP_LOSS": "op_loss",
    "OP_TRAIN": "op_train",
}


from .base_autoencoder import BaseAutoencoder  # noqa
from .ae_1 import AE1  # noqa
