import os
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv(".quant_env")
print(env_path)
load_dotenv(env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")