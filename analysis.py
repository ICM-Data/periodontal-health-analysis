import pandas as pd

def assign_periodontal_status(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    def classify(row):
        depth = row["probing_depth_mm_mean"]
        cal = row["clinical_attachment_loss_mm_mean"]
        bop = row["bleeding_on_probing_pct"]

        if depth >= 5 or cal >= 4:
            return "Severe"
        if depth >= 4 or cal >= 2:
            return "Moderate"
        if depth >= 3 or bop >= 30:
            return "Mild"
        return "Healthy/Low risk"

    result["periodontal_status"] = result.apply(classify, axis=1)
    return result

def create_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("periodontal_status", dropna=False)
          .agg(
              patients=("patient_id", "count"),
              mean_age=("age", "mean"),
              mean_bop_pct=("bleeding_on_probing_pct", "mean"),
              mean_probing_depth=("probing_depth_mm_mean", "mean"),
              mean_attachment_loss=("clinical_attachment_loss_mm_mean", "mean"),
              smoker_rate=("smoker", "mean"),
              diabetes_rate=("diabetes", "mean"),
          )
          .reset_index()
          .sort_values("patients", ascending=False)
    )

def risk_factor_summary(df: pd.DataFrame) -> pd.DataFrame:
    risk = df.assign(
        high_risk=df["periodontal_status"].isin(["Moderate", "Severe"]).astype(int)
    )

    rows = []
    for factor in ["smoker", "diabetes"]:
        grouped = (
            risk.groupby(factor)
                .agg(
                    patients=("patient_id", "count"),
                    high_risk_rate=("high_risk", "mean"),
                    mean_bop_pct=("bleeding_on_probing_pct", "mean"),
                )
                .reset_index()
        )
        grouped.insert(0, "risk_factor", factor)
        grouped = grouped.rename(columns={factor: "factor_value"})
        rows.append(grouped)

    return pd.concat(rows, ignore_index=True)
