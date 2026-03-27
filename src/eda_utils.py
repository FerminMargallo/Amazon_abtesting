import pandas as pd
from IPython.display import display

def baseline_eda(df: pd.DataFrame) -> None:
  """
    Performs a comprehensive baseline Exploratory Data Analysis (EDA) on a DataFrame.

    This function generates a quick overview of the dataset by displaying a random
    sample, structural dimensions, data types, missing value percentages, duplicate
    row counts, categorical value distributions, and summary statistics for
    numerical columns.

    Args:
        df (pandas.DataFrame): The input DataFrame to be analyzed.

    Returns:
        None: The function prints and displays the EDA results directly.
    """
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
   
  for col in df.select_dtypes(include=['object', 'category']).columns:
      print(f"\n{col.upper()}:")
      print(df[col].value_counts(dropna=False))
      print('-----------')

  print('\n--- NUMERICAL STATISTICS ---')
  display(df.describe().T)