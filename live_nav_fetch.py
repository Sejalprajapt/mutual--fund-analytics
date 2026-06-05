import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

funds  = {
 "sbi_bluechips" : 119551,
 "icici_bluchips" : 120503,
 "nippon_large_cap": 118632,
 "axis_bluechips" : 119092,
 "kotak_bluechip" : 120841,
 "hdfc_top100": 125497
 }

for fund_name, code in funds.items():
    url = f"https://api.mfapi.in/mf/{code}"

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data["data"])

df.to_csv(f"data/raw/{fund_name}.csv", index=False)


print(f"{fund_name} saved successfully")