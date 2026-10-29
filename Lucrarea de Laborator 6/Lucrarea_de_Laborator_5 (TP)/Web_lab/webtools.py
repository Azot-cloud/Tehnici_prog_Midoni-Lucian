#Laborator: funcții, metode și importuri pe web
import json

# Student: <Midoni Lucian>


BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10  # secunde #


# Constanta

DEFAULT_HEADERS = {"User-Agent": "WebLab-<Midoni Lucian>"}


# Exercitiul 17


import time
import requests

time.sleep(1)

raspuns_17 = requests.get("http://cybercor.org", timeout=TIMEOUT)

print("Istoricul rederictionarii:")

for ist in raspuns_17.history:
    print(f"Cod stare: {ist.status_code} URL: {ist.url}")

print("URL final:", raspuns_17.url)
print("Codul de stare al adresei finale:", raspuns_17.status_code)



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



#Exercitiul 30

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

# Exercitiul 38


from urllib.parse import urljoin, urlparse


def split_links(links: list, domain: str):
    interne = []
    externe = []
    target_netloc = urlparse(domain).netloc

    for link in links:
        full_url = urljoin(domain, link)
        link_netloc = urlparse(full_url).netloc

        if link_netloc == target_netloc:
            interne.append(full_url)
        else:
            externe.append(full_url)

    return interne, externe
response = requests.get(BASE_URL, timeout=TIMEOUT)


legaturi_interne, legaturi_externe = split_links("https://cybercor.org", BASE_URL)

print(f"Legaturi interne:{len(legaturi_interne)}")
for link in legaturi_interne:
    print(link)

print(f"Legaturi externe:{len(legaturi_externe)}")
for link in legaturi_externe:
    print(link)


# Exercitiul 42

import socket


def resolve(hostname):
    return socket.gethostbyname(hostname)

url_test = "cybercor.org"

print("IP adress a Serverului:", url_test)
print(resolve(url_test))



# Exercitiul 43



import socket
import ssl
from datetime import datetime

def cert_days_left(hostname):

    context = ssl.create_default_context()
    sock = socket.create_connection((hostname, 443))
    wrap = context.wrap_socket(sock, server_hostname=hostname)

    data_text = wrap.getpeercert()["notAfter"]

    expirare_secunde = ssl.cert_time_to_seconds(data_text)

    expirare = datetime.fromtimestamp(expirare_secunde)

    timp_ramas = expirare - datetime.now()

    return timp_ramas

url_test = "cybercor.org"
zile  = cert_days_left(url_test)
print(f"Certificatul pentru {url_test} mai este valabil {zile} zile.")


# --------------------------------------------------------------------------

# Exercitiul 50
import re
import requests
import json

def site_report(url):
    print(f"\n Se accesează {url}")
    raspuns = fetch(url)

    print("\n Se extrage titlul")
    titlu = get_title(raspuns.text)

    print("Se verifică headerele de securitate...")
    sec_headers = security_headers(url)

    print("\n Se  verifica rutele")
    rute = ["/", "/robots.txt", "/sitemap.xml"]
    status_rute = check_paths(url, rute)

    print("\n Se verifică IP-ul și certificatul")
    domeniu = urlparse(url).netloc
    adresa_ip = resolve(domeniu)
    zile_certificat = cert_days_left(domeniu)

    print("Se verifică fișierul robots.txt...")
    text_robots = fetch_robots(url)
    cai_interzise = disallowed_paths(text_robots)

    print("[7/8] Se extrag și se sortează legăturile (linkurile)...")
    toate_linkurile = re.findall(r'href=["\'](.*?)["\']', raspuns.text)
    legaturi_interne, legaturi_externe = split_links(toate_linkurile, url)

    print("Generarea Raportului")

    raport = {
        "Site_url": url,
        "Cod de stare": raspuns.status_code,
        "Titlul paginii": titlu,
        "Adressa IP": url_test,
        "Rederictionari":[ist.status_code for ist in raspuns.history],
        "security_headers": sec_headers,
        "Certificat": zile,
        "Legaturi": [legaturi_interne,legaturi_externe],
        "Cai interzise": cai_interzise,
        "Salvat in report.json": True
    }

    print(" === RAPORT FINAL === ")
    print(json.dumps(raport,indent=4))

    with open("report.json", "w") as fisier_json:
        json.dump(raport, fisier_json, indent=4)

    print("\n Raport creat cu succes")

#Ex 46
if __name__ == "__main__":

    print("Autotest:", get_status("https://cybercor.org"))




