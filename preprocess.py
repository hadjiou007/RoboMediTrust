# data/preprocess.py
"""
Data preprocessing and augmentation for UCI Heart Disease dataset.
Generates synthetic samples to handle class imbalance.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def augment_data(df, target_col='target', factor=1.5):
    """Generate synthetic samples for minority class."""
    df_minority = df[df[target_col] == 1]
    new_samples = []
    
    for _ in range(int(len(df_minority) * factor)):
        sample = df_minority.sample().iloc[0].copy()
        # Add small noise
        for col in df_minority.select_dtypes(include=[np.number]).columns:
            if col != target_col:
                sample[col] += np.random.normal(0, 0.02 * df[col].std())
        new_samples.append(sample)
    
    augmented_df = pd.concat([df, pd.DataFrame(new_samples)], ignore_index=True)
    return augmented_df

# Usage
# df = pd.read_csv('data/uci_heart_disease.csv')
# df_augmented = augment_data(df)
# df_augmented.to_csv('data/augmented_data.csv', index=False)