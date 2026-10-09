import pandas as pd
import os
from src.logger import setup_logger

logger = setup_logger("data_loader")

def load_raw_data(data_dir="data/raw"):
    tables = ["customers", "policies", "vehicles", "claims", "payments"]
    data = {}
    for table in tables:
        file_path = os.path.join(data_dir, f"{table}.csv")
        if os.path.exists(file_path):
            data[table] = pd.read_csv(file_path)
            logger.info(f"Loaded {table}.csv with shape {data[table].shape}")
        else:
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"Missing required data file: {file_path}")
    return data
