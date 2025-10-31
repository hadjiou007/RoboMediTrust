# RoboMediTrust: A Privacy-Preserving Robotic Framework for Collaborative Disease Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
<img width="1021" height="913" alt="image" src="https://github.com/user-attachments/assets/4b0209ac-37ca-4db8-9750-44e02f3bdc23" />

This repository contains the code for the **RoboMediTrust** framework, a novel approach for privacy-preserving, robot-mediated federated learning in healthcare.

## 🔍 Overview

RoboMediTrust integrates:
- **On-Device Diff-DNA Privacy**: Structural noise injection via DNA-inspired permutations.
  <img width="1024" height="846" alt="image" src="https://github.com/user-attachments/assets/804c3244-e393-419b-b0d3-6a5aac6bb0a7" />

- **Personalized RNN (PRM)**: Bi-LSTM + GRU model for accurate diagnosis.
  <img width="1045" height="583" alt="image" src="https://github.com/user-attachments/assets/fb7282f4-ec1a-44ad-929c-6fad96188d88" />

- **Federated Learning**: Decentralized training across hospitals.
- **Gaussian DP (DP-SGD)**: Model-level privacy.
- **SMPC Simulation**: Secure data transmission.
- **Generalization**: Validated across Heart, Breast Cancer, Kidney, and Lung diseases.

This project provides a Jupyter notebook and helper scripts to:

- download the UCI Heart Disease dataset (Cleveland / combined CSV),
- preprocess and impute missing values,
- apply data augmentation (SMOTE, ADASYN, numeric perturbation, bootstrap) to produce an expanded, balanced dataset,
- simulate a federated setup across 5 hospitals using Dirichlet partitioning (α = 0.4),
- save per-client datasets and the global augmented dataset,
- generate exploratory visualizations: missing-value bar plot, correlation heatmap, PCA 3D projection,
- train baseline models locally and evaluate metrics,

Achieves **96.7% accuracy** on heart disease with strong privacy (ε=1.2).

## 📂 File Structure

- `robot/`: Robotic unit logic and on-device privacy.
- `privacy/`: Diff-DNA, DP-SGD, and SMPC modules.
- `models/`: PRM model architecture.
- `experiments/`: Training scripts for Table 14 and generalization.
- `notebooks/`: Interactive demo.

📂 Data
Datasets can be downloaded from:

UCI Heart Disease : https://archive.ics.uci.edu/dataset/45/heart+disease
Breast Cancer : https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
chronic kidney disease :  https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease 
Lung cancer : https://archive.ics.uci.edu/dataset/62/lung+cancer 
alzheimers disease : https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset
Hypertension risk prediction : https://www.kaggle.com/datasets/ankushpanday1/hypertension-risk-prediction-dataset  


## 🚀 Quick Start

```bash
git clone https://github.com/hadjiou007/roboMediTrust.git
cd roboMediTrust
pip install -r requirements.txt



Notes
- All commonly used libraries are allowed; 
- The notebook downloads the dataset automatically from the UCI repository (or uses an alternative CSV if provided).
- The federated is offline: it partitions datasets into per-client folders and runs local training loops, then simulates FedAvg aggregation for demonstration.
