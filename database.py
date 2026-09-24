import sqlite3
import pandas as pd

TABLE_NAME = "periodontal_patients"

def save_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str = TABLE_NAME) -> None:
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)

def query_sqlite(db_path: str, query: str) -> pd.DataFrame:
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query(query, conn)
