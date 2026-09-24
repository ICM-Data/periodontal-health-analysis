import pandas as pd
from src.etl import run_etl

def test_run_etl_creates_outputs(tmp_path):
    source = tmp_path / "source.csv"
    output = tmp_path / "cleaned.csv"
    database = tmp_path / "periodontal.db"

    pd.DataFrame(
        [
            {
                "patient_id": "P001",
                "age": 35,
                "sex": "F",
                "smoker": 0,
                "diabetes": 0,
                "bleeding_on_probing_pct": 20,
                "probing_depth_mm_mean": 2.5,
                "clinical_attachment_loss_mm_mean": 0.7,
            }
        ]
    ).to_csv(source, index=False)

    result = run_etl(
        str(source),
        str(output),
        str(database),
    )

    assert len(result) == 1
    assert output.exists()
    assert database.exists()
    assert "periodontal_status" in result.columns
