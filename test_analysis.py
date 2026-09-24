import pandas as pd
from src.analysis import assign_periodontal_status

def test_assigns_severe_status():
    df = pd.DataFrame([{
        "probing_depth_mm_mean": 5.2,
        "clinical_attachment_loss_mm_mean": 4.1,
        "bleeding_on_probing_pct": 60,
    }])

    result = assign_periodontal_status(df)
    assert result.loc[0, "periodontal_status"] == "Severe"

def test_assigns_low_risk_status():
    df = pd.DataFrame([{
        "probing_depth_mm_mean": 2.1,
        "clinical_attachment_loss_mm_mean": 0.4,
        "bleeding_on_probing_pct": 12,
    }])

    result = assign_periodontal_status(df)
    assert result.loc[0, "periodontal_status"] == "Healthy/Low risk"
