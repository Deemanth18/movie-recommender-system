# Streamlit front-end for the content-based recommender
import streamlit as st
import pandas as pd
import sys
import os

# ensure src is importable when running from project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.preprocessing import load_movies
from src.content_based import ContentRecommender
from src.utils import get_poster_url_tmdb
from app.config import TMDB_API_KEY


# ----------------- CONFIG -----------------
st.set_page_config(
    page_title="Movie Recommender",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- CACHING -----------------
@st.cache_data
def load_data(path="data/movies.csv"):
    return load_movies(path)

@st.cache_resource
def build_recommender(movies_df):
    rec = ContentRecommender()
    rec.fit(movies_df)
    return rec

# ----------------- APP -----------------
def main():
    # Sidebar
    st.sidebar.title("⚙️ Settings")
    st.sidebar.write("Paste your TMDB API key here to show posters.")
    api_key_input = st.sidebar.text_input(
        "TMDB API key (optional)",
        value=TMDB_API_KEY or "",
        type="password"
    )
    num_rec = st.sidebar.slider("Number of recommendations", 3, 15, 6)

    # Main Title
    st.title("🎬 Movie Recommender — Content-Based")
    st.markdown(
        """
        This app uses **TF-IDF** on movie *title + genres* to compute similarity between movies.  
        Select a movie and get similar ones. For posters, provide a TMDB API key in the sidebar.
        """
    )

    # Load dataset
    try:
        movies_df = load_data()
    except Exception as e:
        st.error(f"❌ Failed to load dataset. Put `movies.csv` in `data/` folder. Error: {e}")
        return

    recommender = build_recommender(movies_df)

    # Search inputs
    titles = movies_df['title'].tolist()
    movie_choice = st.selectbox("🎥 Select a movie (or start typing):", options=titles, index=0)

    manual = st.text_input("Or type movie title manually:", value="")
    chosen_title = manual.strip() if manual.strip() else movie_choice

    # Recommend button
    if st.button("🔎 Recommend"):
        try:
            recommendations = recommender.recommend(chosen_title, top_n=num_rec)
        except KeyError as e:
            st.warning(str(e))
            return
        except Exception as e:
            st.error(f"Error while recommending: {e}")
            return

        # Display Recommendations
        st.subheader(f"✅ Recommendations for: **{chosen_title}**")

        cols = st.columns(3)
        for idx, row in recommendations.iterrows():
            col = cols[idx % 3]
            title = row['title']

            # Extract year if available
            year = None
            if '(' in title and title.strip().endswith(')'):
                try:
                    year_candidate = title.split('(')[-1].replace(')', '')
                    if year_candidate.isdigit():
                        year = int(year_candidate)
                except Exception:
                    year = None

            poster_url = get_poster_url_tmdb(title, api_key_input, year)

            with col:
                st.markdown(f"### {title}")
                if poster_url:
                    st.image(poster_url, use_column_width=True)
                else:
                    st.write("_Poster unavailable_")

                # Extra metadata
                if 'genres' in recommendations.columns:
                    st.caption(f"🎭 Genres: {row.get('genres', '')}")
                if 'similarity' in row:
                    st.caption(f"📊 Similarity Score: {row['similarity']:.3f}")

        # Footer Tip
        st.write("---")
        st.info("💡 Tip: Add more features (overview, cast, director) in `data/` to improve quality.")

    # Sidebar footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("👨‍💻 **Project**: Great for portfolio. Add a README, demo video, and GitHub repo!")

# ----------------- ENTRYPOINT -----------------
if __name__ == "__main__":
    main()
