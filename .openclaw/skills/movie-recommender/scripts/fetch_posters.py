"""
Fetch movie poster URL from TMDB API.

Usage:
    python fetch_posters.py "Movie Title" [Year]

Output:
    Prints the poster URL or "NO_POSTER" if not found.

Requires:
    TMDB_API_KEY environment variable to be set.
"""

import sys
import os
import requests
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"


def get_poster_url(title: str, year: str = None) -> str | None:
    """
    Search TMDB for a movie by title (and optional year),
    return its poster URL.
    """
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        logger.warning("TMDB_API_KEY environment variable not set.")
        return None

    params = {"api_key": api_key, "query": title}
    if year:
        params["year"] = year

    try:
        response = requests.get(
            f"{TMDB_BASE_URL}/search/movie",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        logger.error(f"TMDB API request failed: {e}")
        return None

    results = data.get("results", [])
    if not results:
        return None

    poster_path = results[0].get("poster_path")
    if not poster_path:
        return None

    return f"{TMDB_IMAGE_BASE}{poster_path}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_posters.py \"Movie Title\" [Year]")
        sys.exit(1)

    title = sys.argv[1]
    year = sys.argv[2] if len(sys.argv) > 2 else None

    url = get_poster_url(title, year)
    if url:
        print(url)
    else:
        print("NO_POSTER")


if __name__ == "__main__":
    main()
