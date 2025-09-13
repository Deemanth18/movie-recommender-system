import os
from dotenv import load_dotenv

load_dotenv()  # load .env if present

# You can set TMDB_API_KEY in your environment or create a .env with TMDB_API_KEY=your_key
TMDB_API_KEY = os.getenv("679bd301c1cd9e46558a8420519988f5")
