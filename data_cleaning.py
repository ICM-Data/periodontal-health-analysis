import pandas as pd

REQUIRED_COLUMNS = [
    "patient_id",
    "age",
    "sex",
    "smoker",
    "diabetes",
    "bleeding_on_probing_pct",
    "probing_depth_mm_mean",
    "clinical_attachment_loss_mm_mean",
]

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def validate_columns(df: pd.DataFrame) -> None:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    cleaned = df.copy()

    numeric_columns = [
        "age",
        "smoker",
        "diabetes",
        "bleeding_on_probing_pct",
        "probing_depth_mm_mean",
        "clinical_attachment_loss_mm_mean",
    ]

    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    cleaned = cleaned.drop_duplicates(subset=["patient_id"])
    cleaned = cleaned.dropna(subset=REQUIRED_COLUMNS)

    cleaned = cleaned[
        cleaned["age"].between(18, 100)
        & cleaned["bleeding_on_probing_pct"].between(0, 100)
        & cleaned["probing_depth_mm_mean"].between(0, 15)
        & cleaned["clinical_attachment_loss_mm_mean"].between(0, 15)
    ]

    cleaned["smoker"] = cleaned["smoker"].astype(int)
    cleaned["diabetes"] = cleaned["diabetes"].astype(int)

    return cleaned.reset_index(drop=True)
