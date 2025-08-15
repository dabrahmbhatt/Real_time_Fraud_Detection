import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# --- 1. Load Historical Data ---

def load_data(file_path):
    """Loads transaction data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from '{file_path}'.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# --- 2. Train and Save Model ---

def train_and_save_model(df, model_path):
    """Trains an Isolation Forest model and saves it to a file."""
    if df is None:
        print("Cannot train model, data not loaded.")
        return

    print("Training fraud detection model...")
    
    # Define features for the model
    features = df[['amount', 'is_international']]
    
    # Initialize the model
    # Contamination is the expected proportion of anomalies in the data
    model = IsolationForest(contamination=0.1, random_state=42)
    
    # Train the model
    model.fit(features)
    print("Model training complete.")
    
    # Ensure the 'models' directory exists
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # Save the trained model to the specified path
    joblib.dump(model, model_path)
    print(f"Model saved successfully to '{model_path}'.")

# --- Main Execution ---

if __name__ == "__main__":
    # Define file paths
    data_file_path = os.path.join('data', 'historical_transactions.csv')
    model_file_path = os.path.join('models', 'fraud_detector.joblib')

    # Run the training pipeline
    historical_data = load_data(data_file_path)
    if historical_data is not None:
        train_and_save_model(historical_data, model_file_path)
