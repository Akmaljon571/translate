import requests

url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"

querystring = {"langpair": "en|it", "q": "Hello World!", "mt": "1", "onlyprivate": "0", "de": "a@b.c"}

headers = {
    "X-RapidAPI-Key": "f5d602a575msha11f03335de9104p12bf91jsn5e0242ad517f",
    "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
