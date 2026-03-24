import pandas as pd
import scipy.stats as stats
from IPython.display import display

def explore_ab_groups(df: pd.DataFrame, group_col: str) -> None:
    """
    Displays descriptive statistics for categorical and numerical columns, 
    separated by the A/B test groups.
    """
    for category in df[group_col].unique():
        df_filtered = df[df[group_col] == category]
        
        print(f"--- GROUP: {category.upper()} ---")
        print("Categorical Columns Statistics:")
        display(df_filtered.describe(include=['object', 'category']).T)
        
        print("Numerical Columns Statistics:")
        display(df_filtered.describe(include='number').T)
        print('-' * 40)


def check_normality(df: pd.DataFrame, metric_cols: list) -> None:
    """
    Performs the Shapiro-Wilk test to check if the data follows a normal distribution.
    Null Hypothesis (H0): The data is normally distributed.
    """
    print("--- SHAPIRO-WILK NORMALITY TEST ---")
    for metric in metric_cols:
        # Drop NaNs to avoid errors in the statistical test
        clean_data = df[metric].dropna() 
        statistic,p_value = stats.shapiro(clean_data)
        
        if p_value > 0.05:
            print(f" {metric.upper()}: p-value={p_value:.4f} -> Data follows a NORMAL distribution.")
        else:
            print(f" {metric.upper()}: p-value={p_value:.4f} -> Data DOES NOT follow a normal distribution.")


def check_homoscedasticity(df: pd.DataFrame, group_col: str, metric_cols: list) -> None:
    """
    Performs Levene's test to check for equal variances across groups (Homoscedasticity).
    Null Hypothesis (H0): All input samples are from populations with equal variances.
    """
    print("\n--- LEVENE'S HOMOSCEDASTICITY TEST ---")
    for metric in metric_cols:
        groups_data = []
        for value in df[group_col].unique():
            # Extract clean metric data for each group
            groups_data.append(df[df[group_col] == value][metric].dropna())
            
        # Unpack the list of arrays into the levene function
        statistic, p_value = stats.levene(*groups_data)
        
        if p_value > 0.05:
            print(f"{metric.upper()}: p-value={p_value:.4f} -> Variances are homogeneous (HOMOSCEDASTICITY met).")
        else:
            print(f"{metric.upper()}: p-value={p_value:.4f} -> Variances are NOT homogeneous (HETEROSCEDASTICITY).")


def perform_mann_whitney(df: pd.DataFrame, group_col: str, metric_cols: list) -> None:
    """
    Performs the Mann-Whitney U test (non-parametric) to determine if there are 
    significant differences between two independent groups.
    """
    print("\n--- MANN-WHITNEY U TEST (Non-Parametric) ---")
    
    unique_groups = df[group_col].dropna().unique()
    if len(unique_groups) != 2:
        print("Error: The control column must have exactly 2 distinct groups.")
        return

    for metric in metric_cols:
        # Separate data by group
        group_a = df[df[group_col] == unique_groups[0]][metric].dropna()
        group_b = df[df[group_col] == unique_groups[1]][metric].dropna()
        
        statistic, p_value = stats.mannwhitneyu(group_a, group_b)
        
        print(f"Testing metric: {metric.upper()} between {unique_groups[0]} and {unique_groups[1]}")
        if p_value > 0.05:
            print(f" Result (p={p_value:.4f}): NO significant differences between the groups.")
        else:
            print(f" Result (p={p_value:.4f}): SIGNIFICANT DIFFERENCES EXIST between the groups!")
        print("-" * 30)