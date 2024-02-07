import requests
from fastapi import FastAPI,Request
import json
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000/",
    "http://localhost:3000",
    "https://logika-movie-app.vercel.app",
    "https://logika-movie-lx14kxs1i-twkesqw.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
base_url = "https://api.themoviedb.org/3/movie/"
API_KEY = "4e44d9029b1270a757cddc766a1bcb63"
lang = "uk-UA"

def getFilms(type,page):
    url = f"{base_url}/{type}?api_key={API_KEY}&language={lang}&page={page}"
    response = requests.get(url)
    return response.json()

def getFilmById(id):
    url = f"{base_url}/{id}?api_key={API_KEY}&language={lang}"
    response = requests.get(url)
    return response.json()

def getTrailerById(id):
    lang = "uk-UA"
    url = f"{base_url}/{id}/videos?api_key={API_KEY}&language={lang}"
    response = requests.get(url)

    if len(response.json()["results"]) == 0:
        lang = "en-US"
        url = f"{base_url}/{id}/videos?api_key={API_KEY}&language={lang}"
        response = requests.get(url)

    return response.json()["results"][0]["key"]

def searchFilmByTitle(title):
    title = title.split("_")
    url = f"https://api.themoviedb.org/3/search/movie?query={'+'.join(title)}&api_key={API_KEY}&language={lang}"
    response = requests.get(url)
    return response.json()

def trendingSixFilms():
    url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}&language={lang}"
    response = requests.get(url)
    return response.json()["results"][0:8]


@app.get("/movies/{type}/{page}")
def popular(type,page):
    return getFilms(type,page)

@app.get("/movie/{id}")
def movie(id: int):
    return getFilmById(id)


@app.get("/trailers/{id}")
def trailer(id: int):
    return getTrailerById(id)


@app.get("/search/{title}")
def search(title:str):
    return searchFilmByTitle(title)

@app.get("/trending")
def trending():
    return trendingSixFilms()







