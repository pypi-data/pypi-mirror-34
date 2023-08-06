from typing import List, Tuple, Dict

import numpy as np


def sentence2indices(
        sentence: List[str],
        sos_token: str,
        eos_token: str,
        unk_token: str,
        pad_token: str,
        word2index: Dict[str, int],
        maxlen: int,
        logger: object = None,
    ) -> Tuple[np.ndarray, int]:

    # assign pad index
    pad_index = word2index[pad_token]
    output_array = pad_index * np.ones(maxlen).astype('int32')

    # assign sos index
    output_array[0] = word2index[sos_token]

    if (len(sentence) > (maxlen - 2)) and (logger is not None):
        logger.warning(
            'the length of input sentence: [{}] is more than maxlen {}'.format(
                sentence, maxlen - 2,
            ),
        )

    tokens = sentence[: maxlen - 2]
    for i, token in enumerate(tokens, 1):
        if token not in word2index:
            # assign unk index
            output_array[i] = word2index[unk_token]
        else:
            output_array[i] = word2index[token]

    # assign eos index
    output_array[i + 1] = word2index[eos_token]

    return output_array.astype('int32'), len(tokens) + 2
