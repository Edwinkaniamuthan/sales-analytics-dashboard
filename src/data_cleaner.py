import pandas as pd


class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def clean_data(self) -> pd.DataFrame:
        self.df.columns = self.df.columns.str.strip()
        self.df = self.df.drop_duplicates()

        numeric_cols = ["Sales", "Profit", "Quantity", "Discount"]
        for col in numeric_cols:
            if col in self.df.columns:
                self.df = self.df.dropna(subset=[col])

        return self.df
