from typing import List
import re
from glob import glob
from os.path import join, basename, dirname

import numpy as np
from serving_utils import Client

from .preprocessor import Preprocessor
from .autoencoders import *  # noqa
from .variational_autoencoders import *  # noqa


def inference(
        sentences: List[str],
        model_path: str,
        logger=None,
    ) -> np.ndarray:
    '''
    ex:
    model_path = /home/example
    preprocessor would be stored at /home/example_pre.msg
    model fragments path would be
        /home/example_[model_name]-param.pkl
        /home/example_[model_name]-variable.model
    '''

    # load preprocessor
    pre = Preprocessor.load(model_path)

    # preprocessing
    pre_sentences = pre.batch_preprocessing(
        sentences=sentences,
    )
    data, seqlen = pre.batch_sent2indices(
        sentences=pre_sentences,
    )

    # restore model
    param_path = glob(model_path + '*-param.pkl')[0]

    model_module_name = re.findall(
        '{}_(.+)-param.pkl'.format(model_path),
        param_path,
    )[0]

    model_module = globals()[model_module_name]
    model = model_module.load(model_path)
    output = model.encode(
        x=data,
        seqlen=seqlen,
        batch_size=32,
    )
    return output


def inference_tf_serving(
        sentences: List[str],
        client: Client,
        model_dir: str,
    ) -> np.ndarray:

    '''
    ex:
    model_dir = /home/example_[model_name]/
    preprocessor would be stored at /home/example_[model_name]/_pre.msg

    '''

    # load preprocessor
    pre = Preprocessor.load(join(model_dir, ''))

    # preprocessing
    pre_sentences = pre.batch_preprocessing(
        sentences=sentences,
    )
    data, seqlen = pre.batch_sent2indices(
        sentences=pre_sentences,
    )

    # get encode_tf_serving function
    model_dir_name = basename(dirname(model_dir))  # example_[model_name]
    model_class_name = model_dir_name.split('_')[-1]  # [model_name]
    model_class = globals()[model_class_name]

    output = model_class.encode_tf_serving(
        tf_serving_client=client,
        x=data,
        seqlen=seqlen,
        dir_name=model_dir_name,
    )
    return output
