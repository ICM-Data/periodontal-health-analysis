import pandas as pd
from src.data_cleaning import clean_data

def test_removes_duplicate_patient_ids():
    df = pd.DataFrame([
        {
            "patient_id": "P001", "age": 35, "sex": "F", "smoker": 0, "diabetes": 0,
            "bleeding_on_probing_pct": 25, "probing_depth_mm_mean": 3.0,
            "clinical_attachment_loss_mm_mean": 1.0
        },
        {
            "patient_id": "P001", "age": 35, "sex": "F", "smoker": 0, "diabetes": 0,
            "bleeding_on_probing_pct": 25, "probing_depth_mm_mean": 3.0,
            "clinical_attachment_loss_mm_mean": 1.0
        }
    ])

    result = clean_data(df)
    assert len(result) == 1
