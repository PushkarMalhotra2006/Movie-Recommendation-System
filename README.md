# 🎬 Movie Recommendation System

A full-stack AI-powered movie recommendation web application built using **FastAPI**, **Streamlit**, **TF-IDF based content filtering**, and the **TMDB API**.

The project combines:

* content-based movie recommendations using cosine similarity
* live movie metadata from TMDB
* a responsive Streamlit frontend
* a FastAPI backend with multiple recommendation endpoints

The application allows users to:

* search movies with live suggestions
* explore trending/popular movies
* view movie details
* get similar movie recommendations
* discover genre-based recommendations

---

## 🚀 Live Demo

### Frontend (Streamlit)

https://movie-recommendation-system-by-pushkar.streamlit.app/

### Backend API (Render)

https://movie-recommendation-system-sn0l.onrender.com

---

# 📌 Features

* 🔎 Movie search with dynamic suggestions
* 🎬 Trending / Popular / Upcoming / Top Rated movie feeds
* 🧠 TF-IDF based content recommendation system
* 🎭 Genre-based recommendations using TMDB Discover API
* 🖼️ Posters, backdrops, ratings, and metadata from TMDB
* ⚡ FastAPI backend with async API handling
* 🎨 Responsive Streamlit frontend
* 🔄 Client-server architecture
* 📦 Pickle-based precomputed recommendation system
* ☁️ Deployment using Render + Streamlit Cloud

---

# 🧠 Recommendation System

The recommendation engine uses:

* **TF-IDF Vectorization**
* **Cosine Similarity**

Movies are recommended based on textual similarity between movie metadata/tags.

The backend computes similarity scores locally using the precomputed TF-IDF matrix and returns the most relevant movies.

---

# 🏗️ Project Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
TF-IDF Recommendation Engine
  ↓
TMDB API
```

---

# ⚙️ Tech Stack

## Frontend

* Python
* Streamlit

## Backend

* FastAPI
* Uvicorn
* HTTPX

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* NumPy
* Pandas

## Deployment

* Render
* Streamlit Cloud

## External APIs

* TMDB API

---

# 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py                 # Streamlit frontend
├── main.py                # FastAPI backend
├── movies.ipynb           # ML training + preprocessing
│
├── df.pkl
├── tfidf.pkl
├── tfidf_matrix.pkl
├── indices.pkl
│
├── requirements.txt
├── .env
└── README.md
```

---

# 🔥 Backend Workflow

1. User searches/selects a movie
2. Frontend sends request to FastAPI backend
3. Backend fetches movie details from TMDB
4. TF-IDF similarity model computes recommendations
5. Backend enriches results with TMDB posters/details
6. JSON response returned to frontend
7. Streamlit renders movie cards and recommendations

---
# Main API End Points

| Endpoint              | Description                    |
| --------------------- | ------------------------------ |
| `/home`               | Home feed movies               |
| `/tmdb/search`        | Search movies                  |
| `/movie/id/{tmdb_id}` | Movie details                  |
| `/recommend/tfidf`    | TF-IDF recommendations         |
| `/recommend/genre`    | Genre-based recommendations    |
| `/movie/search`       | Combined recommendation bundle |

---

# ⚠️ Challenges Faced

* Understanding frontend ↔ backend communication
* Handling async API requests in FastAPI
* Parsing different TMDB response structures
* Managing recommendation fallbacks safely
* Integrating ML recommendations with real-time TMDB data
* Deployment/networking issues with external APIs

---

# Author

Pushkar
