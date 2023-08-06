TENSOR_NAMES = {  # noqa
    "X_PLACE": "input_x_placeholder",
    "MASK_PLACE": "input_mask_placeholder",
    "LR_PLACE": "input_lr_placeholder",
    "DECODER_ASSIST_PLACE": "decoder_assist_place",
    "IS_TRAINING_PLACE": "input_is_training_placeholder",
    "DROPOUT_PLACE": "dropout_placeholder_with_default_0",
    "OP_LATENT_VEC": "op_latent_vector",
    "OP_LOSS": "op_loss",
    "OP_TRAIN": "op_train",
}

from .lstm2lstm import VAELstm2Lstm  # noqa
from .cnn2tcnn import VAECNN2tCNN  # noqa
