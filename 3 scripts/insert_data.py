import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# DATABASE CONFIG
# -----------------------------

DB_USER = "postgres"
DB_PASSWORD = "123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fintech_analytics"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

# -----------------------------
# LOAD CSV
# -----------------------------

df = pd.read_csv("data/raw/transactions_update.csv")

# -----------------------------
# INSERT INTO DATABASE
# -----------------------------

df.to_sql(
    "transactions",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully!")