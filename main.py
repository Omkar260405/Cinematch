import pandas as pd
import ast

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# 1. LOAD DATASETS
# ==========================================

movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("dataset/tmdb_5000_credits.csv")


# ==========================================
# 2. FUNCTION TO EXTRACT GENRES/KEYWORDS
# ==========================================

def convert(text):
    try:
        items = ast.literal_eval(text)

        names = []

        for item in items:
            names.append(item["name"])

        return " ".join(names)

    except:
        return ""


# ==========================================
# 3. FUNCTION TO EXTRACT TOP 3 CAST MEMBERS
# ==========================================

def get_cast(text):
    try:
        items = ast.literal_eval(text)

        names = []

        for item in items[:3]:
            names.append(item["name"])

        return " ".join(names)

    except:
        return ""


# ==========================================
# 4. FUNCTION TO EXTRACT DIRECTOR
# ==========================================

def get_director(text):
    try:
        items = ast.literal_eval(text)

        for item in items:
            if item["job"] == "Director":
                return item["name"]

        return ""

    except:
        return ""


# ==========================================
# 5. CLEAN MOVIE DATA
# ==========================================

movies["genres"] = movies["genres"].apply(convert)

movies["keywords"] = movies["keywords"].apply(convert)


# ==========================================
# 6. CLEAN CREDITS DATA
# ==========================================

credits["cast"] = credits["cast"].apply(get_cast)

credits["crew"] = credits["crew"].apply(get_director)


# ==========================================
# 7. RENAME DIRECTOR COLUMN
# ==========================================

credits.rename(
    columns={"crew": "director"},
    inplace=True
)


# ==========================================
# 8. COMBINE MOVIE + CREDITS DATA
# ==========================================

movies = movies.merge(
    credits[["movie_id", "cast", "director"]],
    left_on="id",
    right_on="movie_id",
    how="left"
)


# ==========================================
# 9. HANDLE MISSING VALUES
# ==========================================

movies["cast"] = movies["cast"].fillna("")

movies["director"] = movies["director"].fillna("")

movies["overview"] = movies["overview"].fillna("")


# ==========================================
# 10. CREATE COMBINED TAGS
# ==========================================

movies["tags"] = (
    movies["genres"] + " "
    + movies["keywords"] + " "
    + movies["cast"] + " "
    + movies["director"] + " "
    + movies["overview"]
)


# Convert everything to lowercase
movies["tags"] = movies["tags"].apply(
    lambda x: x.lower()
)


# ==========================================
# 11. TF-IDF
# ==========================================

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(
    movies["tags"]
)


# ==========================================
# 12. COSINE SIMILARITY
# ==========================================

similarity = cosine_similarity(
    tfidf_matrix
)


# ==========================================
# 13. CREATE MOVIE INDEX
# ==========================================

movie_indices = pd.Series(
    movies.index,
    index=movies["title"]
).drop_duplicates()


# ==========================================
# 14. RECOMMENDATION FUNCTION
# ==========================================

def recommend_movies(
    movie_title,
    number_of_recommendations=5
):

    if movie_title not in movie_indices:
        print("Movie not found.")
        return

    movie_index = movie_indices[movie_title]

    similarity_scores = list(
        enumerate(similarity[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print(
        f"\nRecommendations for: {movie_title}\n"
    )

    count = 0

    for index, score in similarity_scores:

        # Don't recommend the movie itself
        if index == movie_index:
            continue

        movie_name = movies.iloc[index]["title"]

        print(
            f"{count + 1}. {movie_name} "
            f"(Similarity: {score:.2f})"
        )

        count += 1

        if count >= number_of_recommendations:
            break


# ==========================================
# 15. TEST RECOMMENDATION
# ==========================================

recommend_movies("Avatar")