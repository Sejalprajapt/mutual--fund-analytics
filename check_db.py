import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")
cursor = conn.cursor()

for table in ["fact_nav", "fact_transactions", "fact_performance"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(table, ":", cursor.fetchone()[0])

conn.close()