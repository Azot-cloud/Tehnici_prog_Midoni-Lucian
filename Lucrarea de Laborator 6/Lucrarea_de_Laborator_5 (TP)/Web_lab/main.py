#Laborator: funcții, metode și importuri pe web


# Student: <Midoni Lucian>


BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10  # secunde



# Exercitiul 44

import webtools
webtools.get_title(webtools.fetch(BASE_URL).text)


# Exercitiul  45

import webtools
from webtools import get_title, security_headers

# Raspuns:
# In caz ca main.py va avea  functie proprie get_title()
# aceasta isi va da overwrite la afisare in terminal.



# Exercitiul 46  Realizat in webtools.py



# Atunci cand executam python webtools.py se seteaza automat variabila __name__ la valoarea __main__
# Dar atunci cand executam fisierul main.py fisierul webtools.py este importat, prin urmare
# variabila __name__ devine webtools iar conditia devine falsa si codul este ignorat.



# Exercitul 47

from webtools import fetch, get_title, DEFAULT_HEADERS
print("Constanta DEFAULT_HEADERS este:", DEFAULT_HEADERS)


# Exercitiul 48

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="https://cybercor.org")
args = parser.parse_args()

print(f"Url-ul este: {args.url}")


# Exercitiul 49

import csv
from datetime import datetime
from webtools import check_paths

rezultate = check_paths(base=BASE_URL, paths=["/", "/robots.txt", "/sitemap.xml"])

with open("report.csv", mode="w", newline="") as fisier:
    writer = csv.writer(fisier)
    writer.writerow(["path", "status", "checked_at"])

    for path, status in rezultate.items():

        checked_at = datetime.now().isoformat()
        writer.writerow([path, status, checked_at])
print(rezultate)


 # Exercitiul 50

import argparse
from webtools import site_report

parser = argparse.ArgumentParser()
parser.add_argument("url",help="https://cybercor.org")
args = parser.parse_args()

site_report(args.url)


# Extra (Beatifulsoup4)

from bs4 import BeautifulSoup


def get_title(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    print(soup)
    return None





def extract_links(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    return [a["href"] for a in soup.find_all("a", href=True)]