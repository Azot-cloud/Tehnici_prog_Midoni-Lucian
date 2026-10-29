#Laborator: funcții, metode și importuri pe web

# Student: <Midoni Lucian>


BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10  # secunde #




# Exercitiul 21

import time
import requests

def fetch(url):
    """Trimite o cerere GET către url și returnează obiectul"""
    time.sleep(1)
    response = requests.get(url, timeout=TIMEOUT)
    return response

raspuns = fetch(BASE_URL)
print("Cod de stare: ",raspuns.status_code)




# Exercitiul 22

import time
import requests


def get_status(url):
    """Returnează doar codul de stare HTTP pentru adresa url."""
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code

apeluri = ["/","/robots.txt","/sitemap.xml"]

for apel in apeluri:
    time.sleep(1)
    url_complet = BASE_URL + apel
    stare = get_status(url_complet)
    print(f"Apelare: {apel:<13} | Cod de stare: {stare}")




# Exercitiul 23

import time
import requests

def fetch(url, timeout=10):
    time.sleep(1)
    response = requests.get(url, timeout=timeout)
    return response

rasp1 = fetch(BASE_URL)
print("Afisarea cu valoare implicita 10s:", rasp1.status_code)

rasp2 = fetch(BASE_URL, timeout=3)
print("Afisarea cu valoare implicita 3s:", rasp2.status_code)



# Exercitiul 24

import time
import requests

def get_title(html):
    """Primeste un sir html și returneaza titlul paginii."""
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    titlu = html[start:end].strip()
    return titlu

time.sleep(1)
response = requests.get(BASE_URL, timeout=TIMEOUT)

titlu_pagina = get_title(response.text)
print("Titlul paginii este:", titlu_pagina)




# Exercitiul 25

import requests

def get_title(html):
    """Docstring"""
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    titlu = html[start:end].strip()
    return titlu

help(get_title)




# Exercitiul 26

import time
import requests

def get_status(url: str) -> int:
    time.sleep(1)
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code
try:
    print(get_status(123))
except:
    print("Error: Adnotarilede tip str > int  nu se opresc")

# La rularea programului adnotarile nu se opresc




# Exercitiul 27

import time
import requests

def page_exists(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=TIMEOUT)
        return response.status_code == 200

    except requests.RequestException:
        return False

url_invalid = "https://this-domain-does-not-exist.invalid"
print("Exista domeniul invalid?:", page_exists(url_invalid))




# Exercitiul 28

import time
import requests

def check_paths(base, paths):
    """Verifică o listă de căi pentru un URL de bază și returnează un dicționar {path: status_code}."""
    rezultate = {}

    for path in paths:
        time.sleep(1)
        url_complet = base + path
        response = requests.get(url_complet, timeout=TIMEOUT)
        rezultate[path] = response.status_code

    return rezultate

lista = ["/", "/robots.txt", "/sitemap.xml"]
dicționar_rezultat = check_paths(BASE_URL, lista)

print("Rezultat dicționar:", dicționar_rezultat)



# Exercitiul 29

import time
import requests

def get_header(url,name,default="lipseste"):
    """Returnează valoarea unui antet."""
    time.sleep(1)
    response = requests.get(url,timeout=TIMEOUT)
    return response.headers.get(name, default)

antet = get_header(BASE_URL, name="Server")
print("Antetului serverului este:", antet)




# Exercitiul 30

import time
import requests

def security_headers(url: str) -> dict:
    """Verifică prezența celor 5 antete de securitate și returnează un dicționar"""
    lista = ["Strict-Transport-Security",
             "Content-Security-Policy",
             "X-Frame-Options",
             "X-Content-Type-Options",
             "Referrer-Policy"
             ]

    time.sleep(1)
    response = requests.get(url, timeout=TIMEOUT)
    rezultat = {}
    for antet in lista:
        rezultat[antet] = antet in response.headers

    return rezultat

statut_securitate = security_headers(BASE_URL)
print("Prezența antetelor de securitate:\n", statut_securitate)


# Exercitiul 31

import time
import requests


def score_headers(results: dict) -> str:
    """Primește dicționarul de rezultate"""
    prezente = sum(results.values())
    total = len(results)
    return f"{prezente}/{total}"

scor = score_headers(security_headers(BASE_URL))
print("Scorul antetelor de securitate:", scor)



# Exercitiul 32

import time
import requests

def fetch_robots(base):
    """Descarcă conținutul /robots.txt sau returnează None."""
    time.sleep(1)  # Pauza de rețea obligatorie
    try:
        url = base.rstrip("/") + "/robots.txt"
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException:
        return None

def disallowed_paths(robots_text):
    """Extrage căile interzise dintr-un text robots.txt."""
    if not robots_text:
        return []

    cai = []
    for line in robots_text.splitlines():
        line = line.strip()
        if line.startswith("Disallow:"):
            cale = line[9:].strip()
            if cale:
                cai.append(cale)
    return cai

# Testare:
text = fetch_robots(BASE_URL)
rezultat = disallowed_paths(text)
print("Căi interzise:", rezultat)



# Exercitiul 33

import time
import requests

def response_times(*urls: str) -> dict:
    """Măsoară timpul de răspuns pentru oricâte URL-uri primite ca argumente variable."""
    rezultate = {}

    for url in urls:
        time.sleep(1)
        try:
            response = requests.get(url, timeout=TIMEOUT)

            timp_secunde = response.elapsed.total_seconds()
            rezultate[url] = timp_secunde
        except requests.RequestException:
            rezultate[url] = None

    return rezultate

rezultat_timp = response_times(BASE_URL, BASE_URL + "/robots.txt")
print("Timpi de răspuns:", rezultat_timp)



# Exercitiul 34

import time
import requests


def log(message, **details):

    parti = [message]

    for key, value in details.items():
        parti.append(f"{key}={value}")

        print(" | ".join(parti))

log("verificat", url=BASE_URL, status=200)
log("eroare rețea", url="https://invalid.url", code=404, retry=False)