import streamlit as st
import requests


# Page title
st.title("🎬 TMDB Connection Test")


# Get token securely
token = st.secrets["TMDB_ACCESS_TOKEN"]


# TMDB API
url = "https://api.themoviedb.org/3/search/movie"

headers = {
    "Authorization": f"Bearer {token}",
    "accept": "application/json"
}

params = {
    "query": "Avatar"
}


# Send request
response = requests.get(
    url,
    headers=headers,
    params=params
)


# Display status
st.write("Status code:", response.status_code)


if response.status_code == 200:

    data = response.json()

    st.success("✅ TMDB connection successful!")

    st.subheader("Movies found:")

    for movie in data["results"][:3]:

        st.write(
            f"🎬 {movie['title']}"
        )

        st.write(
            f"Poster path: {movie.get('poster_path')}"
        )

        st.divider()

else:

    st.error("❌ TMDB connection failed.")

    st.write(response.text)