import pandas as pd
from src.database import save_to_sqlite, query_sqlite

def test_save_and_query_sqlite(tmp_path):
    db_path = tmp_path / "test.db"

    df = pd.DataFrame(
        {
            "patient_id": ["P001", "P002"],
            "age": [30, 45],
        }
    )

    save_to_sqlite(df, str(db_path), table_name="patients")

    result = query_sqlite(
        str(db_path),
        "SELECT COUNT(*) AS total FROM patients",
    )

    assert result.loc[0, "total"] == 2
