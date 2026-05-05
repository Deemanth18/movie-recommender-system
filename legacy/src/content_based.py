import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel  # fast cosine for TF-IDF
from difflib import get_close_matches  # for better fuzzy matching


class ContentRecommender:
    def __init__(self):
        self.tfidf = None
        self.tfidf_matrix = None
        self.titles = None
        self.indices = None
        self.movies_df = None

    def fit(self, movies_df, text_column='content'):
        """
        Train the recommender on a movie dataset.
        
        Args:
            movies_df (pd.DataFrame): Must include 'title' and text_column.
            text_column (str): Column used for TF-IDF features.
        """
        self.movies_df = movies_df.copy()
        self.titles = self.movies_df['title'].astype(str)

        # Reverse mapping: title -> index
        self.indices = pd.Series(self.movies_df.index, index=self.titles).drop_duplicates()

        # TF-IDF on content
        self.tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self.tfidf_matrix = self.tfidf.fit_transform(self.movies_df[text_column].astype(str))
        return self

    def recommend(self, title, top_n=10):
        """
        Recommend top_n similar movies given a title.

        Args:
            title (str): Movie title to search for.
            top_n (int): Number of recommendations to return.

        Returns:
            pd.DataFrame: Recommended movies with similarity scores.
        """
        if title not in self.indices:
            # Use fuzzy matching to find the closest title
            close_matches = get_close_matches(title, self.titles, n=1, cutoff=0.6)
            if close_matches:
                title_matched = close_matches[0]
            else:
                raise KeyError(f"'{title}' not found in movie titles.")
        else:
            title_matched = title

        idx = self.indices[title_matched]

        # Cosine similarity
        cosine_similarities = linear_kernel(self.tfidf_matrix[idx:idx+1], self.tfidf_matrix).flatten()

        # Exclude the same movie, sort descending
        related_idx = np.argsort(-cosine_similarities)
        related_idx = related_idx[related_idx != idx]
        top_idx = related_idx[:top_n]

        results = self.movies_df.iloc[top_idx].copy()
        results = results.assign(similarity=cosine_similarities[top_idx])
        return results[['title', 'genres', 'similarity']].reset_index(drop=True)

    def save(self, path):
        """Save trained recommender to a pickle file."""
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path):
        """Load trained recommender from pickle file."""
        with open(path, 'rb') as f:
            return pickle.load(f)
