# Amazon A/B Testing & Statistical Analysis

End-to-end A/B testing workflow comparing two groups with a rigorous statistical pipeline — from assumption checks to the appropriate significance test — built as reusable, tested Python modules.

**Stack:** Python (Pandas, SciPy, Matplotlib) · pytest

---

## Overview

This project evaluates whether a change (variant B) produces a statistically significant difference versus the control (variant A). Rather than jumping straight to a t-test, the workflow first **checks the assumptions** (normality, equal variances) and then selects the correct test accordingly — the way A/B testing should be done in practice.

---

## Dataset

- **Source:** [add source — e.g. Kaggle / synthetic A/B test dataset]
- **Size:** [add rows × columns]
- **Groups compared:** Control (A) vs Variant (B)
- **Metric analysed:** [e.g. conversion rate / average order value / time on page]

---

## Methodology

The statistical decision pipeline:

1. **Normality check** — Shapiro-Wilk test on each group.
2. **Equal-variance check** — Levene's test.
3. **Significance test** — based on the assumption results:
   - If assumptions hold → parametric test (t-test).
   - If assumptions are violated → **Mann-Whitney U** (non-parametric).
4. **Interpretation** — p-value, effect direction, and a practical business conclusion.

This logic is implemented as reusable functions and covered by **unit tests** (`pytest`).

---

## Key Findings

The A/B test was a clear success for the new variant (**Group B**).

- **Conversion & Revenue:** Group B significantly increased both the conversion rate (p = 0.0045) and the total value spent (p = 0.0038) versus the control.
- **Basket size:** Users in Group B bought significantly more items per transaction (quantity, p = 0.0033).
- **Engagement:** Session duration remained statistically identical (p = 0.6460) — a positive signal, since the new variant drives more sales and larger baskets *without* requiring users to spend more time on the site.

**Recommendation:** Roll out the Group B variant to 100% of users.

---

## Repository Structure

```
Amazon_abtesting/
├── README.md
├── data/
├── notebooks/
├── src/
│   ├── data_cleaning.py
│   ├── eda.py
│   └── statistical_tests.py
├── tests/
│   └── test_statistical_tests.py
├── images/
└── requirements.txt
```

---

## How to Run

```bash
git clone https://github.com/FerminMargallo/Amazon_abtesting.git
cd Amazon_abtesting
pip install -r requirements.txt

# Run the analysis
jupyter notebook

# Run the unit tests
pytest
```

---

## Author

**Fermín Margallo** — Data Analyst
[GitHub](https://github.com/FerminMargallo) · [LinkedIn](https://www.linkedin.com/in/fermín-margallo-remón) · [Email](mailto:fmargalloremon@gmail.com)
