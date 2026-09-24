from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def save_status_chart(df: pd.DataFrame, output_path: str) -> None:
    counts = df["periodontal_status"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Periodontal Status Distribution")
    ax.set_xlabel("Status")
    ax.set_ylabel("Number of Patients")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=150)
    plt.close(fig)

def save_risk_scatter(df: pd.DataFrame, output_path: str) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(
        df["probing_depth_mm_mean"],
        df["clinical_attachment_loss_mm_mean"],
        alpha=0.75,
    )
    ax.set_title("Probing Depth vs Clinical Attachment Loss")
    ax.set_xlabel("Mean Probing Depth (mm)")
    ax.set_ylabel("Mean Clinical Attachment Loss (mm)")
    fig.tight_layout()

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
