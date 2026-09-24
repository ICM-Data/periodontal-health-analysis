import pandas as pd
import streamlit as st

from src.data_cleaning import load_data, clean_data
from src.analysis import assign_periodontal_status

st.set_page_config(
    page_title="Periodontal Health Dashboard",
    page_icon="🦷",
    layout="wide",
)

@st.cache_data
def load_dashboard_data():
    df = load_data("data/periodontal_sample.csv")
    df = clean_data(df)
    return assign_periodontal_status(df)

df = load_dashboard_data()

st.title("Periodontal Health Dashboard")
st.caption(
    "Portfolio demo using synthetic data. "
    "The classifications are simplified and are not intended for clinical diagnosis."
)

st.sidebar.header("Filters")

status_options = sorted(df["periodontal_status"].unique().tolist())
selected_status = st.sidebar.multiselect(
    "Periodontal status",
    options=status_options,
    default=status_options,
)

smoker_filter = st.sidebar.selectbox(
    "Smoking status",
    options=["All", "Non-smoker", "Smoker"],
)

diabetes_filter = st.sidebar.selectbox(
    "Diabetes status",
    options=["All", "No diabetes", "Diabetes"],
)

filtered = df[df["periodontal_status"].isin(selected_status)].copy()

if smoker_filter == "Non-smoker":
    filtered = filtered[filtered["smoker"] == 0]
elif smoker_filter == "Smoker":
    filtered = filtered[filtered["smoker"] == 1]

if diabetes_filter == "No diabetes":
    filtered = filtered[filtered["diabetes"] == 0]
elif diabetes_filter == "Diabetes":
    filtered = filtered[filtered["diabetes"] == 1]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Patients", len(filtered))
col2.metric(
    "Mean bleeding on probing",
    f"{filtered['bleeding_on_probing_pct'].mean():.1f}%"
    if len(filtered) else "—",
)
col3.metric(
    "Mean probing depth",
    f"{filtered['probing_depth_mm_mean'].mean():.2f} mm"
    if len(filtered) else "—",
)
col4.metric(
    "Mean attachment loss",
    f"{filtered['clinical_attachment_loss_mm_mean'].mean():.2f} mm"
    if len(filtered) else "—",
)

st.subheader("Periodontal status distribution")
status_counts = (
    filtered["periodontal_status"]
    .value_counts()
    .rename_axis("Periodontal status")
    .reset_index(name="Patients")
)
st.bar_chart(status_counts.set_index("Periodontal status"))

st.subheader("Clinical relationship")
scatter_df = filtered[
    [
        "probing_depth_mm_mean",
        "clinical_attachment_loss_mm_mean",
    ]
].rename(
    columns={
        "probing_depth_mm_mean": "Mean probing depth (mm)",
        "clinical_attachment_loss_mm_mean": "Mean attachment loss (mm)",
    }
)
st.scatter_chart(
    scatter_df,
    x="Mean probing depth (mm)",
    y="Mean attachment loss (mm)",
)

st.subheader("Risk factor comparison")
risk_view = filtered.copy()
risk_view["Smoking"] = risk_view["smoker"].map({0: "No", 1: "Yes"})
risk_view["Diabetes"] = risk_view["diabetes"].map({0: "No", 1: "Yes"})

risk_summary = pd.DataFrame(
    {
        "Group": [
            "Non-smokers",
            "Smokers",
            "No diabetes",
            "Diabetes",
        ],
        "Mean BOP (%)": [
            risk_view.loc[risk_view["smoker"] == 0, "bleeding_on_probing_pct"].mean(),
            risk_view.loc[risk_view["smoker"] == 1, "bleeding_on_probing_pct"].mean(),
            risk_view.loc[risk_view["diabetes"] == 0, "bleeding_on_probing_pct"].mean(),
            risk_view.loc[risk_view["diabetes"] == 1, "bleeding_on_probing_pct"].mean(),
        ],
    }
).dropna()

st.dataframe(risk_summary, use_container_width=True, hide_index=True)

st.subheader("Filtered patient-level data")
st.dataframe(filtered, use_container_width=True, hide_index=True)
