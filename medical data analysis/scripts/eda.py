"""
Basic EDA script:
- prints info, head, describe
- outcome counts and means grouped by outcome
- saves a small text summary to reports/
"""

import os
import pandas as pd

def basic_info(df: pd.DataFrame):
    print("\n=== INFO ===")
    print(df.info())

def head_and_stats(df: pd.DataFrame):
    print("\n=== HEAD ===")
    print(df.head())
    print("\n=== DESCRIBE ===")
    print(df.describe())

def outcome_summary(df: pd.DataFrame):
    if "Outcome" in df.columns:
        print("\n=== Outcome Counts ===")
        print(df["Outcome"].value_counts())
        print("\n=== Mean values by Outcome ===")
        print(df.groupby("Outcome").mean())

def save_text_summary(df: pd.DataFrame, out_path="reports/summary.txt"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write("Basic EDA Summary\n\n")
        f.write("Shape: " + str(df.shape) + "\n\n")
        if "Outcome" in df.columns:
            f.write("Outcome counts:\n")
            f.write(df["Outcome"].value_counts().to_string() + "\n\n")
            f.write("Means by outcome:\n")
            f.write(df.groupby("Outcome").mean().to_string() + "\n")
    print(f"Saved text summary to {out_path}")

if __name__ == "__main__":
    df = pd.read_csv("data/diabetes_cleaned.csv")
    basic_info(df)
    head_and_stats(df)
    outcome_summary(df)
    save_text_summary(df)
