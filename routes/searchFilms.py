import requests
from var import *
from fastapi import APIRouter

router = APIRouter()
def searchFilmByTitle(title):
    title = title.split("_")
    url = f"https://api.themoviedb.org/3/search/movie?query={'+'.join(title)}&api_key={API_KEY}&language={lang}"
    response = requests.get(url)
    return response.json()


@router.get("/search/{title}")
def search(title:str):
    return searchFilmByTitle(title)