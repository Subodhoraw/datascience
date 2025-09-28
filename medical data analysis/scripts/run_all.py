"""
Simple pipeline to run preprocessing -> EDA -> Visualizations
Run: python scripts/run_all.py
"""

from scripts import data_preprocessing as dp
from scripts import eda as ed
from scripts import visualization as viz
import pandas as pd

if __name__ == "__main__":
    # Preprocess
    df = dp.load_data("data/diabetes.csv")
    df = dp.replace_zeros_with_na(df)
    df = dp.impute_median(df)
    dp.save_cleaned(df, "data/diabetes_cleaned.csv")

    # EDA
    df_clean = pd.read_csv("data/diabetes_cleaned.csv")
    ed.basic_info(df_clean)
    ed.head_and_stats(df_clean)
    ed.outcome_summary(df_clean)
    ed.save_text_summary(df_clean)

    # Visualization
    viz.plot_histograms(df_clean)
    viz.plot_boxplots_by_outcome(df_clean)
    viz.plot_correlation(df_clean)

    print("\nAll done. Check reports/graphs and reports/summary.txt")
