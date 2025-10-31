# models/prm_model.py
"""
Personalized RNN Model (PRM) with Bi-LSTM + GRU block.
Implements Fig. 7 architecture.
"""

import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model

def build_prm_model(input_dim=24, embedding_dim=64):
    inputs = Input(shape=(input_dim,), name="feature_input")

    # Patch Embedding
    x = Embedding(input_dim=1000, output_dim=embedding_dim)(inputs)
    x = Reshape((-1, embedding_dim))(x)

    # Positional Encoding
    positions = tf.range(start=0, limit=input_dim, delta=1)
    pos_encoding = Embedding(input_dim=input_dim, output_dim=embedding_dim)(positions)
    x = x + pos_encoding

    # Bidirectional LSTM + GRU Block
    x = Bidirectional(LSTM(64, return_sequences=True, dropout=0.3))(x)
    x = GRU(32, return_sequences=False, dropout=0.3)(x)

    # Output Layer
    outputs = Dense(1, activation='sigmoid', name="diagnosis")(x)

    model = Model(inputs=inputs, outputs=outputs)
    return model