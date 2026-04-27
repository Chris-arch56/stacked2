import streamlit as st
import requests

API_URL = "https://restful-inlh.onrender.com"

st.set_page_config(page_title="Movie Frontend", page_icon="🎬")

st.title("Movie Database Frontend")
st.write("This frontend connects to my FastAPI + Supabase movie backend.")

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
    director = st.text_input("Director")
    genre = st.text_input("Genre")
    description = st.text_area("Description")
    poster = st.file_uploader("Upload Poster Image", type=["jpg", "jpeg", "png"])

    if st.button("Add Movie"):
        if poster is None:
            st.error("Please upload a poster image.")
        else:
            data = {
                "title": title,
                "director": director,
                "genre": genre,
                "description": description
            }

            files = {
                "poster": (poster.name, poster.getvalue(), poster.type)
            }

            response = requests.post(f"{API_URL}/movies", data=data, files=files)

            if response.status_code == 200:
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
    director = st.text_input("New Director")
    genre = st.text_input("New Genre")
    description = st.text_area("New Description")

    if st.button("Update Movie"):
        data = {}

        if title:
            data["title"] = title
        if director:
            data["director"] = director
        if genre:
            data["genre"] = genre
        if description:
            data["description"] = description

        response = requests.patch(f"{API_URL}/movies/{movie_id}", data=data)

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
