# privacy/diff_dna/encoder.py
"""
Mapping Nucleotides Table (MNT) for Diff-DNA.
Converts numerical/categorical values to DNA-like sequences.
"""

# Simplified MNT based on manuscript examples
MNT = {
    '0': 'AAA', '1': 'AAC', '2': 'AAG', '3': 'AAT',
    '4': 'ACA', '5': 'ACC', '6': 'ACG', '7': 'ACT',
    '8': 'AGA', '9': 'AGC',
    'A': 'TAT', 'B': 'TAC', 'C': 'TAG', 'D': 'TAA',
    'E': 'TTT', 'F': 'TTC', 'G': 'TTG', 'H': 'TTA',
    'I': 'CTT', 'J': 'CTC', 'K': 'CTG', 'L': 'CTA',
    'M': 'CGT', 'N': 'CGC', 'O': 'CGG', 'P': 'CGA',
    'Q': 'CAT', 'R': 'CAC', 'S': 'CAA', 'T': 'CCT',
    'U': 'CCC', 'V': 'CCG', 'W': 'CCA', 'X': 'ACT',
    'Y': 'ACC', 'Z': 'ACG'
}

def map_char_to_nucleotide(char: str) -> str:
    return MNT.get(char.upper(), 'XXX')

def encode_text_to_nld(text: str) -> str:
    return ''.join([map_char_to_nucleotide(c) for c in text])

def encode_features_to_nld(features: dict) -> str:
    """
    Convert a patient feature dictionary to a single NLD string.
    Mimics the process in the manuscript's nucleotide representation table.
    """
    flat_str = ''.join([str(v) for v in features.values()])
    return encode_text_to_nld(flat_str)