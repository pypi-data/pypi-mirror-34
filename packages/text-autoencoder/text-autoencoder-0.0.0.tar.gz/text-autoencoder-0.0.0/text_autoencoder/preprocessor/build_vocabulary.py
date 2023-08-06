from typing import Dict, Tuple
from collections import Counter

from tqdm import tqdm


def build_vocabulary(
        input_path: str,
        max_size: int = None,
        sos_token: str = '<SOS>',
        eos_token: str = '<EOS>',
        unk_token: str = '<UNK>',
        pad_token: str = '<PAD>',
    ) -> Tuple[Dict[str, int], int]:

    max_len = 0
    tokens = [sos_token, eos_token, unk_token, pad_token]
    counter = Counter([])
    with open(input_path, 'r') as filep:
        for line in tqdm(
            filep,
            ascii=True,
            desc='build vocabulary',
        ):
            line = filep.readline().strip()
            tokens = line.split(' ')
            counter.update(tokens)

            if len(tokens) > max_len:
                max_len = len(tokens)

    trim_counter = counter.most_common(max_size)

    output_dict = {
        key: idx for idx, (key, _) in enumerate(
            trim_counter, len(tokens))
    }
    for idx, default_token in enumerate(tokens):
        if default_token not in output_dict:
            output_dict.update({default_token: idx})

    return output_dict, max_len
