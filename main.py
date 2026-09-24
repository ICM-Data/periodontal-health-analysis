from pathlib import Path

from src.etl import run_etl
from src.analysis import create_summary, risk_factor_summary
from src.visualization import save_status_chart, save_risk_scatter

DATA_PATH = "data/periodontal_sample.csv"
OUTPUT_DIR = Path("outputs")
DATABASE_PATH = OUTPUT_DIR / "periodontal_health.db"

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    df = run_etl(
        source_csv=DATA_PATH,
        output_csv=OUTPUT_DIR / "periodontal_cleaned.csv",
        db_path=DATABASE_PATH,
    )

    summary = create_summary(df)
    risk_summary = risk_factor_summary(df)

    summary.to_csv(OUTPUT_DIR / "periodontal_summary.csv", index=False)
    risk_summary.to_csv(OUTPUT_DIR / "risk_factor_summary.csv", index=False)

    save_status_chart(df, OUTPUT_DIR / "figures" / "status_distribution.png")
    save_risk_scatter(df, OUTPUT_DIR / "figures" / "probing_depth_vs_attachment_loss.png")

    print("\nPeriodontal Health Portfolio Project")
    print("-" * 38)
    print(f"Patients analyzed: {len(df)}")
    print(f"SQLite database: {DATABASE_PATH}")
    print("\nStatus summary:")
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
