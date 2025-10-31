"""
RoboMediTrust - Training & Evaluation Notebook
Reproduces results across multiple datasets and generates training curves.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, LSTM, GRU, Bidirectional
from tensorflow.keras.optimizers import Adam

# Set style
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12})

# -------------------------------
# Load and Preprocess Multiple Datasets
# -------------------------------

datasets = {
    "Heart Disease": {"path": "data/uci_heart_disease.csv", "target_col": "target"},
    "Breast Cancer": {"path": "data/breast_cancer.csv", "target_col": "diagnosis"},
    "Chronic Kidney Disease": {"path": "data/kidney_disease.csv", "target_col": "class"},
    "Lung Cancer": {"path": "data/lung_cancer.csv", "target_col": "result"}
}

results_summary = []

for name, info in datasets.items():
    print(f"\n📊 Loading dataset: {name}")
    
    try:
        data = pd.read_csv(info["path"])
    except FileNotFoundError:
        print(f"⚠️ Dataset {name} not found. Skipping.")
        continue

    # Handle target encoding (binary)
    if info["target_col"] in data.columns:
        y = (data[info["target_col"]] == data[info["target_col"]].unique()[0]).astype(int)
        X = data.drop(columns=[info["target_col"]])
    else:
        print(f"⚠️ Target column {info['target_col']} not found. Skipping.")
        continue

    # Encode categorical features
    for col in X.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))

    # Normalize numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build PRM Model (Bi-LSTM + GRU)
    model = Sequential([
        Input(shape=(X_train.shape[1],)),
        Dense(64, activation='relu'),
        tf.keras.layers.Reshape((X_train.shape[1], 1)),  # Prepare for RNN
        Bidirectional(LSTM(32, return_sequences=True)),
        GRU(16, return_sequences=False),
        Dropout(0.3),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy', 'precision', 'recall'])

    # Train model
    print(f"🚀 Training on {name}...")
    history = model.fit(X_train, y_train,
                        validation_data=(X_test, y_test),
                        epochs=50,
                        batch_size=32,
                        verbose=0)

    # Evaluate
    loss, accuracy, precision, recall = model.evaluate(X_test, y_test, verbose=0)
    f1 = 2 * (precision * recall) / (precision + recall + 1e-8)

    results_summary.append({
        "Dataset": name,
        "Instances": len(data),
        "Attributes": X.shape[1],
        "Accuracy (%)": round(accuracy * 100, 1),
        "Sensitivity (%)": round(recall * 100, 1),
        "Specificity (%)": round((1 - (np.sum(y_test == 0) - np.sum((1-model.predict(X_test).round()) == 0)) / np.sum(y_test == 0))) * 100, 1),
        "F1-Score": round(f1, 3)
    })

# -------------------------------
# Plot Accuracy Across Datasets
# -------------------------------
df_results = pd.DataFrame(results_summary)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df_results, x="Dataset", y="Accuracy (%)", palette="viridis", ax=ax)
ax.set_title("Model Accuracy Across Medical Datasets")
ax.set_ylabel("Test Accuracy (%)")
for i, v in enumerate(df_results["Accuracy (%)"]):
    ax.text(i, v + 0.5, f"{v}", ha='center', va='bottom')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("results/accuracy_across_datasets.png", dpi=300, bbox_inches='tight')
plt.show()

# -------------------------------
# Display Results Table (Generalization)
# -------------------------------
print("\n📋 Generalization Performance Across Diseases:")
print(df_results.to_markdown(index=False, floatfmt=".1f"))

# Save to CSV
df_results.to_csv("results/generalization_results.csv", index=False)