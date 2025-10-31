# privacy/dp_sgd.py
"""
Integrates DP-SGD for model-level privacy during federated training.
"""

import tensorflow as tf
from tensorflow_privacy.privacy.optimizers.dp_optimizer_keras import DPKerasSGDOptimizer

def get_dp_optimizer(l2_norm_clip=1.0, noise_multiplier=1.5, num_microbatches=1, learning_rate=0.001):
    """
    Creates a DP-SGD optimizer.
    Parameters tuned to achieve ε ≈ 1.0 as in Table 14.
    """
    return DPKerasSGDOptimizer(
        l2_norm_clip=l2_norm_clip,
        noise_multiplier=noise_multiplier,
        num_microbatches=num_microbatches,
        learning_rate=learning_rate
    )

# Example usage in model compilation
# model.compile(optimizer=get_dp_optimizer(), loss='binary_crossentropy', metrics=['accuracy'])