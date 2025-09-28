"""
Data Preprocessing Script
- Load dataset
- Replace known zero-values (where zeros mean missing)
- Impute median for those columns
- Save cleaned dataset
"""

import os
import pandas as pd

MISSING_ZERO_COLS = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded data: {df.shape}")
    return df

def replace_zeros_with_na(df: pd.DataFrame, cols=None) -> pd.DataFrame:
    if cols is None:
        cols = MISSING_ZERO_COLS
    for c in cols:
        if c in df.columns:
            df[c] = df[c].replace(0, pd.NA)
    return df

def impute_median(df: pd.DataFrame, cols=None) -> pd.DataFrame:
    if cols is None:
        cols = MISSING_ZERO_COLS
    for c in cols:
        if c in df.columns:
            median = df[c].median(skipna=True)
            df[c] = df[c].fillna(median)
            print(f"Imputed {c} with median = {median}")
    return df

def save_cleaned(df: pd.DataFrame, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Saved cleaned data to {out_path}")

if __name__ == "__main__":
    path = "data/diabetes.csv"
    out = "data/diabetes_cleaned.csv"

    df = load_data(path)
    print("\nMissing before replacement:\n", df.isnull().sum())
    df = replace_zeros_with_na(df)
    print("\nMissing after zero->NA replacement:\n", df.isnull().sum())
    df = impute_median(df)
    print("\nMissing after imputation:\n", df.isnull().sum())
    save_cleaned(df, out)
