import os
from dotenv import load_dotenv

load_dotenv()  # load .env if present

# You can set TMDB_API_KEY in your environment or create a .env with TMDB_API_KEY=your_key
TMDB_API_KEY = os.getenv("a41d0ccc6d2babfbf98058b17f933106")
