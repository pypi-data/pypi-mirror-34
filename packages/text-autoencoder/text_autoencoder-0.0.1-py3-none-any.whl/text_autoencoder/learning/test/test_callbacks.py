from unittest import TestCase

from ..callbacks import (
    get_improvement,
)


class CallbacksTestCase(TestCase):

    def test_get_improvement(self):
        test_case_dict = {
            'case_1': {'current_loss': 0.8, 'min_loss': 0.5},
            'case_2': {'current_loss': 0.8, 'min_loss': 1},
            'case_3': {'current_loss': 0.8, 'min_loss': 0.80001},
            'case_4': {'current_loss': 0.8, 'min_loss': 0.85, 'epsilon': 0.1},
            'case_5': {'current_loss': 0.8, 'min_loss': 0.95, 'epsilon': 0.1},
        }
        answer_dict = {
            'case_1': (0.5, False),
            'case_2': (0.8, True),
            'case_3': (0.80001, False),
            'case_4': (0.85, False),
            'case_5': (0.8, True),
        }
        for key, val in test_case_dict.items():
            self.assertEqual(answer_dict[key], get_improvement(**val))
