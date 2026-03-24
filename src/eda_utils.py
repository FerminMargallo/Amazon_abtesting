import pandas as pd
from IPython.display import display

def baseline_eda(df: pd.DataFrame) -> None:
    """
    Performs a preliminary exploratory data analysis on a given DataFrame.

    This analysis includes:
    - A random sample of 5 rows from the DataFrame.
    - General DataFrame information (data types, non-null counts, etc.).
    - Percentage of missing values per column.
    - Count of duplicated rows.
    - Value distributions for categorical columns.
    - Summary statistics for numerical columns.

    Parameters:
        df (pd.DataFrame): The DataFrame to analyze.

    Returns:
        None
    """

def baseline_eda(df):
  print('--- RANDOM SAMPLE ---')
  display(df.sample(5))

  print('\n--- DIMENSIONS ---')
  print(f'Our dataset has {df.shape[0]} rows and {df.shape[1]} columns.')

  print('\n--- INFO ---')
  df.info() 

  print('\n--- MISSING VALUES (%) ---')
  display(round(df.isnull().mean() * 100, 2))

  print('\n--- DUPLICATES ---')
  print(f'Total duplicated rows: {df.duplicated().sum()}')

  print('\n--- CATEGORICAL VALUE COUNTS ---')
    # Included 'category' alongside 'object' just in case you optimize data types later
  for col in df.select_dtypes(include=['object', 'category']).columns:
      print(f"\n{col.upper()}:")
      print(df[col].value_counts(dropna=False))
      print('-----------')

  print('\n--- NUMERICAL STATISTICS ---')
  display(df.describe().T)