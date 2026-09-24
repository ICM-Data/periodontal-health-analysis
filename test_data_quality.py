import pandas as pd
from src.data_cleaning import clean_data

def test_invalid_measurements_are_removed():
    df = pd.DataFrame([
        {"patient_id":"P001","age":45,"sex":"F","smoker":0,"diabetes":0,"bleeding_on_probing_pct":35,"probing_depth_mm_mean":3.5,"clinical_attachment_loss_mm_mean":1.5},
        {"patient_id":"P002","age":47,"sex":"M","smoker":1,"diabetes":0,"bleeding_on_probing_pct":140,"probing_depth_mm_mean":3.1,"clinical_attachment_loss_mm_mean":1.2},
    ])
    result = clean_data(df)
    assert len(result) == 1
    assert result.iloc[0]["patient_id"] == "P001"
