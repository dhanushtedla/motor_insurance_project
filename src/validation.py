import pandas as pd
from src.logger import setup_logger

logger = setup_logger("validation")

def validate_raw_data(data_dict):
    validation_results = {}
    for name, df in data_dict.items():
        null_counts = df.isnull().sum().to_dict()
        duplicate_count = int(df.duplicated().sum())
        validation_results[name] = {
            "shape": df.shape,
            "null_values": null_counts,
            "duplicates": duplicate_count
        }
        logger.info(f"Validation for {name}: Shape={df.shape}, Duplicates={duplicate_count}")
    return validation_results
