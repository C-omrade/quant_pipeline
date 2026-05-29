from datetime import datetime, timedelta
from core.database import engine, Base
from services.data_fetcher import fetch_historical_data

def setup_database():
    print("Creating database tables. ....")
    Base.metadata.create_all(bind=engine)

def run_ingestion(symbol: str, days_back: int= 365):
    end_date = datetime.now() - timedelta(days=1)
    start_date = end_date - timedelta(days=days_back)

    print(f"fetching data for {symbol} from {start_date.date()} to {end_date.date()}...")
    df = fetch_historical_data(symbol, start_date, end_date)

    if df.empty:
        print("no data found")
        return 
    
    print(f"Fetched {len(df)} records. Bulk inserting into PostgreSQL...")
    df.to_sql('market_data', con=engine, if_exists='append', index=False)
    
    print("Data ingestion complete!")

if __name__ == "__main__":
    setup_database()
    run_ingestion("AAPL", 365) # Fetching 1 year of Apple data
    run_ingestion("TSLA", 365)