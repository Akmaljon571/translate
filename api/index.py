import requests

from database.connect import get_one


def language_api(text, id):
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"
    get_func = get_one(id)
    querystring = {"langpair": f"{get_func['lang1']}|{get_func['lang2']}", "q": text, "mt": "1", "onlyprivate": "0", "de": "a@b.c"}

    headers = {
        "X-RapidAPI-Key": "f5d602a575msha11f03335de9104p12bf91jsn5e0242ad517f",
        "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

