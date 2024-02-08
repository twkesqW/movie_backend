import requests
from var import *
from fastapi import APIRouter
router = APIRouter()

def trendingSixFilms():
    url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}&language={lang}"
    response = requests.get(url)
    return response.json()["results"][0:8]




@router.get("/trending")
def trending():
    return trendingSixFilms()
