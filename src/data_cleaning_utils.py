import pandas as pd

def lowercase_strings(df: pd.DataFrame) -> None:
    """
    Converts all string values to lowercase for object-type columns.

    For each text (object) column, it transforms the strings to lowercase,
    standardizing the data and preventing case-sensitivity issues during comparisons.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the columns to process.

    Returns:
        None: The DataFrame is modified in-place.
    """
    for col in df.select_dtypes(include='O').columns:
        df[col] = df[col].str.lower()


def convert_commas_to_dots(df: pd.DataFrame) -> None:
    """
    Replaces commas with dots in text columns and attempts to cast them to numeric.

    For each object-type column, it replaces commas (',') with dots ('.') to 
    standardize decimal separators. It then attempts to cast the column to float64. 
    If the conversion fails, the column remains as text.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the columns to process.

    Returns:
        None: The DataFrame is modified in-place.
    """
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace(',', '.', regex=False)
        try:
            df[col] = df[col].astype('float64')
        except ValueError:
            pass


def replace_spaces_with_underscores(df: pd.DataFrame) -> None:
    """
    Replaces spaces with underscores in the values of all text-type columns.

    For each object-type column, it replaces blank spaces (' ') with 
    underscores ('_'), facilitating easier data handling.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the columns to process.

    Returns:
        None: The DataFrame is modified in-place.
    """
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace(' ', '_', regex=False)