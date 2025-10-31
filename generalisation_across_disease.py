# experiments/generalization_across_diseases.py
"""
Evaluates RoboMediTrust on multiple disease datasets.
Reproduces generalization claim from Section 5.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from models.prm_model import build_prm_model
import tensorflow as tf

datasets = {
    "Heart": "data/uci_heart_disease.csv",
    "Breast Cancer": "data/breast_cancer.csv",
    "Kidney": "data/kidney_disease.csv",
    "Lung Cancer": "data/lung_cancer.csv"
}

results = []

for name, path in datasets.items():
    try:
        df = pd.read_csv(path)
        X = df.drop(columns=[df.columns[-1]])  # Assume last column is target
        y = df[df.columns[-1]]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = build_prm_model(input_dim=X_train_scaled.shape[1])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, verbose=0)
        
        preds = (model.predict(X_test_scaled) > 0.5).astype(int)
        acc = accuracy_score(y_test, preds)
        
        results.append({"Dataset": name, "Accuracy (%)": round(acc*100, 1)})
        
    except Exception as e:
        print(f"Error processing {name}: {e}")

print(pd.DataFrame(results))