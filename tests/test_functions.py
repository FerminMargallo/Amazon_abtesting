import pandas as pd
import numpy as np
import pytest

# 1. Import your actual modules
from src.null_values import calculate_outliers
from src.abtest import check_normality

# --- TEST 1: Outlier Detection (IQR) ---
def test_calculate_outliers(capsys):
    """Tests that the IQR method detects an obvious outlier and calculates the %."""
    df = pd.DataFrame({"revenue": [10, 12, 14, 16, 100]})
    calculate_outliers(df, ["revenue"])
    
    captured = capsys.readouterr()
    assert "total of 1 outliers" in captured.out
    assert "20.0 %" in captured.out


# --- TEST 2: Empty DataFrame Handling (Edge Case) ---
def test_calculate_outliers_empty(capsys):
    """Tests that the function handles an empty DataFrame without errors."""
    df_empty = pd.DataFrame({"revenue": []})
    calculate_outliers(df_empty, ["revenue"])
    
    captured = capsys.readouterr()
    assert "total of 0 outliers" in captured.out
    assert "0 %" in captured.out


# --- TEST 3: Statistical Engine (Normality Test) ---
def test_check_normality(capsys):
    """Tests that the function correctly identifies a normal distribution."""
    # Setup: We generate mathematically normal data using numpy
    np.random.seed(42)
    df_normal = pd.DataFrame({
        "metric": np.random.normal(loc=50, scale=5, size=100)
    })
    
    # Execution
    check_normality(df_normal, ["metric"])
    
    captured = capsys.readouterr()
    
    # Assert: Check that the printed text confirms normality
    # IMPORTANT: Adjust "DOES NOT" based on what your actual function prints!
    assert "Data does not follow a normal distribution" not in captured.out