from dotenv import load_dotenv
import os

load_dotenv()
base_url = "https://api.themoviedb.org/3/movie/"
API_KEY = os.getenv("API_KEY")
lang = "uk-UA"