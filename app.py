import streamlit as st
import requests

API_URL = "https://restful-in1h.onrender.com"

st.set_page_config(page_title="Movie Frontend", page_icon="🎬")

st.title("Movie Database Frontend")
st.write("This app connects to my REST API backend and lets users search, create, retrieve, update, and delete movies.")

menu = st.sidebar.selectbox(
    "Choose an action",
    ["Search Movies", "Create Movie", "Retrieve Movie", "Update Movie", "Delete Movie"]
)

if menu == "Search Movies":
    st.header("Search / View All Movies")

    if st.button("Load Movies"):
        response = requests.get(f"{API_URL}/movies")
        if response.status_code == 200:
            st.success("Movies loaded successfully.")
            st.write(response.json())
        else:
            st.error("Could not load movies.")
            st.write(response.text)

elif menu == "Create Movie":
    st.header("Create a New Movie")

    title = st.text_input("Movie Title")
    genre = st.text_input("Genre")
    year = st.number_input("Year", min_value=1800, max_value=2100, step=1)
    rating = st.text_input("Rating")

    if st.button("Add Movie"):
        new_movie = {
            "title": title,
            "genre": genre,
            "year": year,
            "rating": rating
        }

        response = requests.post(f"{API_URL}/movies", json=new_movie)

        if response.status_code == 200 or response.status_code == 201:
            st.success("Movie added successfully.")
            st.write(response.json())
        else:
            st.error("Movie was not added.")
            st.write(response.text)

elif menu == "Retrieve Movie":
    st.header("Retrieve One Movie")

    movie_id = st.number_input("Enter Movie ID", min_value=1, step=1)

    if st.button("Get Movie"):
        response = requests.get(f"{API_URL}/movies/{movie_id}")

        if response.status_code == 200:
            st.success("Movie found.")
            st.write(response.json())
        else:
            st.error("Movie not found.")
            st.write(response.text)

elif menu == "Update Movie":
    st.header("Update a Movie")

    movie_id = st.number_input("Movie ID to Update", min_value=1, step=1)
    title = st.text_input("New Movie Title")
    genre = st.text_input("New Genre")
    year = st.number_input("New Year", min_value=1800, max_value=2100, step=1)
    rating = st.text_input("New Rating")

    if st.button("Update Movie"):
        updated_movie = {
            "title": title,
            "genre": genre,
            "year": year,
            "rating": rating
        }

        response = requests.patch(f"{API_URL}/movies/{movie_id}", json=updated_movie)

        if response.status_code == 200:
            st.success("Movie updated successfully.")
            st.write(response.json())
        else:
            st.error("Movie was not updated.")
            st.write(response.text)

elif menu == "Delete Movie":
    st.header("Delete a Movie")

    movie_id = st.number_input("Movie ID to Delete", min_value=1, step=1)

    if st.button("Delete Movie"):
        response = requests.delete(f"{API_URL}/movies/{movie_id}")

        if response.status_code == 200:
            st.success("Movie deleted successfully.")
            st.write(response.json())
        else:
            st.error("Movie was not deleted.")
            st.write(response.text)
