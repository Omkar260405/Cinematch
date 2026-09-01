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
# 2. EXTRACT GENRES AND KEYWORDS
# ==========================================

def convert(text):
    try:
        items = ast.literal_eval(text)

        names = []

        for item in items:
            names.append(item["name"])

        return names

    except:
        return []


# ==========================================
# 3. EXTRACT TOP 3 CAST MEMBERS
# ==========================================

def get_cast(text):
    try:
        items = ast.literal_eval(text)

        names = []

        for item in items[:3]:
            names.append(item["name"])

        return names

    except:
        return []


# ==========================================
# 4. EXTRACT DIRECTOR
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
# 5. LOAD MOVIE INFORMATION
# ==========================================

movies["genres_list"] = movies[
    "genres"
].apply(convert)

movies["keywords_list"] = movies[
    "keywords"
].apply(convert)


# ==========================================
# 6. LOAD CAST & DIRECTOR
# ==========================================

credits["cast_list"] = credits[
    "cast"
].apply(get_cast)

credits["director"] = credits[
    "crew"
].apply(get_director)


# ==========================================
# 7. MERGE DATASETS
# ==========================================

movies = movies.merge(
    credits[
        [
            "movie_id",
            "cast_list",
            "director"
        ]
    ],
    left_on="id",
    right_on="movie_id",
    how="left"
)


# ==========================================
# 8. HANDLE MISSING VALUES
# ==========================================

movies["cast_list"] = movies[
    "cast_list"
].apply(
    lambda x: x if isinstance(x, list) else []
)

movies["genres_list"] = movies[
    "genres_list"
].apply(
    lambda x: x if isinstance(x, list) else []
)

movies["keywords_list"] = movies[
    "keywords_list"
].apply(
    lambda x: x if isinstance(x, list) else []
)

movies["director"] = movies[
    "director"
].fillna("")

movies["overview"] = movies[
    "overview"
].fillna("")


# ==========================================
# 9. CREATE TEXT TAGS FOR ML
# ==========================================

movies["genres"] = movies[
    "genres_list"
].apply(
    lambda x: " ".join(x)
)

movies["keywords"] = movies[
    "keywords_list"
].apply(
    lambda x: " ".join(x)
)

movies["cast"] = movies[
    "cast_list"
].apply(
    lambda x: " ".join(x)
)


movies["tags"] = (
    movies["genres"]
    + " "
    + movies["keywords"]
    + " "
    + movies["cast"]
    + " "
    + movies["director"]
    + " "
    + movies["overview"]
)


movies["tags"] = movies[
    "tags"
].str.lower()


# ==========================================
# 10. TF-IDF
# ==========================================

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(
    movies["tags"]
)


# ==========================================
# 11. COSINE SIMILARITY
# ==========================================

similarity = cosine_similarity(
    tfidf_matrix
)


# ==========================================
# 12. MOVIE INDEX
# ==========================================

movie_indices = pd.Series(
    movies.index,
    index=movies["title"]
).drop_duplicates()


# ==========================================
# 13. RECOMMENDATION FUNCTION
# ==========================================

def recommend_movies(
    movie_title,
    number_of_recommendations=5
):

    if movie_title not in movie_indices:
        return []

    movie_index = movie_indices[
        movie_title
    ]

    similarity_scores = list(
        enumerate(
            similarity[movie_index]
        )
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    selected_movie = movies.iloc[
        movie_index
    ]

    recommendations = []

    for index, score in similarity_scores:

        # Don't recommend the same movie
        if index == movie_index:
            continue

        movie = movies.iloc[index]

        reasons = []

        # ==================================
        # GENRE SIMILARITY
        # ==================================

        selected_genres = set(
            selected_movie["genres_list"]
        )

        recommended_genres = set(
            movie["genres_list"]
        )

        common_genres = (
            selected_genres
            & recommended_genres
        )

        if common_genres:

            reasons.append(
                "Similar genres: "
                + ", ".join(
                    list(common_genres)[:3]
                )
            )


        # ==================================
        # KEYWORD SIMILARITY
        # ==================================

        selected_keywords = set(
            selected_movie[
                "keywords_list"
            ]
        )

        recommended_keywords = set(
            movie[
                "keywords_list"
            ]
        )

        common_keywords = (
            selected_keywords
            & recommended_keywords
        )

        if common_keywords:

            reasons.append(
                "Similar themes: "
                + ", ".join(
                    list(common_keywords)[:3]
                )
            )


        # ==================================
        # CAST SIMILARITY
        # ==================================

        selected_cast = set(
            selected_movie[
                "cast_list"
            ]
        )

        recommended_cast = set(
            movie[
                "cast_list"
            ]
        )

        common_cast = (
            selected_cast
            & recommended_cast
        )

        if common_cast:

            reasons.append(
                "Shared cast: "
                + ", ".join(
                    list(common_cast)[:3]
                )
            )


        # ==================================
        # DIRECTOR SIMILARITY
        # ==================================

        if (
            selected_movie["director"]
            and
            selected_movie["director"]
            == movie["director"]
        ):

            reasons.append(
                "Same director: "
                + movie["director"]
            )


        # ==================================
        # FALLBACK REASON
        # ==================================

        if not reasons:

            reasons.append(
                "Similar overall movie content"
            )


        # ==================================
        # RELEASE YEAR
        # ==================================

        release_year = "N/A"

        if pd.notna(
            movie["release_date"]
        ):

            release_year = str(
                movie["release_date"]
            )[:4]


        # ==================================
        # FINAL RESULT
        # ==================================

        recommendations.append(
            {
                "title": movie["title"],

                "movie_id": int(
                    movie["id"]
                ),

                "similarity": score,

                "rating": movie[
                    "vote_average"
                ],

                "genres": movie[
                    "genres"
                ],

                "release_year": release_year,

                "reasons": reasons
            }
        )


        if len(
            recommendations
        ) >= number_of_recommendations:

            break


    return recommendations