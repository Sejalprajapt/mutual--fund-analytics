import pandas as pd
files = [
    "data/raw/02_nav_history.csv",
    "data/raw/07_scheme_performance.csv",
    "data/raw/08_investor_transcations.csv"
        ]

for file in files:
    print("\n" + "="*50)
    print(file)

    df = pd.read_csv(file)

    print("columns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())
