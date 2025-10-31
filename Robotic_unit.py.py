# robot/robotic_unit.py
"""
Handles patient interaction, data collection, and on-device privacy.
"""

import time
import numpy as np
from robot.diff_dna_privacy import apply_diff_dna_privacy
from privacy.smpc_sim import encrypt_data, decrypt_result
from models.federated_client import load_global_model, secure_inference

class MedicalRobot:
    def __init__(self, hospital_pub_key, robot_priv_key):
        self.hospital_pub_key = hospital_pub_key
        self.robot_priv_key = robot_priv_key
        self.global_model = None
        self.is_connected = False

    def power_on(self):
        print("🤖 Robot: Powering on...")
        return self.self_check()

    def self_check(self):
        print("🔍 Robot: Running system diagnostics...")
        time.sleep(1)
        print("✅ System OK")
        return True

    def detect_patient(self):
        print("👀 Robot: Waiting for patient...")
        time.sleep(2)  # Simulate detection
        print("👋 Patient detected!")
        return True

    def guide_patient(self):
        print("🎙️ Robot: Please place your fingers on the sensors.")
        print("📊 Measuring ECG, Blood Pressure, SpO₂...")

    def read_sensors(self):
        """Simulate reading real physiological data."""
        # In practice, this would interface with hardware
        mock_data = {
            'age': 52,
            'sex': 1,
            'cp': 0,
            'trestbps': 125,
            'chol': 212,
            'fbs': 0,
            'restecg': 1,
            'thalach': 168,
            'exang': 0,
            'oldpeak': 1.0,
            'slope': 2,
            'ca': 2,
            'thal': 3
        }
        print(f"📋 Raw data collected: {mock_data}")
        return mock_data

    def apply_local_privacy(self, raw_data):
        """Apply Diff-DNA privacy on-device."""
        print("🔒 Applying Diff-DNA privacy (on-device)...")
        private_data = apply_diff_dna_privacy(raw_data)
        return private_data

    def transmit_or_infer(self, encrypted_data):
        """Send to hospital or infer locally if offline."""
        if self.is_connected:
            print("📤 Sending encrypted data to hospital network...")
            return "Sent"
        else:
            print("📴 No connection. Performing local secure inference...")
            if not self.global_model:
                self.global_model = load_global_model()
            prediction_encrypted = secure_inference(self.global_model, encrypted_data)
            result_cleartext = decrypt_result(prediction_encrypted, self.robot_priv_key)
            print(f"💡 Diagnosis: {result_cleartext}")
            return result_cleartext

    def run_full_cycle(self, online=True):
        """Execute the full RoboMediTrust workflow."""
        self.is_connected = online

        # 1. Initialization
        if not self.power_on():
            print("❌ System failure.")
            return

        # 2. Wait for patient
        if not self.detect_patient():
            return

        # 3. Guide patient
        self.guide_patient()

        # 4. Collect vital signs
        raw_data = self.read_sensors()

        # 5. Apply differential privacy
        private_data = self.apply_local_privacy(raw_data)

        # 6. Encrypt data
        encrypted_data = encrypt_data(private_data, self.hospital_pub_key)
        print(f"🔐 Data encrypted: {len(str(encrypted_data))} bytes")

        # 7. Transmit or perform secure inference
        result = self.transmit_or_infer(encrypted_data)

        # 8. Present result to patient
        if not self.is_connected:
            print(f"📢 Robot: Your heart health status is: {result}")

        print("🔚 Session complete. Logging anonymized ID.")

if __name__ == "__main__":

    HOSPITAL_PUB_KEY = "HOSP_PUB_123"
    ROBOT_PRIV_KEY = "ROBOT_PRIV_456"

    robot = MedicalRobot(HOSPITAL_PUB_KEY, ROBOT_PRIV_KEY)
    robot.run_full_cycle(online=False)  # Demo in offline mode