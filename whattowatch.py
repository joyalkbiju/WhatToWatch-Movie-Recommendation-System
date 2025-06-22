import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5f98b4261540314891e93f8e3663f284'.format(id))
    data=response.json()
    
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_ind=movies[movies['title']==movie].index[0]
    distances=similarity[movie_ind]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:7]
    recommended_movies=[]
    posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return recommended_movies,posters


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('WhatToWatch')

selected_movie=st.selectbox(
    'Select Your Favourite Movie',
    movies['title'].values
)

if st.button('Recommend Movies'):
    names,posters=recommend(selected_movie)


   




    for i in range(0, 6, 2):
        col1, spacer, col2 = st.columns([3, 0.5, 3])  

        with col1:
            st.image(posters[i], use_column_width=True)
            st.write(f"**{names[i]}**")


        with col2:
            st.image(posters[i+1], use_column_width=True)
            st.write(f"**{names[i+1]}**")
    