from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import getFilms,getTrailer,getTrendingFilms,searchFilms
app = FastAPI()
app.include_router(getFilms.router)
app.include_router(getTrailer.router)
app.include_router(getTrendingFilms.router)
app.include_router(searchFilms.router)


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















