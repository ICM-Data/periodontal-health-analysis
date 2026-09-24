from pathlib import Path

from src.data_cleaning import load_data, clean_data
from src.analysis import assign_periodontal_status
from src.database import save_to_sqlite

def run_etl(source_csv: str, output_csv: str, db_path: str):
    df = load_data(source_csv)
    df = clean_data(df)
    df = assign_periodontal_status(df)

    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_csv, index=False)
    save_to_sqlite(df, db_path)

    return df
