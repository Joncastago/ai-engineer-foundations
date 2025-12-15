import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def basic_info(df: pd.DataFrame) -> dict:
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().to_dict()
    }

if __name__ == "__main__":
    print("Data Explorer ready")
Add initial data explorer script
