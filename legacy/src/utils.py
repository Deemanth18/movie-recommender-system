import requests

def get_poster_url_tmdb(title, api_key, year=None):
    """
    Search TMDB for a movie by title (and optional year),
    return its poster URL.
    """
    if not api_key:
        print("⚠️ No TMDB API key provided.")
        return None

    search_url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": title}
    if year:
        params["year"] = year

    try:
        response = requests.get(search_url, params=params)
        print(f"🔍 Request URL: {response.url}")
        response.raise_for_status()
        data = response.json()
        print(f"✅ Response JSON: {data}")
    except Exception as e:
        print(f"❌ TMDB API error: {e}")
        return None

    results = data.get("results", [])
    if not results:
        print(f"⚠️ No results found for {title}")
        return None

    movie = results[0]
    poster_path = movie.get("poster_path")
    if not poster_path:
        print(f"⚠️ No poster path for {title}")
        return None

    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    print(f"✅ Poster URL: {poster_url}")
    return poster_url
