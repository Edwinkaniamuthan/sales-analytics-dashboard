import pandas as pd


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.file_path)
            return df
        except FileNotFoundError:
            raise Exception("CSV file not found. Check the path.")
        except Exception as e:
            raise Exception(f"Error loading data: {e}")
