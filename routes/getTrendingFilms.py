import requests
from fastapi import APIRouter

from var import *

def getTrailerById(id):
    lang = "uk-UA"
    url = f"{base_url}/{id}/videos?api_key={API_KEY}&language={lang}"
    response = requests.get(url)

    if len(response.json()["results"]) == 0:
        lang = "en-US"
        url = f"{base_url}/{id}/videos?api_key={API_KEY}&language={lang}"
        response = requests.get(url)

    return response.json()["results"][0]["key"]

router = APIRouter()

@router.get("/trailers/{id}")
def trailer(id: int):
    return getTrailerById(id)