import pandas as pd
import sqlite3
import os

# Set path to CSV and DB
csv_path = os.path.join("..", "data", "Online Retail.csv")
db_path = os.path.join("..", "data", "online_retail.db")

# Read CSV (semicolon-delimited and encoded in latin1)
df = pd.read_csv(csv_path)

# Drop rows where InvoiceNo or StockCode is missing (critical fields)
df = df.dropna(subset=["InvoiceNo", "StockCode"])

# Standardize column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# Save to SQLite
with sqlite3.connect(db_path) as conn:
    df.to_sql("online_retail", conn, if_exists="replace", index=False)

print("✅ The database has been created: online_retail.db")
