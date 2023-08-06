from unittest import TestCase

import numpy as np

from ..train_test_split import train_test_split


class SplitTestCase(TestCase):

    def test_train_test_split(self):
        result = train_test_split(
            iterables=[
                np.array(
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [10, 11, 12],
                        [13, 14, 15],
                    ],
                ),
                np.array([1, 2, 3, 4, 5]),
                np.array([7, 8, 9, 10, 11]),
            ],
            ratio=0.2,
            shuffle=False,
        )
        self.assertEqual(
            set(['train', 'test']),
            set(result.keys()),
        )
        # ans_test = (item.tolist() for item in result['test'])
        self.assertEqual(
            ([[1, 2, 3]], [1], [7]),
            (result['test'][0].tolist(),
             result['test'][1].tolist(),
             result['test'][2].tolist(),),
        )
        self.assertEqual(
            ([
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13, 14, 15],
            ],
                [2, 3, 4, 5],
                [8, 9, 10, 11],
            ),
            (
                result['train'][0].tolist(),
                result['train'][1].tolist(),
                result['train'][2].tolist(),
            ),
        )
