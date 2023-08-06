from typing import List
import argparse
import json

from bistiming import SimpleTimer
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

from inference import inference


def knn_parser():
    parser = argparse.ArgumentParser(
        description='KNN Classification.')
    parser.add_argument(
        'model_path',
        type=str,
        help='text autoencoder model directory',
    )
    parser.add_argument(
        '-tra', '--training_dataset',
        type=str,
        help='input training dataset with class',
    )
    parser.add_argument(
        '-tes', '--testing_dataset',
        type=str,
        help='input testing dataset with class',
    )
    parser.add_argument(
        '-nn', '--n_neighbors',
        type=int,
        help='Number of neighbors to use by default for kneighbors queries.',
        default=5,
    )
    parser.add_argument(
        '-wg', '--weights',
        type=str,
        help='weight function used in prediction.',
        default='distance',
    )
    parser.add_argument(
        '-nj', '--n_jobs',
        type=int,
        help='The number of parallel jobs to run for neighbors search.',
        default=1,
    )
    return parser.parse_args()


def preprocessing(input_path: str):

    with open(input_path, 'r') as filep:
        data = json.load(filep)['data']

    X = []
    y = []
    for datum in data:
        X.append(datum['utterance'])
        y.append(datum['intent'])
    return X, y


def knn_classification(
        n_neighbors: int,
        weights: str,
        n_jobs: int,
        train_X: np.array,
        train_y: List[str],
        test_X: np.array,
        test_y: List[str],
    ) -> None:

    neigh = KNeighborsClassifier(
        n_neighbors=n_neighbors,
        weights=weights,
        n_jobs=n_jobs,
    )
    with SimpleTimer('Fitting'):
        neigh.fit(train_X, train_y)

    with SimpleTimer('Evaluating'):
        accuracy = neigh.score(test_X, test_y)

    print('accuracy = {}'.format(accuracy))


def main():
    args = knn_parser()
    # load and inference
    train_text, train_y = preprocessing(args.training_dataset)
    test_text, test_y = preprocessing(args.testing_dataset)

    train_X = inference(
        sentences=train_text,
        model_path=args.model_path,
    )
    test_X = inference(
        sentences=test_text,
        model_path=args.model_path,
    )

    knn_classification(
        n_neighbors=args.n_neighbors,
        weights=args.weights,
        n_jobs=args.n_jobs,
        train_X=train_X,
        train_y=train_y,
        test_X=test_X,
        test_y=test_y,
    )


if __name__ == '__main__':
    main()
