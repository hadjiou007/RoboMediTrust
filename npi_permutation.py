# privacy/diff_dna/npi_permutation.py
"""
Noise Permutation Individual (NPI) module.
Applies irreversible swaps to the nucleotide sequence.
"""

def apply_npi_sequence(sequence: str, indices: list) -> str:
    """
    Apply a series of swaps defined by index pairs in `indices`.
    Example: indices=[1,3,2,4] means swap pos 1<->3, then 2<->4.
    """
    chars = list(sequence)
    for i in range(0, len(indices)-1, 2):
        idx1, idx2 = indices[i], indices[i+1]
        if idx1 < len(chars) and idx2 < len(chars):
            chars[idx1], chars[idx2] = chars[idx2], chars[idx1]
    return ''.join(chars)