import requests

def get_poster_url_tmdb(title, api_key, year=None):
    """
    Search TMDB for a movie by title (and optional year),
    return its poster URL.
    """
    if not api_key:
        return None  # No key provided

    search_url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": title}
    if year:
        params["year"] = year

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
    except Exception as e:
        print(f"TMDB API error: {e}")
        return None

    results = response.json().get("results", [])
    if not results:
        return None

    movie = results[0]  # take best match
    poster_path = movie.get("poster_path")
    if not poster_path:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster_path}"
