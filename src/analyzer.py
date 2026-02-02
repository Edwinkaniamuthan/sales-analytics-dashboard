import pandas as pd
import numpy as np


class SalesAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_kpis(self) -> dict:
        return {
            "total_sales": np.round(self.df["Sales"].sum(), 2),
            "total_profit": np.round(self.df["Profit"].sum(), 2),
            "total_orders": len(self.df),
            "avg_discount": np.round(self.df["Discount"].mean(), 2)
        }

    def sales_by_category(self) -> pd.DataFrame:
        return (
            self.df
            .groupby("Category")["Sales"]
            .sum()
            .reset_index()
            .sort_values(by="Sales", ascending=False)
        )

    def sales_by_region(self) -> pd.DataFrame:
        return (
            self.df
            .groupby("Region")["Sales"]
            .sum()
            .reset_index()
            .sort_values(by="Sales", ascending=False)
        )

    def top_profitable_subcategories(self, n=10):
        return (
            self.df
            .groupby("Sub-Category")["Profit"]
            .sum()
            .reset_index()
            .sort_values(by="Profit", ascending=False)
            .head(n)
        )
