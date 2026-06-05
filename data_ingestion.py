import pandas as pd
import os

folder = "Data/raw"
# look inside Data/raw folder
for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path)
        print("\n" + "="*50)
        print("File:", file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())
