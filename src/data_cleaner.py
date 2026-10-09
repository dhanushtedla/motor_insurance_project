import pandas as pd
import os
from src.logger import setup_logger

logger = setup_logger("data_cleaner")

def clean_data(data_dict):
    cleaned_data = {}
    for name, df in data_dict.items():
        df_clean = df.drop_duplicates().copy()
        cleaned_data[name] = df_clean
        logger.info(f"Cleaned {name}: Removed duplicates, final shape {df_clean.shape}")
    return cleaned_data

def save_cleaned_data(cleaned_dict, output_dir="data/cleaned"):
    os.makedirs(output_dir, exist_ok=True)
    for name, df in cleaned_dict.items():
        file_path = os.path.join(output_dir, f"{name}_cleaned.csv")
        df.to_csv(file_path, index=False)
        logger.info(f"Saved {name}_cleaned.csv to {output_dir}")
