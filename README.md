# Amazon A/B Testing Analysis

An end-to-end analysis of an e-commerce A/B test that compares a control experience (Group A) with a new website variant (Group B). The project covers exploratory analysis, data cleaning, missing-value treatment, and statistical testing through reusable Python utilities and Jupyter notebooks.

## Project Overview

The analysis investigates whether the two groups differ across four customer and business metrics:

- Conversion
- Total value
- Session duration
- Quantity purchased

The supplied dataset contains 2,000 user records and 21 original columns, including user, product, purchase, device, and session attributes. All datasets required to reproduce the work are included in the repository.

## Key Results

The final notebook uses two-sided Mann–Whitney U tests with a 5% significance level. Group B has higher observed averages for conversion, total value, and quantity purchased; these differences are statistically significant. Session duration does not differ significantly between the groups.

| Metric | Group A mean | Group B mean | p-value | Result |
| --- | ---: | ---: | ---: | --- |
| Conversion | 10.23% | 14.41% | 0.0045 | Statistically significant difference |
| Total value | 41.64 | 61.61 | 0.0038 | Statistically significant difference |
| Quantity | 0.29 | 0.45 | 0.0033 | Statistically significant difference |
| Session duration | 15.72 | 15.55 | 0.6460 | No statistically significant difference |

These results provide evidence in favor of Group B for the measured outcomes. Before a production rollout, the finding should be considered alongside effect size, implementation cost, guardrail metrics, and the experiment's business context.

## Methodology

1. **Exploratory data analysis** examines the dataset's structure, data types, missing values, duplicates, distributions, and summary statistics.
2. **Data cleaning** standardizes text, column names, decimal separators, and conversion labels.
3. **Missing-value treatment** identifies outliers and applies iterative and K-nearest-neighbors imputation where appropriate.
4. **Assumption checks** use Shapiro–Wilk tests for normality and Levene's test for equal variances.
5. **Hypothesis testing** uses the Mann–Whitney U test because the selected metrics do not satisfy the normality assumption.

For each metric, the null hypothesis states that there is no difference between Group A and Group B. A p-value below 0.05 is treated as evidence against that hypothesis.

## Repository Structure

```text
Amazon_abtesting/
├── data/
│   ├── data_raw.csv          # Original dataset
│   ├── data_cleaned.csv      # Cleaned dataset
│   └── data_processed.csv    # Dataset used for the A/B test
├── notebooks/
│   ├── 01.baseline_eda.ipynb
│   ├── 02.cleaning_data.ipynb
│   ├── 03.null_values.ipynb
│   └── 04.ab_testing.ipynb
├── src/
│   ├── abtest.py             # Group exploration and statistical-test helpers
│   ├── data_cleaning_utils.py
│   ├── eda_utils.py
│   └── null_values.py
├── tests/
│   └── test_functions.py
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3
- `pip`

### Installation

```bash
git clone https://github.com/FerminMargallo/Amazon_abtesting.git
cd Amazon_abtesting

# Optional: create and activate a virtual environment
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Reproduce the Analysis

Start Jupyter from the repository root:

```bash
jupyter notebook
```

Run the notebooks in order:

1. `01.baseline_eda.ipynb`
2. `02.cleaning_data.ipynb`
3. `03.null_values.ipynb`
4. `04.ab_testing.ipynb`

### Run the Tests

```bash
python -m pytest -q
```

## Tools

- Python
- pandas and NumPy
- SciPy
- scikit-learn
- Matplotlib and seaborn
- Jupyter Notebook
- pytest

## Author

Fermín Margallo — Data Analyst

[GitHub](https://github.com/FerminMargallo) · [LinkedIn](https://www.linkedin.com/in/fermín-margallo-remón) · [Email](mailto:fmargalloremon@gmail.com)

