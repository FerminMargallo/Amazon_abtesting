# Amazon A/B Testing Analysis

This repository contains an end-to-end exploratory and statistical workflow for analyzing an Amazon-style A/B test experiment. It includes:

- data preparation utilities,
- exploratory data analysis (EDA) helpers,
- missing-value and outlier analysis tools,
- A/B test statistical checks,
- and Jupyter notebooks that show the full analysis flow.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Tech Stack](#tech-stack)
4. [Setup Instructions](#setup-instructions)
5. [Data Files](#data-files)
6. [How to Run the Analysis](#how-to-run-the-analysis)
7. [Module-by-Module API Reference](#module-by-module-api-reference)
8. [Testing](#testing)
9. [Typical Workflow](#typical-workflow)
10. [Known Limitations and Notes](#known-limitations-and-notes)
11. [Contributing](#contributing)

---

## Project Overview

This repository was developed as part of a **data analytics bootcamp** project focused on applying real-world data cleaning, exploratory analysis, and hypothesis testing workflows in Python.

The project is designed to support practical A/B testing analysis with Python.

It provides utility functions to:

- standardize and clean tabular data,
- perform a baseline EDA,
- visualize and diagnose numerical/categorical distributions,
- detect outliers,
- impute missing values,
- and run common A/B statistical checks (normality, homoscedasticity, Mann–Whitney U).

The notebooks in `notebooks/` illustrate how these pieces connect in a real workflow.

---

## Repository Structure

```text
Amazon_abtesting/
├── data/
│   ├── data_raw.csv
│   ├── data_cleaned.csv
│   └── data_processed.csv
├── notebooks/
│   ├── 01.baseline_eda.ipynb
│   ├── 02.cleaning_data.ipynb
│   ├── 03.null_values.ipynb
│   └── 04.ab_testing.ipynb
├── src/
│   ├── abtest.py
│   ├── data_cleaning_utils.py
│   ├── eda_utils.py
│   └── null_values.py
├── tests/
│   └── test_functions.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

Core libraries used by this project include:

- `pandas` for data manipulation,
- `numpy` for numerical operations,
- `matplotlib` and `seaborn` for visualization,
- `scipy` for statistical tests,
- `scikit-learn` for imputation (`KNNImputer`, `IterativeImputer`),
- `pytest` for automated tests,
- Jupyter ecosystem for notebook-based analysis.

---

## Setup Instructions

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd Amazon_abtesting
```

### 2) Create and activate a virtual environment

**macOS/Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run tests

```bash
pytest -q
```

---

## Data Files

The `data/` directory includes multiple dataset stages:

- `data_raw.csv`: raw input data,
- `data_cleaned.csv`: post-cleaning version,
- `data_processed.csv`: prepared data for downstream modeling/testing.

> Tip: Keep raw files immutable and only modify cleaned/processed artifacts.

---

## How to Run the Analysis

Open notebooks in order to follow the full analytical storyline:

1. `notebooks/01.baseline_eda.ipynb` — initial exploration,
2. `notebooks/02.cleaning_data.ipynb` — cleaning and formatting,
3. `notebooks/03.null_values.ipynb` — missing-value strategy,
4. `notebooks/04.ab_testing.ipynb` — statistical A/B testing.

Launch Jupyter Lab/Notebook:

```bash
jupyter lab
```

(or `jupyter notebook` if preferred)

---

## Module-by-Module API Reference

### `src/data_cleaning_utils.py`

#### `lowercase_strings(df)`
Converts all object-type column values to lowercase (in-place).

#### `convert_commas_to_dots(df)`
For object columns:
- replaces decimal commas with dots,
- attempts conversion to `float64`.

Columns that cannot be cast remain as text.

#### `replace_spaces_with_underscores(df)`
Replaces spaces with underscores in object-type column values.

---

### `src/eda_utils.py`

#### `baseline_eda(df)`
Prints/displays:
- random sample,
- shape,
- `info()`,
- missing-value percentage,
- duplicate count,
- categorical value counts,
- numerical summary statistics.

---

### `src/null_values.py`

#### `subplot_col_cat(df)`
Creates countplots for categorical columns.

#### `subplot_col_num(df)`
Creates histogram + boxplot pairs for numerical columns.

#### `calculate_outliers(df, cols)`
Computes and prints outlier counts and percentages using IQR bounds.

#### `impute_iterative(df, col_list)`
Imputes selected columns with `IterativeImputer` and appends `*_iterative` columns.

#### `impute_knn(df, col_list)`
Imputes selected columns with `KNNImputer` and appends `*_knn` columns.

---

### `src/abtest.py`

#### `explore_ab_groups(df, group_col)`
Shows descriptive statistics split by A/B test group.

#### `check_normality(df, metric_cols)`
Runs Shapiro–Wilk normality test by metric.

#### `check_homoscedasticity(df, group_col, metric_cols)`
Runs Levene’s test to compare group variances.

#### `perform_mann_whitney(df, group_col, metric_cols)`
Runs the Mann–Whitney U test for two independent groups.

---

## Testing

Tests are located in `tests/test_functions.py` and currently cover:

- outlier detection behavior,
- empty-data edge handling for outliers,
- normality test output sanity.

Run tests:

```bash
pytest -q
```

---

## Typical Workflow

A practical analysis sequence for this repository:

1. Load raw data (`data/data_raw.csv`).
2. Apply text/format cleaning utilities from `src/data_cleaning_utils.py`.
3. Run `baseline_eda()` from `src/eda_utils.py`.
4. Analyze distributions and outliers with `src/null_values.py` helpers.
5. Handle nulls using iterative or KNN imputation.
6. Run A/B statistical checks from `src/abtest.py`.
7. Record results and business conclusions in notebooks/reports.

---

## Known Limitations and Notes

- This is a **bootcamp learning project**, so the code prioritizes clarity and educational readability over production hardening.
- Several utility functions are designed for notebook usage and print results instead of returning structured outputs.
- Some plotting/statistical helpers assume expected input schema and valid numeric columns.
- `perform_mann_whitney` expects exactly two groups in the specified group column.
- The repository currently uses a broad `requirements.txt` environment (includes Jupyter ecosystem packages); you may optionally slim this for production pipelines.

---

## Contributing

1. Create a feature branch.
2. Implement changes with clear, focused commits.
3. Run tests locally before opening a PR.
4. Add/update tests when adding functionality.
5. Update this README when behavior or APIs change.

---

If useful, future improvements could include:

- stronger type validation and explicit exceptions,
- return-value-oriented APIs (in addition to notebook prints),
- CI integration for automated linting/tests,
- and richer statistical reporting objects.

