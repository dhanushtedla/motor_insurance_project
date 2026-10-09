from src.logger import setup_logger 
 
logger = setup_logger("insights") 
 
def generate_insights(kpis): 
    insights = [] 
    claim_ratio = kpis.get("claim_ratio_percent", 0) 
    if claim_ratio > 70: 
        insights.append("High Loss Ratio detected (>70%%). Review pricing strategy.") 
    else: 
        insights.append("Loss ratio is within acceptable risk limits.") 
    logger.info("Generated executive insights.") 
    return insights
