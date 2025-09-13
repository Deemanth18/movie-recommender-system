import pandas as pd

def load_movies(path="data/movies.csv"):
    """
    Load movies CSV and prepare 'content' field for text vectorization.
    Expected input: movies.csv with columns: movieId, title, genres
    """
    df = pd.read_csv(path)
    # ensure required columns exist
    if not {'movieId', 'title', 'genres'}.issubset(df.columns):
        raise ValueError("movies.csv must contain movieId, title and genres columns.")
    # fill missing
    df['genres'] = df['genres'].fillna('')
    # create content column: combine title + genres (you can add overview/cast later)
    df['content'] = (df['title'].astype(str) + ' ' + df['genres'].astype(str)).str.lower()
    # keep index consistent
    df = df.reset_index(drop=True)
    return df
