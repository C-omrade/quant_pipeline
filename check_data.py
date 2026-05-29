import pandas as pd
from core.database import engine

def view_data():
    query = """
    select * from market_data
    where symbol = 'TSLA'
    order by timestamp desc
    limit 10
    """
    print("Querying Database.....")

    df = pd.read_sql(query, engine)

    print("\n -- Last 10 days TSLA Data ---")
    print(df.to_string())

if __name__ == "__main__":
    view_data()