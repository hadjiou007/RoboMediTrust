roboMediTrust/
├── robot/
│   ├── __init__.py
│   ├── robotic_unit.py              # Implements Pseudo Code 1
│   └── diff_dna_privacy.py          # On-device privacy engine
│
├── privacy/
│   ├── diff_dna/
│   │   ├── mnt_encoder.py           # MNT table from manuscript
│   │   ├── npi_engine.py            # NPI permutation logic
│   │   └── diff_dna_core.py         # Full Diff-DNA pipeline
│   ├── dp_sgd.py                    # DP-SGD optimizer
│   └── smpc_simulator.py            # SMPC key exchange and encryption sim
│
├── models/
│   ├── prm_model.py                 # PRM: Bi-LSTM + GRU
│   └── federated_client.py          # Local training with hyperparameters
│
├── data/
│   ├── uci_heart_disease.csv        # Original dataset
│   ├── augmented_data.csv           # After augmentation
│   └── preprocess.py                # Cleaning and encoding
│
├── experiments/
│   ├── train_baseline.py
│   ├── train_diff_dna.py            # Reproduce Table 14
│   ├── evaluate_configurations.py
│   └── generalization_across_diseases.py
│
├── notebooks/
│   └── full_pipeline_demo.ipynb     # Interactive reproduction of Fig. 10
│
├── results/
│   ├── accuracy_across_datasets.png
│   ├── table14_reproduced.csv
│   └── npi_simulation_results.txt
│
├── requirements.txt
├── README.md
└── LICENSE