import pandas as pd
import random

class MockTransactionStream:
    """Simulates a real-time stream of transaction data."""
    def get_batch(self, batch_size=5):
        """Generates a batch of new transactions."""
        batch = []
        for _ in range(batch_size):
            # Normal transaction
            amount = round(random.uniform(5.0, 200.0), 2)
            is_international = random.choice([0, 1])
            
            # Occasionally generate a fraudulent-looking transaction
            if random.random() < 0.05: # 5% chance of being an anomaly
                amount = round(random.uniform(1000.0, 5000.0), 2)
                is_international = 1
            
            batch.append({
                'timestamp': pd.to_datetime('now', utc=True),
                'amount': amount,
                'is_international': is_international
            })
        return pd.DataFrame(batch)