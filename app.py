import streamlit as st
import requests

from recommender import movies, recommend_movies


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    /* ======================================
       MAIN APP
       ====================================== */

    .stApp {
        background-color: #0b0f19;
    }


    /* ======================================
       BRAND
       ====================================== */

    .brand-title {
        font-size: 32px;
        font-weight: 800;
        line-height: 1.1;
        margin-top: 0px;
    }

    .brand-slogan {
        font-size: 14px;
        opacity: 0.70;
        margin-top: 4px;
    }


    /* ======================================
       SECTION TITLE
       ====================================== */

    .section-title {
        font-size: 30px;
        font-weight: 800;
        margin-top: 30px;
        margin-bottom: 22px;
        letter-spacing: -0.5px;
    }


    /* ======================================
       MOVIE CARD
       ====================================== */

    .movie-card {
        background-color: #111827;
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 18px;
        border: 1px solid #20283a;
        overflow: hidden;
    }


    /* ======================================
       MOVIE TITLE
       ====================================== */

    .movie-title {
        font-size: 21px;
        font-weight: 800;
        margin-top: 12px;
        line-height: 1.35;
        word-break: break-word;
    }


    /* ======================================
       MOVIE INFORMATION
       ====================================== */

    .movie-info {
        font-size: 16px;
        font-weight: 500;
        margin-top: 8px;
        line-height: 1.5;
        opacity: 0.95;
        word-break: break-word;
    }


    /* ======================================
       MATCH BADGE
       ====================================== */

    .match-badge {
        display: inline-block;
        background-color: #18243a;
        padding: 7px 12px;
        border-radius: 8px;
        font-size: 15px;
        font-weight: 800;
        margin-top: 10px;
    }


    /* ======================================
       REASON BOX
       ====================================== */

    .reason-box {
        background-color: #151b2b;
        padding: 16px;
        border-radius: 12px;
        margin-top: 15px;
        margin-bottom: 15px;
        border: 1px solid #20283a;
    }

    .reason-title {
        font-size: 18px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .reason-item {
        font-size: 15px;
        margin: 7px 0;
        line-height: 1.4;
        opacity: 0.95;
        word-break: break-word;
    }


    /* ======================================
       SEARCH RESULT
       ====================================== */

    .search-movie-title {
        font-size: 24px;
        font-weight: 800;
        line-height: 1.3;
        margin-bottom: 8px;
        word-break: break-word;
    }

    .search-movie-info {
        font-size: 16px;
        line-height: 1.6;
        margin-top: 8px;
    }


    /* ======================================
       DETAIL PAGE
       ====================================== */

    .detail-title {
        font-size: 32px;
        font-weight: 800;
        line-height: 1.3;
        margin-bottom: 14px;
        word-break: break-word;
    }

    .detail-meta {
        font-size: 17px;
        margin-bottom: 10px;
        line-height: 1.5;
        word-break: break-word;
    }


    /* ======================================
       HISTORY
       ====================================== */

    .history-item {
        background-color: #111827;
        border: 1px solid #20283a;
        border-radius: 10px;
        padding: 14px 16px;
        margin-bottom: 9px;
        font-size: 16px;
        font-weight: 500;
        word-break: break-word;
    }


    /* ======================================
       EMPTY STATE
       ====================================== */

    .empty-state {
        background-color: #111827;
        border: 1px solid #20283a;
        border-radius: 14px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }


    /* ======================================
       BUTTONS
       ====================================== */

    .stButton > button {
        border-radius: 9px;
        font-weight: 650;
        min-height: 43px;
        font-size: 15px;
        white-space: normal;
    }


    /* ======================================
       TOP ICON BUTTONS
       ====================================== */

    .icon-button button {
        font-size: 21px !important;
        border-radius: 10px !important;
        min-height: 45px !important;
    }


    /* ======================================
       IMAGES
       ====================================== */

    img {
        max-width: 100%;
        height: auto;
    }


    /* ======================================
       TABLET
       ====================================== */

    @media (max-width: 900px) {

        .brand-title {
            font-size: 28px;
        }

        .brand-slogan {
            font-size: 13px;
        }

        .section-title {
            font-size: 26px;
            margin-top: 24px;
            margin-bottom: 18px;
        }

        .movie-title {
            font-size: 19px;
        }

        .movie-info {
            font-size: 15px;
        }

        .reason-title {
            font-size: 17px;
        }

        .reason-item {
            font-size: 14px;
        }

        .detail-title {
            font-size: 28px;
        }

        .detail-meta {
            font-size: 16px;
        }

        .search-movie-title {
            font-size: 21px;
        }

        .search-movie-info {
            font-size: 15px;
        }

    }


    /* ======================================
       MOBILE
       ====================================== */

    @media (max-width: 600px) {

        /* Main spacing */

        .block-container {
            padding-left: 12px !important;
            padding-right: 12px !important;
        }


        /* Brand */

        .brand-title {
            font-size: 24px;
        }

        .brand-slogan {
            font-size: 12px;
        }


        /* Sections */

        .section-title {
            font-size: 23px;
            margin-top: 20px;
            margin-bottom: 16px;
        }


        /* Movie cards */

        .movie-card {
            padding: 12px;
            border-radius: 12px;
            margin-bottom: 14px;
        }

        .movie-title {
            font-size: 18px;
            margin-top: 9px;
        }

        .movie-info {
            font-size: 14px;
            margin-top: 6px;
        }


        /* Match */

        .match-badge {
            font-size: 13px;
            padding: 6px 9px;
        }


        /* Reason */

        .reason-box {
            padding: 12px;
            margin-top: 12px;
        }

        .reason-title {
            font-size: 16px;
        }

        .reason-item {
            font-size: 13px;
            margin: 5px 0;
        }


        /* Search */

        .search-movie-title {
            font-size: 20px;
        }

        .search-movie-info {
            font-size: 14px;
        }


        /* Details */

        .detail-title {
            font-size: 25px;
        }

        .detail-meta {
            font-size: 15px;
        }


        /* History */

        .history-item {
            font-size: 14px;
            padding: 12px;
        }


        /* Buttons */

        .stButton > button {
            min-height: 40px;
            font-size: 14px;
        }


        /* Empty state */

        .empty-state {
            padding: 22px 14px;
        }

    }


    /* ======================================
       VERY SMALL PHONES
       ====================================== */

    @media (max-width: 400px) {

        .brand-title {
            font-size: 21px;
        }

        .brand-slogan {
            font-size: 11px;
        }

        .section-title {
            font-size: 21px;
        }

        .movie-title {
            font-size: 17px;
        }

        .movie-info {
            font-size: 13px;
        }

        .detail-title {
            font-size: 22px;
        }

        .detail-meta {
            font-size: 14px;
        }

        .search-movie-title {
            font-size: 18px;
        }

        .reason-title {
            font-size: 15px;
        }

        .reason-item {
            font-size: 12px;
        }

    }


    /* ======================================
       DIVIDER
       ====================================== */

    hr {
        opacity: 0.25;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# TMDB SESSION
# ==========================================

@st.cache_resource
def get_session():

    try:

        token = st.secrets["TMDB_ACCESS_TOKEN"]

        if not token:

            return None

        session = requests.Session()

        session.headers.update(
            {
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        return session

    except Exception as error:

        print(
            f"TMDB configuration error: {error}",
            flush=True
        )

        return None


# ==========================================
# CACHED SEARCH
# ==========================================

@st.cache_data(
    ttl=3600,
    show_spinner=False
)
def search_tmdb(query):

    session = get_session()

    if session is None:

        return {
            "success": False,
            "results": [],
            "error": "TMDB API token is missing."
        }

    url = (
        "https://api.themoviedb.org/3/"
        "search/movie"
    )

    params = {
        "query": query,
        "include_adult": False,
        "language": "en-US"
    }

    try:

        response = session.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code == 200:

            return {
                "success": True,
                "results": response.json().get(
                    "results",
                    []
                ),
                "error": None
            }

        if response.status_code == 401:

            return {
                "success": False,
                "results": [],
                "error": "TMDB authorization failed."
            }

        if response.status_code == 429:

            return {
                "success": False,
                "results": [],
                "error": "TMDB request limit reached."
            }

        print(
            f"TMDB search error: "
            f"{response.status_code}",
            flush=True
        )

        return {
            "success": False,
            "results": [],
            "error": "TMDB search request failed."
        }

    except requests.Timeout:

        print(
            "TMDB search timeout.",
            flush=True
        )

        return {
            "success": False,
            "results": [],
            "error": "TMDB request timed out."
        }

    except requests.ConnectionError:

        print(
            "TMDB connection error.",
            flush=True
        )

        return {
            "success": False,
            "results": [],
            "error": "Could not connect to TMDB."
        }

    except requests.RequestException as error:

        print(
            f"TMDB request error: {error}",
            flush=True
        )

        return {
            "success": False,
            "results": [],
            "error": "Unable to contact TMDB."
        }

    except Exception as error:

        print(
            f"Unexpected TMDB search error: {error}",
            flush=True
        )

        return {
            "success": False,
            "results": [],
            "error": "Unexpected search error."
        }


# ==========================================
# CACHED MOVIE DETAILS
# ==========================================

@st.cache_data(
    ttl=3600,
    show_spinner=False
)
def get_movie_details(movie_id):

    session = get_session()

    if session is None:

        return {
            "success": False,
            "details": None,
            "error": "TMDB API token is missing."
        }

    url = (
        f"https://api.themoviedb.org/3/movie/"
        f"{movie_id}"
    )

    try:

        response = session.get(
            url,
            timeout=10
        )

        if response.status_code == 200:

            return {
                "success": True,
                "details": response.json(),
                "error": None
            }

        if response.status_code == 401:

            return {
                "success": False,
                "details": None,
                "error": "TMDB authorization failed."
            }

        if response.status_code == 404:

            return {
                "success": False,
                "details": None,
                "error": "Movie was not found on TMDB."
            }

        if response.status_code == 429:

            return {
                "success": False,
                "details": None,
                "error": "TMDB request limit reached."
            }

        print(
            f"TMDB details error: "
            f"{response.status_code}",
            flush=True
        )

        return {
            "success": False,
            "details": None,
            "error": "Movie details request failed."
        }

    except requests.Timeout:

        print(
            "TMDB details timeout.",
            flush=True
        )

        return {
            "success": False,
            "details": None,
            "error": "TMDB request timed out."
        }

    except requests.ConnectionError:

        print(
            "TMDB details connection error.",
            flush=True
        )

        return {
            "success": False,
            "details": None,
            "error": "Could not connect to TMDB."
        }

    except requests.RequestException as error:

        print(
            f"TMDB details request error: {error}",
            flush=True
        )

        return {
            "success": False,
            "details": None,
            "error": "Unable to contact TMDB."
        }

    except Exception as error:

        print(
            f"Unexpected TMDB details error: {error}",
            flush=True
        )

        return {
            "success": False,
            "details": None,
            "error": "Unexpected movie details error."
        }


# ==========================================
# POSTER URL
# ==========================================

def get_poster(
    poster_path,
    size="w500"
):

    if poster_path:

        return (
            f"https://image.tmdb.org/t/p/"
            f"{size}{poster_path}"
        )

    return None


# ==========================================
# SESSION STATE
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

if "search_query" not in st.session_state:
    st.session_state.search_query = ""

if "search_results" not in st.session_state:
    st.session_state.search_results = []

if "last_search" not in st.session_state:
    st.session_state.last_search = ""

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

if "search_history" not in st.session_state:
    st.session_state.search_history = []

if "recommendation_history" not in st.session_state:
    st.session_state.recommendation_history = []


# ==========================================
# FEATURED MOVIES
# ==========================================

if "featured_movies" not in st.session_state:

    try:

        required_columns = [
            "id",
            "title",
            "vote_average",
            "release_date"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in movies.columns
        ]

        if missing_columns:

            st.session_state.featured_movies = None

            print(
                f"Missing dataset columns: "
                f"{missing_columns}",
                flush=True
            )

        else:

            featured = movies[
                required_columns
            ].dropna(
                subset=["title"]
            )

            if len(featured) > 0:

                st.session_state.featured_movies = (
                    featured.sample(
                        n=min(
                            10,
                            len(featured)
                        ),
                        random_state=42
                    )
                )

            else:

                st.session_state.featured_movies = None

    except Exception as error:

        print(
            f"Featured movies error: {error}",
            flush=True
        )

        st.session_state.featured_movies = None


# ==========================================================
# TOP HEADER
# ==========================================================

header_left, header_space, header_search, header_watchlist, header_history, header_home = st.columns(
    [5, 1.8, 0.7, 0.7, 0.7, 0.7]
)


# ==========================================
# BRAND
# ==========================================

with header_left:

    st.markdown(
        """
        <div class="brand-title">
            🎬 CineMatch
        </div>

        <div class="brand-slogan">
            Discover your next favourite movie 🍿
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# SEARCH ICON
# ==========================================

with header_search:

    if st.button(
        "🔎",
        key="top_search",
        help="Search movies",
        use_container_width=True
    ):

        st.session_state.page = "search"

        st.rerun()


# ==========================================
# WATCHLIST ICON
# ==========================================

with header_watchlist:

    if st.button(
        "❤️",
        key="top_watchlist",
        help="Watchlist",
        use_container_width=True
    ):

        st.session_state.page = "watchlist"

        st.rerun()


# ==========================================
# HISTORY ICON
# ==========================================

with header_history:

    if st.button(
        "🕘",
        key="top_history",
        help="History",
        use_container_width=True
    ):

        st.session_state.page = "history"

        st.rerun()


# ==========================================
# HOME ICON
# ==========================================

with header_home:

    if st.button(
        "🏠",
        key="top_home",
        help="Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


st.divider()


# ==========================================================
# HOME PAGE
# ==========================================================

if st.session_state.page == "home":

    st.markdown(
        '<div class="section-title">'
        '🔥 Featured Movies'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.featured_movies is None:

        st.error(
            "❌ Featured movies could not be loaded."
        )

        st.info(
            "Please check your ML dataset."
        )

    else:

        featured_movies = (
            st.session_state.featured_movies
        )

        columns = st.columns(5)

        for i, (_, movie) in enumerate(
            featured_movies.iterrows()
        ):

            with columns[i % 5]:

                movie_result = get_movie_details(
                    int(movie["id"])
                )

                if (
                    not movie_result["success"]
                    or movie_result["details"] is None
                ):

                    st.warning(
                        "Movie details unavailable."
                    )

                    continue

                details = movie_result["details"]

                st.markdown(
                    '<div class="movie-card">',
                    unsafe_allow_html=True
                )

                poster_url = get_poster(
                    details.get(
                        "poster_path"
                    ),
                    "w342"
                )

                if poster_url:

                    st.image(
                        poster_url,
                        use_container_width=True
                    )

                else:

                    st.write(
                        "🖼️ Poster unavailable"
                    )

                st.markdown(
                    f'<div class="movie-title">'
                    f'{movie["title"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="movie-info">'
                    f'⭐ '
                    f'{details.get("vote_average", 0):.1f}'
                    f'/10'
                    f'</div>',
                    unsafe_allow_html=True
                )

                if st.button(
                    "🎬 View Movie",
                    key=f"featured_{movie['id']}",
                    use_container_width=True
                ):

                    st.session_state.selected_movie = (
                        movie["title"]
                    )

                    st.session_state.selected_tmdb_id = (
                        int(movie["id"])
                    )

                    st.session_state.page = "details"

                    st.rerun()

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


# ==========================================================
# SEARCH PAGE
# ==========================================================

elif st.session_state.page == "search":

    st.markdown(
        '<div class="section-title">'
        '🔎 Search Movies'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Find movies from the CineMatch ML dataset."
    )

    search_text = st.text_input(
        "Movie name",
        placeholder=(
            "Example: Avatar, Inception, "
            "Interstellar..."
        ),
        key="movie_search_input"
    )

    if search_text.strip():

        if (
            st.session_state.get(
                "last_search",
                ""
            )
            != search_text.strip()
        ):

            with st.spinner(
                "🔎 Searching movies..."
            ):

                search_result = search_tmdb(
                    search_text.strip()
                )

            if not search_result["success"]:

                st.error(
                    "❌ "
                    + search_result["error"]
                )

                st.info(
                    "Please check your internet "
                    "connection and try again."
                )

            else:

                results = search_result["results"]

                search_value = (
                    search_text.strip()
                )

                if search_value not in (
                    st.session_state.search_history
                ):

                    st.session_state.search_history.insert(
                        0,
                        search_value
                    )

                try:

                    if "title" not in movies.columns:

                        st.error(
                            "❌ ML dataset does not "
                            "contain a title column."
                        )

                        st.stop()

                    ml_titles = set(
                        movies["title"]
                        .dropna()
                        .astype(str)
                        .str.strip()
                        .str.lower()
                    )

                except Exception as error:

                    print(
                        f"Dataset search error: {error}",
                        flush=True
                    )

                    st.error(
                        "❌ Unable to search the "
                        "ML dataset."
                    )

                    st.stop()

                filtered_results = []

                for result in results:

                    tmdb_title = result.get(
                        "title",
                        ""
                    ).strip().lower()

                    if tmdb_title in ml_titles:

                        filtered_results.append(
                            result
                        )

                st.session_state.search_query = (
                    search_text.strip()
                )

                st.session_state.search_results = (
                    filtered_results[:8]
                )

                st.session_state.last_search = (
                    search_text.strip()
                )

                st.session_state.page = (
                    "search_results"
                )

                st.rerun()


# ==========================================================
# SEARCH RESULTS PAGE
# ==========================================================

elif st.session_state.page == "search_results":

    st.markdown(
        '<div class="section-title">'
        '🎬 Search Results'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        f'Results for: '
        f'**{st.session_state.search_query}**'
    )

    search_results = (
        st.session_state.search_results
    )

    if st.button(
        "← Back to Search"
    ):

        st.session_state.page = "search"

        st.session_state.last_search = ""

        st.rerun()

    st.divider()

    if search_results:

        for result in search_results:

            movie_title = result.get(
                "title",
                "Unknown"
            )

            release_date = result.get(
                "release_date",
                ""
            )

            poster_path = result.get(
                "poster_path"
            )

            col1, col2 = st.columns(
                [1, 4]
            )

            with col1:

                poster_url = get_poster(
                    poster_path,
                    "w185"
                )

                if poster_url:

                    st.image(
                        poster_url,
                        use_container_width=True
                    )

                else:

                    st.write(
                        "🖼️ No poster"
                    )

            with col2:

                st.markdown(
                    f'<div class="search-movie-title">'
                    f'{movie_title}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                if release_date:

                    st.markdown(
                        f'<div class="search-movie-info">'
                        f'📅 {release_date[:4]}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                overview = result.get(
                    "overview",
                    ""
                )

                if overview:

                    st.write(
                        overview
                    )

                else:

                    st.write(
                        "No overview available."
                    )

                if st.button(
                    "🎬 Select Movie",
                    key=f"search_{result['id']}"
                ):

                    st.session_state.selected_movie = (
                        movie_title
                    )

                    st.session_state.selected_tmdb_id = (
                        result["id"]
                    )

                    st.session_state.page = "details"

                    st.rerun()

            st.divider()

    else:

        st.markdown(
            """
            <div class="empty-state">
                <h3>🎬 No movies found</h3>
                <p>
                    This movie is not available
                    in the CineMatch ML dataset.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================================
# MOVIE DETAILS PAGE
# ==========================================================

elif st.session_state.page == "details":

    movie_id = (
        st.session_state.selected_tmdb_id
    )

    selected_movie = (
        st.session_state.selected_movie
    )

    if movie_id is None:

        st.error(
            "❌ No movie selected."
        )

        if st.button(
            "← Back to Search"
        ):

            st.session_state.page = "search"

            st.rerun()

    else:

        with st.spinner(
            "🎬 Loading movie details..."
        ):

            movie_result = get_movie_details(
                movie_id
            )

        if not movie_result["success"]:

            st.error(
                "❌ "
                + movie_result["error"]
            )

            if st.button(
                "← Back to Search Results"
            ):

                st.session_state.page = (
                    "search_results"
                )

                st.rerun()

        else:

            details = movie_result["details"]

            st.markdown(
                '<div class="section-title">'
                '🎬 Movie Details'
                '</div>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(
                [1, 2]
            )

            with col1:

                poster_url = get_poster(
                    details.get(
                        "poster_path"
                    )
                )

                if poster_url:

                    st.image(
                        poster_url,
                        use_container_width=True
                    )

                else:

                    st.info(
                        "🖼️ Poster unavailable"
                    )

            with col2:

                st.markdown(
                    f'<div class="detail-title">'
                    f'{details.get("title", selected_movie)}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="detail-meta">'
                    f'⭐ <b>Rating:</b> '
                    f'{details.get("vote_average", 0):.1f}/10'
                    f'</div>',
                    unsafe_allow_html=True
                )

                release_date = details.get(
                    "release_date",
                    ""
                )

                if release_date:

                    st.markdown(
                        f'<div class="detail-meta">'
                        f'📅 <b>Release:</b> '
                        f'{release_date[:4]}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                genres = details.get(
                    "genres",
                    []
                )

                if genres:

                    genre_names = [
                        genre.get(
                            "name",
                            ""
                        )
                        for genre in genres
                    ]

                    genre_names = [
                        genre
                        for genre in genre_names
                        if genre
                    ]

                    if genre_names:

                        st.markdown(
                            '<div class="detail-meta">'
                            '🎭 <b>Genres:</b> '
                            + " • ".join(
                                genre_names
                            )
                            + '</div>',
                            unsafe_allow_html=True
                        )

                st.write("")

                st.markdown(
                    "### 📖 Overview"
                )

                overview = details.get(
                    "overview",
                    ""
                )

                if overview:

                    st.write(
                        overview
                    )

                else:

                    st.info(
                        "No overview available."
                    )

                st.write("")

                # ==================================
                # WATCHLIST
                # ==================================

                watchlist_ids = [
                    item["tmdb_id"]
                    for item in (
                        st.session_state.watchlist
                    )
                ]

                if movie_id in watchlist_ids:

                    if st.button(
                        "💔 Remove from Watchlist",
                        use_container_width=True
                    ):

                        st.session_state.watchlist = [
                            item
                            for item in (
                                st.session_state.watchlist
                            )
                            if item["tmdb_id"] != movie_id
                        ]

                        st.rerun()

                else:

                    if st.button(
                        "❤️ Add to Watchlist",
                        use_container_width=True
                    ):

                        st.session_state.watchlist.append(
                            {
                                "tmdb_id": movie_id,
                                "title": details.get(
                                    "title",
                                    selected_movie
                                )
                            }
                        )

                        st.rerun()

                st.write("")

                # ==================================
                # RECOMMENDATIONS
                # ==================================

                if st.button(
                    "🤖 Get Recommendations",
                    use_container_width=True
                ):

                    try:

                        if "title" not in movies.columns:

                            st.error(
                                "❌ ML dataset is missing "
                                "the title column."
                            )

                        elif selected_movie in (
                            movies["title"].values
                        ):

                            if selected_movie not in (
                                st.session_state
                                .recommendation_history
                            ):

                                (
                                    st.session_state
                                    .recommendation_history
                                    .insert(
                                        0,
                                        selected_movie
                                    )
                                )

                            st.session_state.page = (
                                "recommendations"
                            )

                            st.rerun()

                        else:

                            st.error(
                                "This movie is not "
                                "available in our "
                                "ML dataset."
                            )

                    except Exception as error:

                        print(
                            f"Recommendation validation "
                            f"error: {error}",
                            flush=True
                        )

                        st.error(
                            "❌ Unable to prepare "
                            "recommendations."
                        )

            st.divider()

            if st.button(
                "← Back to Search Results"
            ):

                st.session_state.page = (
                    "search_results"
                )

                st.rerun()


# ==========================================================
# WATCHLIST PAGE
# ==========================================================

elif st.session_state.page == "watchlist":

    st.markdown(
        '<div class="section-title">'
        '❤️ My Watchlist'
        '</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.watchlist:

        st.markdown(
            """
            <div class="empty-state">
                <h3>❤️ Your watchlist is empty</h3>
                <p>
                    Add movies you want to watch
                    later.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🔎 Search Movies",
            use_container_width=True
        ):

            st.session_state.page = "search"

            st.session_state.last_search = ""

            st.rerun()

    else:

        columns = st.columns(3)

        for i, item in enumerate(
            st.session_state.watchlist
        ):

            with columns[i % 3]:

                movie_result = get_movie_details(
                    item["tmdb_id"]
                )

                if not movie_result["success"]:

                    st.warning(
                        f"Unable to load "
                        f"{item['title']}."
                    )

                    continue

                details = movie_result["details"]

                st.markdown(
                    '<div class="movie-card">',
                    unsafe_allow_html=True
                )

                poster_url = get_poster(
                    details.get(
                        "poster_path"
                    ),
                    "w342"
                )

                if poster_url:

                    st.image(
                        poster_url,
                        use_container_width=True
                    )

                else:

                    st.info(
                        "🖼️ Poster unavailable"
                    )

                st.markdown(
                    f'<div class="movie-title">'
                    f'🎬 '
                    f'{details.get("title", item["title"])}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="movie-info">'
                    f'⭐ '
                    f'{details.get("vote_average", 0):.1f}/10'
                    f'</div>',
                    unsafe_allow_html=True
                )

                release_date = details.get(
                    "release_date",
                    ""
                )

                if release_date:

                    st.markdown(
                        f'<div class="movie-info">'
                        f'📅 {release_date[:4]}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                if st.button(
                    "🎬 View Movie",
                    key=f"watch_view_{item['tmdb_id']}",
                    use_container_width=True
                ):

                    st.session_state.selected_movie = (
                        details.get(
                            "title",
                            item["title"]
                        )
                    )

                    st.session_state.selected_tmdb_id = (
                        item["tmdb_id"]
                    )

                    st.session_state.page = (
                        "details"
                    )

                    st.rerun()

                if st.button(
                    "🗑️ Remove",
                    key=f"watch_remove_{item['tmdb_id']}",
                    use_container_width=True
                ):

                    st.session_state.watchlist = [
                        movie
                        for movie in (
                            st.session_state.watchlist
                        )
                        if movie["tmdb_id"]
                        != item["tmdb_id"]
                    ]

                    st.rerun()

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

    if st.button(
        "← Back to Home"
    ):

        st.session_state.page = "home"

        st.rerun()


# ==========================================================
# HISTORY PAGE
# ==========================================================

elif st.session_state.page == "history":

    st.markdown(
        '<div class="section-title">'
        '🕘 Search & Recommendation History'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "### 🔎 Search History"
    )

    if st.session_state.search_history:

        for search in (
            st.session_state.search_history
        ):

            st.markdown(
                f'<div class="history-item">'
                f'🔎 {search}'
                f'</div>',
                unsafe_allow_html=True
            )

    else:

        st.info(
            "No search history yet."
        )

    st.divider()

    st.markdown(
        "### 🤖 Recommendation History"
    )

    if st.session_state.recommendation_history:

        for movie in (
            st.session_state.recommendation_history
        ):

            st.markdown(
                f'<div class="history-item">'
                f'🎬 {movie}'
                f'</div>',
                unsafe_allow_html=True
            )

    else:

        st.info(
            "No recommendation history yet."
        )

    st.divider()

    if st.button(
        "🗑️ Clear History",
        use_container_width=True
    ):

        st.session_state.search_history = []

        st.session_state.recommendation_history = []

        st.rerun()

    st.write("")

    if st.button(
        "← Back to Home"
    ):

        st.session_state.page = "home"

        st.rerun()


# ==========================================================
# RECOMMENDATIONS PAGE
# ==========================================================

elif st.session_state.page == "recommendations":

    selected_movie = (
        st.session_state.selected_movie
    )

    st.markdown(
        '<div class="section-title">'
        '✨ Movies You May Like'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        f"Because you selected "
        f"**{selected_movie}**"
    )

    try:

        with st.spinner(
            "🤖 Finding movies for you..."
        ):

            recommendations = recommend_movies(
                selected_movie,
                6
            )

    except Exception as error:

        print(
            f"ML recommendation error: {error}",
            flush=True
        )

        st.error(
            "❌ Unable to generate "
            "recommendations right now."
        )

        st.info(
            "Please try another movie."
        )

        recommendations = []


    if not recommendations:

        st.warning(
            "No recommendations are available "
            "for this movie."
        )

    else:

        print(
            f"\nRecommendations for: "
            f"{selected_movie}\n",
            flush=True
        )

        for i, movie in enumerate(
            recommendations,
            start=1
        ):

            try:

                print(
                    f"{i}. {movie['title']} "
                    f"(Match: "
                    f"{movie['similarity']:.2%})",
                    flush=True
                )

            except Exception:

                print(
                    f"{i}. Recommendation "
                    f"information unavailable",
                    flush=True
                )

        columns = st.columns(3)

        for i, movie in enumerate(
            recommendations
        ):

            with columns[i % 3]:

                st.markdown(
                    '<div class="movie-card">',
                    unsafe_allow_html=True
                )

                movie_id = movie.get(
                    "movie_id"
                )

                details = None

                if movie_id is not None:

                    movie_result = (
                        get_movie_details(
                            movie_id
                        )
                    )

                    if movie_result["success"]:

                        details = (
                            movie_result["details"]
                        )

                if details:

                    poster_url = get_poster(
                        details.get(
                            "poster_path"
                        ),
                        "w342"
                    )

                    if poster_url:

                        st.image(
                            poster_url,
                            use_container_width=True
                        )

                    else:

                        st.info(
                            "🖼️ Poster unavailable"
                        )

                else:

                    st.info(
                        "🖼️ Poster unavailable"
                    )

                movie_title = movie.get(
                    "title",
                    "Unknown Movie"
                )

                st.markdown(
                    f'<div class="movie-title">'
                    f'🎬 {movie_title}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                try:

                    rating = float(
                        movie.get(
                            "rating",
                            0
                        )
                    )

                    st.markdown(
                        f'<div class="movie-info">'
                        f'⭐ {rating:.1f}/10'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                except Exception:

                    st.markdown(
                        '<div class="movie-info">'
                        '⭐ Rating unavailable'
                        '</div>',
                        unsafe_allow_html=True
                    )

                release_year = movie.get(
                    "release_year",
                    ""
                )

                if release_year:

                    st.markdown(
                        f'<div class="movie-info">'
                        f'📅 {release_year}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                genres = movie.get(
                    "genres",
                    ""
                )

                if genres:

                    genre_text = str(
                        genres
                    ).replace(
                        " ",
                        " • "
                    )

                    st.markdown(
                        f'<div class="movie-info">'
                        f'🎭 {genre_text}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                try:

                    similarity = float(
                        movie.get(
                            "similarity",
                            0
                        )
                    )

                    st.markdown(
                        f'<div class="match-badge">'
                        f'🎯 '
                        f'{similarity:.0%} Match'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                except Exception:

                    pass

                reasons = movie.get(
                    "reasons",
                    []
                )

                if reasons:

                    st.markdown(
                        '<div class="reason-box">'
                        '<div class="reason-title">'
                        '💡 Why recommended?'
                        '</div>',
                        unsafe_allow_html=True
                    )

                    for reason in reasons:

                        st.markdown(
                            f'<div class="reason-item">'
                            f'✓ {reason}'
                            f'</div>',
                            unsafe_allow_html=True
                        )

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

    st.write("")

    if st.button(
        "← Search Another Movie",
        use_container_width=True
    ):

        st.session_state.page = "search"

        st.session_state.last_search = ""

        st.rerun()


# ==========================================
# TMDB ATTRIBUTION
# ==========================================

st.divider()

st.caption(
    "🎬 Movie data and images provided by TMDB."
)