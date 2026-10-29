import requests
from urllib3.util import request

BASE = "https://httpbin.org"

PATHS = ["/get", "/redirect/2", "/delay/1", "/status/404", "/delay/5"]

# Partea 1



# def search(params):
#     """GET pe /get cu parametri în URL; returnează parametrii primiți de server."""
#
#     r = request.get(BASE+ "/get", params=params)
#     return r.json["args"]
#
# def search_url(params):
#     """Returnează adresa completă construită de requests, cu tot cu parametri."""
#     r = request.get(BASE+"/get", params=params)
#     return r.url



# Partea 2  anteturi

# def fetch_with_agent(agent):
#     r = requests.get(BASE + "/headers", headers={"User-Agent": agent})
#     return r.jsons()["jsons"]
#
# def default_agent():
#     r = requests.get(BASE + "/headers")
#     return r.json()["headers"]["User-Agent"]



# Partea 3 trimiterea datelor


# def post_json(data):
#     r = requests.get(BASE + "/post", json=data)
#     return r.json()["json"]
#
# def post_form(data):
#     r = requests.post(BASE + "/post", data=data)
#     return r.json()["form"]



# Partea 4 coduri de stare


def describe_status(code):
    r = requests.get(f"{BASE}/status/{code}")
    if 200 <= r.status_code < 300:
        return 'succes'
    elif 400 <= r.status_code < 500:
        return 'eroare client'
    elif 500 <= r.status_code < 600:
        return 'eroare server'
    else:
        return 'altceva'


