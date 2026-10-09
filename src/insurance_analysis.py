import pandas as pd
from src.logger import setup_logger

logger = setup_logger("insurance_analysis")

def calculate_kpis(cleaned_data):
    policies_df = cleaned_data.get("policies", pd.DataFrame())
    claims_df = cleaned_data.get("claims", pd.DataFrame())
    total_premium = policies_df["premium_amount"].sum() if "premium_amount" in policies_df.columns else 0
    total_claims = claims_df["claim_amount"].sum() if "claim_amount" in claims_df.columns else 0
    claim_ratio = (total_claims / total_premium) * 100 if total_premium > 0 else 0
    kpis = {
        "total_premium": total_premium,
        "total_claims": total_claims,
        "claim_ratio_percent": claim_ratio
    }
    logger.info(f"Calculated KPIs: {kpis}")
    return kpis
