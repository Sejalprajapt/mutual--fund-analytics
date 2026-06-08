import pandas as pd
import os

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Keep positive transaction amounts
if "amount" in df.columns:
    df = df[df["amount"] > 0]

# Standardize transaction type
if "transaction_type" in df.columns:
    df["transaction_type"] = (
        df["transaction_type"]
        .str.strip()
        .str.upper()
    )

# Convert date column if present
if "transaction_date" in df.columns:
    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("Clean Transactions saved successfully")
print(df.shape)