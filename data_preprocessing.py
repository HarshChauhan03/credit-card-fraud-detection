import pandas as pd

# Sample Dataset

data = {
    "Transaction_Amount": [100, 5000, 200, 15000, 300],
    "Transaction_Time": [10, 23, 14, 2, 18],
    "Fraud": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print(df)

df.to_csv(
    "fraud_data.csv",
    index=False
)

print("Dataset Saved Successfully")