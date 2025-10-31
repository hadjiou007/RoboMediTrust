# privacy/ckks_simulation.py
import numpy as np
import tenseal as ts

def create_ckks_context(poly_modulus_degree=16384, coeff_mod_bit_sizes=[60, 40, 40, 60]):
    context = ts.context(
        scheme=ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=poly_modulus_degree,
        coeff_mod_bit_sizes=coeff_mod_bit_sizes,
        encryption_type=ts.ENCRYPTION_TYPE.ASYMMETRIC
    )
    context.global_scale = 2**40
    context.generate_galois_keys()
    return context

if __name__ == "__main__":
    context = create_ckks_context(poly_modulus_degree=16384)
    weights = np.array([0.123, -0.456, 0.789, 0.012])
    encrypted_weights = ts.ckks_vector(context, weights)
    
    print(f"✅ CKKS Context created with poly_mod_degree={context.poly_modulus_degree}")
    print(f"🔒 Encrypted {len(weights)} weights under CKKS")
    print(f"📊 Encryption size: ~{encrypted_weights.size() * 8 / 1e6:.2f} MB")