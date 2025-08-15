# Real-time Fraud Detection System

## 📝 Project Overview

This project is a proof-of-concept for a real-time fraud detection system. It uses an **Isolation Forest** machine learning model to identify anomalous transactions from a simulated high-volume data stream. The system is designed to flag potentially fraudulent activity instantly, demonstrating a practical application of unsupervised learning for risk management.

---

## ✨ Key Features

-   **Real-time Simulation**: A Python script simulates a continuous stream of transaction data, including both normal and fraudulent events.
-   **Anomaly Detection**: Utilizes `scikit-learn`'s Isolation Forest model, which is effective for identifying outliers in data without needing pre-labeled examples of fraud.
-   **Automated Alerts**: The system processes transactions in micro-batches and prints a clear alert when a potentially fraudulent transaction is detected.
-   **Modular Code**: The project is structured with separate modules for data simulation, model training, and real-time detection, making it easy to understand and extend.

---

## 🛠️ Technologies Used

-   **Python**: Core programming language.
-   **Pandas**: For data manipulation and analysis.
-   **Scikit-learn**: For building and training the Isolation Forest model.
-   **Jupyter Notebook**: For exploratory data analysis (EDA).

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-github-username/real-time-fraud-detection.git](https://github.com/your-github-username/real-time-fraud-detection.git)
    cd real-time-fraud-detection
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the real-time detection script:**
    The script will first train a model on a sample of 5,000 simulated transactions and then begin processing new transactions in real-time.
    ```bash
    python src/detect_fraud.py
    ```
    *To stop the simulation, press `CTRL + C`.*

---

## 📊 Sample Output

When a fraudulent transaction is detected, you will see an alert like this in the console:

```
*** ALERT: Potential Fraudulent Activity Detected! ***
      timestamp      amount  is_international  is_fraud
2  1678886400.0     3450.78                 1         1