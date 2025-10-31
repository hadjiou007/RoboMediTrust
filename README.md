# RoboMediTrust: A Privacy-Preserving Robotic Framework for Collaborative Disease Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This repository contains the code for the **RoboMediTrust** framework, a novel approach for privacy-preserving, robot-mediated federated learning in healthcare.

## 🔍 Overview

RoboMediTrust integrates:
- **On-Device Diff-DNA Privacy**: Structural noise injection via DNA-inspired permutations.
- **Personalized RNN (PRM)**: Bi-LSTM + GRU model for accurate diagnosis.
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

## 🚀 Quick Start

```bash
git clone https://github.com/hadjiou007/roboMediTrust.git
cd roboMediTrust
pip install -r requirements.txt



Notes
- All commonly used libraries are allowed; 
- The notebook downloads the dataset automatically from the UCI repository (or uses an alternative CSV if provided).
- The federated is offline: it partitions datasets into per-client folders and runs local training loops, then simulates FedAvg aggregation for demonstration.
