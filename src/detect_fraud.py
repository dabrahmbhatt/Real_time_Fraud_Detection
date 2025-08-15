import pandas as pd
import joblib
import time
import os
from data_simulation import MockTransactionStream # <-- CORRECTED IMPORT

# --- 1. Load Pre-trained Model ---

def load_model(model_path):
    """Loads a pre-trained model from a .joblib file."""
    try:
        model = joblib.load(model_path)
        print(f"Model loaded successfully from '{model_path}'.")
        return model
    except FileNotFoundError:
        print(f"Error: Model file not found at '{model_path}'.")
        print("Please run 'train_model.py' first to train and save the model.")
        return None

# --- 2. Real-time Prediction ---

def predict_real_time(model, stream):
    """Processes a stream of transactions and predicts fraud."""
    if model is None:
        return

    print("\n--- Starting Real-time Fraud Detection ---")
    try:
        while True:
            # Get a new batch of transactions from the imported stream class
            new_transactions_df = stream.get_batch(batch_size=5)
            print("\nReceived new batch of transactions:")
            print(new_transactions_df[['amount', 'is_international']])
            
            # Use the loaded model to predict fraud
            features = new_transactions_df[['amount', 'is_international']]
            predictions = model.predict(features)
            new_transactions_df['is_fraud_prediction'] = [1 if p == -1 else 0 for p in predictions]
            
            # Identify and report fraudulent transactions
            flagged_transactions = new_transactions_df[new_transactions_df['is_fraud_prediction'] == 1]
            
            if not flagged_transactions.empty:
                print("\n\033[91m*** ALERT: Potential Fraudulent Activity Detected! ***\033[0m")
                print(flagged_transactions)
            else:
                print("No fraudulent activity detected in this batch.")

            time.sleep(4)
    except KeyboardInterrupt:
        print("\n--- Stopping Real-time Fraud Detection ---")

# --- Main Execution ---

if __name__ == "__main__":
    # Define the path to the saved model
    model_file_path = os.path.join('models', 'fraud_detector.joblib')

    # Load the model
    fraud_detection_model = load_model(model_file_path)
    
    # Initialize the transaction stream from the imported class
    transaction_stream = MockTransactionStream()
    
    # Start the detection process
    predict_real_time(fraud_detection_model, transaction_stream)
