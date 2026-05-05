import requests

class TMDBHelper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"
        self.image_base = "https://image.tmdb.org/t/p/w500"

    def search_movie(self, title, year=None):
        """
        Search for a movie by title (and optionally year).
        Returns JSON with movie results.
        """
        params = {"api_key": self.api_key, "query": title}
        if year:
            params["year"] = year
        url = f"{self.base_url}/search/movie"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get("results", [])
            return results[0] if results else None
        return None

    def get_poster_url(self, movie_id):
        """
        Get poster URL for a movie given its TMDB ID.
        """
        url = f"{self.base_url}/movie/{movie_id}"
        params = {"api_key": self.api_key}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return f"{self.image_base}{poster_path}"
        return None
