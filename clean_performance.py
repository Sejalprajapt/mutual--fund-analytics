import pandas as pd
import os

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Keep expense ratio in valid range
if "expense_ratio_pct" in df.columns:
    df = df[
        (df["expense_ratio_pct"] >= 0.1) &
        (df["expense_ratio_pct"] <= 2.5)
    ]

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("Clean Performance saved successfully")
print(df.shape)