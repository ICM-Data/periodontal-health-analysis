# Project Architecture

## Data flow

```text
Synthetic CSV
     |
     v
Validation + Cleaning
     |
     v
Feature Engineering
     |
     +----------> Cleaned CSV
     |
     +----------> SQLite Database
     |
     +----------> SQL Analysis
     |
     +----------> Static Charts
     |
     +----------> Streamlit Dashboard
```

## Components
- `src/data_cleaning.py`: schema validation, type conversion, duplicate removal, invalid-value filtering.
- `src/analysis.py`: feature engineering and analytical summaries.
- `src/database.py`: SQLite persistence and reusable query execution.
- `src/etl.py`: orchestration of the ETL workflow.
- `src/visualization.py`: static portfolio visualizations.
- `app.py`: interactive Streamlit dashboard.
- `tests/`: automated checks for cleaning, classification, persistence, and ETL.
- `.github/workflows/tests.yml`: continuous integration.
- `Dockerfile`: reproducible containerized application.
