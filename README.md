# Periodontal Health Data Pipeline & Dashboard

A portfolio project combining dentistry domain knowledge with data analysis and data engineering.

The project builds an end-to-end workflow that:

1. ingests periodontal-health data from CSV;
2. validates and cleans patient-level records;
3. creates an analytical periodontal-status feature;
4. persists curated data to SQLite;
5. executes reusable SQL analysis;
6. generates summary datasets and charts;
7. exposes the results through an interactive Streamlit dashboard;
8. validates the pipeline with automated tests.

## Why this project

This repository demonstrates how clinical domain knowledge can be translated into a practical data product.

It is designed as a portfolio project for Data Analyst and Data Engineer opportunities.

## Tech stack

- Python
- pandas
- SQLite
- SQL
- Streamlit
- matplotlib
- pytest

## Skills demonstrated

### Data analysis
- exploratory data analysis
- aggregation
- risk-factor comparison
- clinical metric visualization
- dashboard design

### Data engineering
- ETL pipeline organization
- schema validation
- data cleaning
- transformation logic
- SQLite persistence
- reusable SQL queries
- modular Python project structure

### Software quality
- automated tests
- reusable functions
- dependency management
- reproducible execution
- GitHub-ready documentation

## Dataset

`data/periodontal_sample.csv` is a synthetic dataset created only for portfolio development.

No real patient information is included.

Core variables include:

- patient ID
- age
- sex
- smoking status
- diabetes status
- bleeding on probing
- mean probing depth
- mean clinical attachment loss

## Architecture

```text
CSV source
    |
    v
Data validation
    |
    v
Data cleaning
    |
    v
Feature engineering
    |
    +---------> CSV analytical outputs
    |
    +---------> SQLite database
    |
    +---------> SQL analysis
    |
    +---------> Streamlit dashboard
```

## Repository structure

```text
periodontal-health-portfolio/
├── data/
│   └── periodontal_sample.csv
├── notebooks/
├── outputs/
│   ├── figures/
│   ├── periodontal_cleaned.csv
│   ├── periodontal_summary.csv
│   ├── risk_factor_summary.csv
│   └── periodontal_health.db
├── sql/
│   └── analysis_queries.sql
├── src/
│   ├── analysis.py
│   ├── data_cleaning.py
│   ├── database.py
│   ├── etl.py
│   └── visualization.py
├── tests/
│   ├── test_analysis.py
│   ├── test_data_cleaning.py
│   ├── test_database.py
│   └── test_etl.py
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## Run the ETL pipeline

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

This produces:

- cleaned analytical data;
- summary tables;
- risk-factor tables;
- visualizations;
- a SQLite database.

## Run the dashboard

```bash
streamlit run app.py
```

The dashboard provides:

- periodontal-status filters;
- smoking and diabetes filters;
- patient count;
- average bleeding on probing;
- average probing depth;
- average clinical attachment loss;
- periodontal-status distribution;
- probing-depth vs attachment-loss visualization;
- risk-factor comparisons;
- filtered patient-level data.

## SQL

Reusable analysis queries are stored in:

```text
sql/analysis_queries.sql
```

Examples include:

- patients by periodontal status;
- clinical measurements by status;
- periodontal risk by smoking;
- periodontal risk by diabetes.

## Tests

Run:

```bash
pytest
```

Current tests cover:

- periodontal-status classification;
- duplicate removal;
- SQLite persistence;
- ETL output creation.

## Important clinical note

The periodontal-status rule in this repository is intentionally simplified for a programming and analytics portfolio.

It must not be used for diagnosis or clinical decision-making.

## Suggested GitHub description

> End-to-end periodontal health data project using Python, pandas, SQL, SQLite, Streamlit, ETL pipelines, visualization, and automated tests.

## Portfolio roadmap

Next planned milestones:

1. enrich the dataset and data dictionary;
2. add stronger SQL analytical queries;
3. add Power BI-compatible exports;
4. add CI testing with GitHub Actions;
5. containerize the project with Docker;
6. deploy the dashboard;
7. build a second healthcare data project;
8. expand toward production-style application projects.

## Continuous Integration

This repository includes a GitHub Actions workflow in `.github/workflows/tests.yml`.

Every push or pull request runs dependency installation, automated tests, and the ETL pipeline.

## Docker

Build the image:

```bash
docker build -t periodontal-health-dashboard .
```

Run the container:

```bash
docker run -p 8501:8501 periodontal-health-dashboard
```

Then open the Streamlit application at `http://localhost:8501`.

## Documentation

Additional documentation:
- `docs/data_dictionary.md`
- `docs/architecture.md`

## Recommended GitHub topics

`python`, `pandas`, `sql`, `sqlite`, `streamlit`, `data-analysis`, `data-engineering`, `healthcare-data`, `dentistry`, `etl`, `pytest`, `docker`

## Recommended next commit

```text
Add CI pipeline, Docker support and project documentation
```
