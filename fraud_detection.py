import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("fraud_data.csv")

# Features
X = df[
    ["Transaction_Amount",
     "Transaction_Time"]
]

# Target
y = df["Fraud"]

# Train Model
model = RandomForestClassifier(
    random_state=42
)

model.fit(X, y)

# Sample Transaction
transaction = [[12000, 1]]

prediction = model.predict(
    transaction
)

if prediction[0] == 1:
    print("🚨 Fraud Transaction")
else:
    print("✅ Genuine Transaction")