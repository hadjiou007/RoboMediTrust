# robot/diff_dna_privacy.py
"""
Applies Diff-DNA privacy as per Section 3.2.3 and Table (NPI).
Uses MNT mapping and NPI permutations for structural noise.
"""

from privacy.diff_dna.encoder import encode_features_to_nld
from privacy.diff_dna.npi_permutation import apply_npi_sequence

def apply_diff_dna_privacy(patient_data: dict) -> str:
    """
    End-to-end Diff-DNA application on raw patient data.
    Returns a perturbed DNA-like string.
    """
    # Step 1: Encode features to Nucleotide-Level Data (NLD)
    nld_string = encode_features_to_nld(patient_data)
    print(f"🧬 Encoded to NLD: {nld_string[:50]}...")

    # Step 2: Apply Noise Permutation Individual (NPI)
    # Using [1,3], [2,4] as per Table example
    npi_indices = [1, 3, 2, 4]
    perturbed_nld = apply_npi_sequence(nld_string, npi_indices)
    print(f"🌀 After NPI {npi_indices}: {perturbed_nld[:50]}...")

    return perturbed_nld