import streamlit as st
import pickle
import requests
import base64

# Function to convert local image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set background image
def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .main > div {{
        padding-top: 2rem;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        margin: 1rem;
    }}

    .stSelectbox > div > div > div {{
        background-color: rgba(255, 255, 255, 0.9);
    }}

    .stButton > button {{
        background-color: rgba(255, 87, 51, 0.8);
        color: white;
        border: none;
        border-radius: 5px;
        backdrop-filter: blur(5px);
    }}

    .stButton > button:hover {{
        background-color: rgba(255, 87, 51, 1);
    }}

    .sidebar .sidebar-content {{
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(10px);
    }}

    h1, h2, h3 {{
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }}

    .stText {{
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Apply background (make sure background.jpg is in your project folder)
try:
    set_background('background.jpg')
except FileNotFoundError:
    st.warning("Background image 'background.jpg' not found. Please add it to your project folder.")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarty.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommendation System")
st.sidebar.header("Movie Recommendation System")
st.sidebar.subheader("About")
st.sidebar.markdown(
    """
     This :blue[**Movie Recommendation System**] is Simple Recommendation System train on Raw file data.
     And recommend only that movies on which its **model train**, so if you enter any movie which are not 
     in its file it did not recommend anymore.
    """
)
st.sidebar.subheader("How to use")
st.sidebar.markdown(
    """
    :blue[**1.**] Select Movie from Drop Menu.

    :blue[**2.**] And Then Show Recommend

    :blue[**3.**] You will show top 5 Movies similar as your selected movie
    """
)
st.sidebar.subheader("Contact us")
st.sidebar.markdown(
    """
    **Email:** hasiraza511@gmail.com

    **Linkedin:** https://www.linkedin.com/in/muhammad-haseeb-raza-71987a366/

    **github:** https://github.com/hasiraza
    """
)

selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:  # Changed back to 6 to show 5 movies
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])