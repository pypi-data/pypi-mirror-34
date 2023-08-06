import argparse
import yaml
import logging
import sys

from preprocessor import Preprocessor
from learning.train_test_split import train_test_split
from batching import BatchGenerator, BatchLoader
from autoencoders import *  # noqa


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def training_parser():
    parser = argparse.ArgumentParser(
        description='Training.')
    parser.add_argument(
        'config',
        type=str,
        help='model config path',
    )
    parser.add_argument(
        '-o',
        '--output_path',
        type=str,
        default='example',
        help='model output path',
    )
    parser.add_argument(
        '-tf_serving',
        action='store_true',
        help='tensorflow serving mode',
    )
    return parser.parse_args()


def train():
    '''
    ex:
    output_path = /home/example
    if tf_serving is False:
        preprocessor would be stored at /home/example_pre.msg
        model fragments path would be
            /home/example_[model_name]-param.pkl
            /home/example_[model_name]-variable.model

    else:
        preprocessor would be stored at /home/example_[model_name]/_pre.msg
        model fragments path would be
            /home/example_[model_name]/0/...
    '''

    args = training_parser()
    # load config
    with open(args.config, 'r') as filey:
        config = yaml.load(filey)

    # load training data
    with open(config['training_data_path'], 'r') as filep:
        sentences = filep.read().split('\n')

    # adaptor for tf_serving
    if args.tf_serving:
        args.output_path += '_{}/'.format(config['model_name'])

    # preprocessing
    pre = Preprocessor(
        word2index_path=config['word2index_path'],
        word_embedding_path=config['word_embedding_path'],
        logger=LOGGER,
        **config['preprocessor_params'],
    )
    pre.save(args.output_path)

    # preprocess sentence
    pre_sentences = pre.batch_preprocessing(sentences=sentences)

    # text to numerical
    data, seqlen = pre.batch_sent2indices(
        sentences=pre_sentences,
    )
    # train test split
    split_result = train_test_split(
        [data, seqlen],
        ratio=config['train_params']['valid_ratio'],
        shuffle=True,
        logger=LOGGER,
    )
    # train: batch generator
    subtrain_batch_gen = BatchGenerator(
        split_result['train'],
        batch_size=config['train_params']['batch_size'],
    )
    # valid: batch loader
    valid_batch_loader = BatchLoader(
        split_result['test'],
        batch_size=128,
        # config['train_params']['batch_size'],
    )
    model = globals()[config['model_name']](
        embedding_table=pre.word_embedding,
        n_steps=config['preprocessor_params']['maxlen'],
        **config['model_params'],
    )
    model.fit_generator(
        subtrain_batch_generator=subtrain_batch_gen,
        valid_batch_loader=valid_batch_loader,
        output_path=args.output_path,
        save_tf_serving=args.tf_serving,
        **config['train_params'],
    )


if __name__ == '__main__':
    train()
