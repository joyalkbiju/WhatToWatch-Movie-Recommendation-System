# 🎬 WhatToWatch – Movie Recommendation System

**WhatToWatch** is a personalized movie recommendation web application built using **Streamlit** and powered by content-based filtering. Leveraging The Movie Database (TMDb) API, it provides intelligent recommendations along with high-quality movie posters in a clean, user-friendly interface.

---

## 📌 Overview

The app allows users to select a movie they like and receive a curated list of similar titles. It uses cosine similarity over precomputed feature vectors to suggest top 6 similar movies and displays their posters using TMDb.

---

## 🚀 Features

- 🎯 **Content-Based Filtering**: Recommends similar movies based on your favorite
- 🖼️ **Poster Integration**: Fetches high-resolution posters using TMDb API
- 💡 **Interactive UI**: Streamlit-powered app with intuitive controls
- 🧱 **Responsive Two-Column Layout**: Visually appealing display with clean spacing

---

## 🗃️ Project Structure

```
what-to-watch/
│
├── whattowatch.py          # Streamlit application
├── movie.ipynb             # Jupyter notebook for feature generation/modeling
├── movies_dict.pkl         # Dictionary of movie metadata
├── similarity.pkl          # Cosine similarity matrix
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## 🛠️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/what-to-watch.git
cd what-to-watch
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run whattowatch.py
```

The app will open in your default web browser.

---

## 🔑 API Key Configuration

The application uses the TMDb API to fetch movie posters. Replace the placeholder API key in `whattowatch.py` with your own:

```python
response = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=YOUR_API_KEY')
```

📌 Get your free API key from: [TMDb API](https://www.themoviedb.org/documentation/api)

---



## 📦 Dependencies

- `streamlit`
- `pandas`
- `requests`
- `pickle`
- `scikit-learn`
- `nltk`

Ensure these are listed in your `requirements.txt`.

---

## 📖 License

This project is intended for educational and personal use. Respect TMDb's API usage policies when deploying publicly.

---




