import requests
from fastapi import APIRouter

from var import *


router = APIRouter()
def getFilms(type,page):
    url = f"{base_url}/{type}?api_key={API_KEY}&language={lang}&page={page}"
    response = requests.get(url)
    return response.json()

def getFilmById(id):
    url = f"{base_url}/{id}?api_key={API_KEY}&language={lang}"
    response = requests.get(url)
    return response.json()

@router.get("/movies/{type}/{page}")
def popular(type,page):
    return getFilms(type,page)

@router.get("/movie/{id}")
def movie(id: int):
    return getFilmById(id)