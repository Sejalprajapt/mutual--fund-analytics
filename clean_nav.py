import pandas as pd
import os

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

df = df.drop_duplicates()

df = df[df["nav"] > 0]

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

os.makedirs("data/processed", exist_ok=True)

df.to_csv("data/processed/clean_nav.csv", index=False)

print("Clean NAV saved successfully")
print(df.shape)