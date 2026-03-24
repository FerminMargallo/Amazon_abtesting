import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.experimental import enable_iterative_imputer 
from sklearn.impute import KNNImputer, IterativeImputer


def subplot_col_cat(df: pd.DataFrame) -> None:
  """
    Generates countplots for all categorical columns in the DataFrame.
    """
  # Select categorical columns
  categorical_cols=df.select_dtypes(include=['object','category']).columns
  if len(categorical_cols) == 0:
    return "No categorical columns found in the DataFrame."
  # Configure figure size
  num_cols=len(categorical_cols)
  rows=(num_cols+2)//3 # Calculate necessary rows for a 3-column layout
  fig,axes=plt.subplots(rows,3,figsize=(15,rows*5))
  axes=axes.flatten() # Flatten axes to a 1D array for easier iteration

  # Generate plots for each categorical column
  for i,col in enumerate(categorical_cols):
    sns.countplot(data=df, x=col,ax=axes[i],hue=col,palette="tab10",legend=False)
    axes[i].set_title(f'Distribution of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Frequency')
    axes[i].tick_params(axis='x',rotation=90) # Rotate x-axis labels if necessary

  # Remove extra empty axes if there are fewer columns than subplots
  for j in range(i+1,len(axes)):
    fig.delaxes(axes[j])

  #Adjust layout
  plt.tight_layout()
  plt.show()

def subplot_col_num(df: pd.DataFrame) -> None:
  """
    Generates a histogram and a boxplot side-by-side for all numerical columns.
    """
  # Select numerical columns
  col_num=df.select_dtypes(include='number').columns
  num_graph=len(col_num)

  num_rows=(num_graph+2)//2 # Calculate necessary rows for a 2-column layout
  fig,axes=plt.subplots(num_graph,2,figsize=(15,num_rows*5))

  # Generate plots for each categorical column
  for i,col in enumerate(col_num):
    sns.histplot(data=df, x=col,ax=axes[i,0],bins=200)
    axes[i,0].set_title(f'Distribution of {col}')
    axes[i,0].set_xlabel(col)
    axes[i,0].set_ylabel('Frequency')

    sns.boxplot(data=df, x=col,ax=axes[i,1])
    axes[i,1].set_title(f'Boxplot of {col}')

  # Drop remaining empty axes if there are fewer columns than subplots
  for j in range(i+1,len(axes)):
    fig.delaxes(axes[j])

  # Tight layout
  plt.tight_layout()
  plt.show()

def calculate_outliers(df: pd.DataFrame, cols: list) -> None:
    """
    Calculates and prints the number and percentage of outliers in specified 
    numeric columns using the IQR method.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        cols (list): A list of numerical column names to analyze for outliers.

    Returns:
        None
    """
    for col in cols:
        # 1. Calculate Q1, Q3, and IQR (Interquartile Range)
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1  # Using standard acronym IQR

        # 2. Define upper and lower limits for outliers
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        # 3. Filter DataFrame to find outliers
        outliers_df = df[(df[col] < lower_limit) | (df[col] > upper_limit)]

        # 4. Calculate total number and percentage of outliers
        num_outliers = outliers_df.shape[0]
        total_rows = df.shape[0]
        
        # check if total_rows is zero to avoid division error
        if total_rows > 0:
            per_outliers = (num_outliers / total_rows) * 100
        else:
            per_outliers = 0

        print(f'In the column {col.upper()} we have a total of {num_outliers} outliers, representing {round(per_outliers, 2)} % of the total')


def impute_iterative(df: pd.DataFrame, col_list: list):
    """
    Imputes missing values using Multivariate Iterative Imputation.
    Creates new columns with the suffix '_iterative'.
    """
    iter_imputer = IterativeImputer(max_iter=50, random_state=42)
    data_imputed = iter_imputer.fit_transform(df[col_list])
    new_col = [col + "_iterative" for col in col_list]
    df[new_col] = data_imputed
    return df 

def impute_knn(df: pd.DataFrame, col_list: list):
    """
    Imputes missing values using the K-Nearest Neighbors approach.
    Creates new columns with the suffix '_knn'.
    """
    knn_imputer = KNNImputer(n_neighbors=5)
    data_imputed = knn_imputer.fit_transform(df[col_list])
    new_col = [col + "_knn" for col in col_list]
    df[new_col] = data_imputed
    return df