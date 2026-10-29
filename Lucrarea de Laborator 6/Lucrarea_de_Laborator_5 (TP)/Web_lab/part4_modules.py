#Laborator: funcții, metode și importuri pe web
import ssl
from urllib.parse import urlparse

import requests

# Student: <Midoni Lucian>


BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10  # secunde #


# Exercitiul 35

import urllib.parse

url = "https://cybercor.org/path?x=1#top"
parsed = urllib.parse.urlparse(url)

print("Scheme:", parsed.scheme)
print("Netloc:", parsed.netloc)
print("Path:", parsed.path)
print("Query:", parsed.query)
print("Fragment:", parsed.fragment)



# Exercitiul 36

import urllib.parse

BaseURL = "https://cybercor.org"

legaturi_relative = ["/about", "contact.html", "../index.html"]

for legatura in legaturi_relative:
    full_url = urllib.parse.urljoin(BaseURL, legatura)
    print(full_url)





# Exercitiul 37

import re
import requests

def extract_links(html: str) -> list:

    toate_legaturile = re.findall(r'href="([^"]+)"', html)
    legaturi_unice = []

    for link in toate_legaturile:
        if link not in legaturi_unice:
            legaturi_unice.append(link)

    return legaturi_unice

response = requests.get(BASE_URL, timeout=TIMEOUT)
links = extract_links(response.text)

print(f"Am gasit {len(links)} legături unice:\n")
for link in links:
    print(link)




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



# Exercitiul 39

import time
import requests
from html.parser import HTMLParser


class ImageFinder(HTMLParser):

    def __init__(self):
        super().__init__()

        self.images = []

    def handle_starttag(self, tag, attrs):
        # codul vostru aici
        if tag == "img":
            src = dict(attrs).get("src")
            if src is not None:
                self.images.append(src)

            print(self.handle_starttag(self.images,BASE_URL))
# #-------------------------------------------
test_html = """
<html><body>
  <img src="/logo.png" alt="Logo">
  <IMG SRC="poza.jpg">
  <img alt="imagine fără src">
  <img src="https://cdn.example.com/banner.webp" />
  <a href="/despre">Aceasta nu este o imagine</a>
</body></html>
"""

finder = ImageFinder()
finder.feed(test_html)
print(finder.images)

assert finder.images == [

    "/logo.png",
    "poza.jpg",
    "https://cdn.example.com/banner.webp",
], "Parserul nu a găsit exact imaginile așteptate"

print("Testul a trecut!")
#--------------------------------------------------
response = requests.get(BASE_URL, timeout=TIMEOUT)
time.sleep(1)

finder = ImageFinder()
finder.feed(response.text)

print(len(finder.images), "imagini găsite")
for src in finder.images:
    print(src)
# #_______________________________________
time.sleep(1)
response = requests.get(BASE_URL, timeout=TIMEOUT)

real_finder = ImageFinder()
real_finder.feed(response.text)

numar_parser = len(real_finder.images)
numar_brut = response.text.lower().count("<img")

if numar_parser == numar_brut:
    print("Numerele coincid")
else:
    print("Numerele diferă")



# Exercitiul 40

import hashlib
import requests
import time


def page_fingerprint(url):
    time.sleep(1)
    response = requests.get(url, timeout=TIMEOUT)
    return hashlib.sha256(response.content).hexdigest()

url_test = "https://cybercor.org"

print("Prima rulare: ", page_fingerprint(url_test))
time.sleep(1)
print("A doua rulare:", page_fingerprint(url_test))

# Rezultatele ar fi diferite atunci cand continutul paginii sar schimba




#Exercitiul 41

import time
import json
import requests

def test_json_headers():
    time.sleep(1)
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    file = open("headers.json", "w")
    json.dump(dict(response.headers), file, indent=2)
    file.close()

    file_citire = open("headers.json", "r")
    antete = antete = json.load(file_citire)
    file_citire.close()

    print(antete["Date"])

test_json_headers()




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







