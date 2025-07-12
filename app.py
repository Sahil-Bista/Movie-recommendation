import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('Movies.pkl','rb'))
movies_list = movies['original_title'].values

def fetch_poster(movie_id):
    requests

def recommend(movie):
    movie_index = movies[movies['original_title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].original_title)
    return recommended_movies


similarity = pickle.load(open('Similarity.pkl','rb'))


st.title('Movie recommendor system')

selected_movie_name = st.selectbox(
    'Choose the kind of movie u want to watch',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


