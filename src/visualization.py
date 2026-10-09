import matplotlib.pyplot as plt
import seaborn as sns
from src.logger import setup_logger

logger = setup_logger("visualization")

def plot_claim_distribution(claims_df, output_path="reports/claim_distribution.png"):
    if "claim_amount" in claims_df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(claims_df["claim_amount"], kde=True)
        plt.title("Claim Amount Distribution")
        plt.savefig(output_path)
        plt.close()
        logger.info(f"Saved plot to {output_path}")
