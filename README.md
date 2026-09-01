# 🎬 CineMatch

### Discover your next favourite movie 🍿

CineMatch is an ML-based movie recommendation system built using Python and Streamlit.

It recommends movies based on similarity between movies in the ML dataset and provides additional movie information using the TMDB API.

---

## ✨ Features

- 🎬 Machine Learning movie recommendations
- 🔎 Movie search
- 🎯 ML-based similarity matching
- 📊 Match percentage
- 💡 "Why recommended?" explanations
- 🖼️ TMDB movie posters
- 📖 Movie details and overview
- ❤️ Personal watchlist
- 🕘 Search history
- 🤖 Recommendation history
- ⚡ Cached TMDB requests for faster loading
- 🛡️ Error handling
- 📱 Responsive UI
- 🏠 Featured movies on homepage

---

## 🧠 Machine Learning

CineMatch uses a content-based recommendation approach.

The recommendation system compares movie information from the dataset and calculates similarity between movies.

The system then returns movies with the highest similarity scores.

### Recommendation Flow

```text
User selects a movie
        ↓
ML model analyzes movie
        ↓
Similarity calculation
        ↓
Top similar movies
        ↓
Match percentage
        ↓
Recommended movies