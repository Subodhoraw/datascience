"""
Visualization script:
- saves histograms, boxplots, and a correlation heatmap to reports/graphs/
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def plot_histograms(df: pd.DataFrame, out_dir="reports/graphs"):
    ensure_dir(out_dir)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    for c in numeric_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(df[c].dropna(), kde=True)
        plt.title(f"{c} distribution")
        filename = f"{out_dir}/{c}_hist.png"
        plt.savefig(filename, bbox_inches="tight")
        plt.close()
        print(f"Saved {filename}")

def plot_boxplots_by_outcome(df: pd.DataFrame, out_dir="reports/graphs"):
    ensure_dir(out_dir)
    if "Outcome" not in df.columns:
        return
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    for c in numeric_cols:
        if c == "Outcome": continue
        plt.figure(figsize=(6,4))
        sns.boxplot(x="Outcome", y=c, data=df)
        plt.title(f"{c} by Outcome")
        filename = f"{out_dir}/{c}_box_by_outcome.png"
        plt.savefig(filename, bbox_inches="tight")
        plt.close()
        print(f"Saved {filename}")

def plot_correlation(df: pd.DataFrame, out_dir="reports/graphs"):
    ensure_dir(out_dir)
    plt.figure(figsize=(10,8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f")
    plt.title("Correlation heatmap")
    filename = f"{out_dir}/correlation_heatmap.png"
    plt.savefig(filename, bbox_inches="tight")
    plt.close()
    print(f"Saved {filename}")

if __name__ == "__main__":
    df = pd.read_csv("data/diabetes_cleaned.csv")
    plot_histograms(df)
    plot_boxplots_by_outcome(df)
    plot_correlation(df)
