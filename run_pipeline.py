from src.data_loader import load_raw_data 
from src.validation import validate_raw_data 
from src.data_cleaner import clean_data, save_cleaned_data 
from src.insurance_analysis import calculate_kpis 
from src.insights import generate_insights 
from src.logger import setup_logger 
 
logger = setup_logger("master_pipeline") 
 
def main(): 
    logger.info("Starting Motor Insurance Analytics Pipeline...") 
    data = load_raw_data() 
    validate_raw_data(data) 
    cleaned = clean_data(data) 
    save_cleaned_data(cleaned) 
    kpis = calculate_kpis(cleaned) 
    insights = generate_insights(kpis) 
    print("\n=== PIPELINE SUCCESS ===") 
    print(f"KPIs: {kpis}") 
    print(f"Insights: {insights}") 
 
if __name__ == "__main__": 
    main()
