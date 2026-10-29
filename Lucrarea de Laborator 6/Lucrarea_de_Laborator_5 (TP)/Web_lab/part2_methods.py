#Laborator: funcții, metode și importuri pe web

# Student: <Midoni Lucian>


BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10  # secunde #

# Exercitiul 9

import requests
response = requests.get(BASE_URL, timeout=TIMEOUT)

print(response.status_code)
print(response.ok)
print(response.url)
print(response.encoding)


# Exercitiul 10
import requests

response = requests.get(BASE_URL, timeout=TIMEOUT)
response.raise_for_status()

try:
    bad_response = requests.get(
        BASE_URL + "/this-page-does-not-exist", timeout=TIMEOUT
    )
    bad_response.raise_for_status()
except requests.HTTPError:
    print("Pagina solicitata nu a fost gasita sau a aparut o eroare HTTP.")


# Exercitiul 11
import requests

response = requests.get(BASE_URL, timeout=TIMEOUT)

for header, value in response.headers.items():
    print(f"{header}: {value}")

# Exercitiul 12
import requests
response = requests.get(BASE_URL, timeout=TIMEOUT)

print(response.headers.get("Server", "lipseste"))
print(response.headers.get("Content-Type", "lipseste"))
print(response.headers.get("content-type", "lipseste"))

# Exercitiul 13
import requests
response = requests.get(BASE_URL, timeout=TIMEOUT)

count = response.text.lower().count("cyber")
print(count)

# Exercitiul 14

import time
import requests

time.sleep(1)

response = requests.get(BASE_URL, timeout=TIMEOUT)

html = response.text

start = html.find("<title>") + len("<title>")
end = html.find("</title>")

titlu = html[start:end].strip()

print("Titlul paginii este:", titlu)
print("Afisare stare cod:",response.status_code)




# Exercitiul 15

import time
import requests

time.sleep(1)

raspuns_15 = requests.get(BASE_URL, timeout=TIMEOUT)

linii = raspuns_15.text.splitlines()
numar_linii = len(linii)

cea_mai_lunga_linie = max(linii, key=len)
lungime_maxima = len(cea_mai_lunga_linie)

print("Numar lini:", numar_linii)
print("Lungimea cele mai lungi linii:", lungime_maxima)

print("Afisarea stare cod:",raspuns_15.status_code)



# Exercitiul 16


import time
import requests

time.sleep(1)

response = requests.get(BASE_URL, timeout=TIMEOUT)

ver_https = response.url.startswith("https://")


if ver_https:
    print("Conexiunea este securizata (HTTPS).")
else:
    print("Conexiunea nu este securizata (HTTP).")

print("Code de stare:",response.status_code)


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



# Exercitiul 18

import time
import requests

time.sleep(1)
response = requests.get(BASE_URL, timeout=TIMEOUT)

time.sleep(1)
response_1 = requests.head(BASE_URL, timeout=TIMEOUT)

comp = len(response.content)
comp_1 = len(response_1.content)

print("Lungimea .get :",comp)
print("Lungimea .head :",comp_1)


# requests.get() - reda atat antetele cat si continutul propriu zis
# requests.head() - reda doar antetele, de aceea este intotdeauna 0



# Exercitiul 19

import time
import requests

time.sleep(1)
response = requests.get(BASE_URL, timeout=TIMEOUT)
cookies = response.cookies

if cookies:
        for cookie in cookies:
            print(f"Cookie setat: {cookie.name}  Securizat: {cookie.secure}")
else:
    print("Nici un cookie setat")






# Exercitiul 20

import time
import requests

obiect = requests.Session()
obiect.headers.update({'User-Agent': 'WebLab-<Midoni Lucian>'})
time.sleep(1)

response = obiect.get(ECHO_URL+ "/headers", timeout=TIMEOUT)
print("Raspuns:\n ",response.json())

# response.text este un atribut ce deja are o valoare stocata de aceea nu are nevoie de paranteze.
# response.json() este o metoda ce executa un proces de interpretare motiv pentru care trebuie apelata cu paranteze.






