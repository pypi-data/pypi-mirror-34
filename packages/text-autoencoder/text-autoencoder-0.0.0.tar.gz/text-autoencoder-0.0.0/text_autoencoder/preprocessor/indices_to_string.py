from typing import List, Dict


def indices2string(
        self,
        word_indices: List[int],  # np.array
        index2word: Dict[int, str],
        seqlen: int = None,
    ) -> str:

    output_str = ''

    if seqlen is None:
        seqlen = len(word_indices)

    for j, ind in enumerate(word_indices):
        if j >= seqlen:
            break
        output_str += index2word[ind]

    return output_str
