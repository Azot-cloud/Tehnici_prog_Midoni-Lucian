#Laborator: funcții, metode și importuri pe web

# Student: <Midoni Lucian>


BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10  # secunde #


# Exercitiul 1

import requests

print("Versiunea requests: ",requests.__version__)
import urllib.request



# Requests a avut nevoie deoarece nu face parte din bilioteca standard Python.
# Urllib nu a avut nevoie de pip install deoarece acesta este o biblioteca externa.

# Exercitiul 2

#      V1
import requests
response = requests.get(BASE_URL)
print("Cod de stare:",response.status_code)

#      V2
from requests import get
response_2= requests.get(BASE_URL)
print("Cod de stare:",response_2.status_code)


# Avantaj "import requests": Pastreaza codul clar si previne coliziuni de nume.

# Avantaj "from requests import get": Face codul mai scurt, mai curat și mai rapid de scris,
# si nu trebuie sa apelezi de mai multe ori functia.

# Exercitiul 3

import time
import requests as rq

time.sleep(1)

descarca3 = rq.get(BASE_URL, timeout=TIMEOUT)
print("Stare:",descarca3.status_code)


# Când un alias face codul mai ușor de citit?
# Un alias face codul mai ușor, atunci cand numele unei biblioteci e prea mare.

# Când un alias face codul mai greu de citit?
# Un alias face codul mai greu atunci cand folosesti un alias inventat pe care altii nu il inteleg.


# Exercitiul 4


import time
import urllib.request

time.sleep(1)

descarca4 = urllib.request.urlopen(ECHO_URL, timeout=TIMEOUT)
print("Cod de stare (urllib):", descarca4.status)

corp_octeti = descarca4.read()
corp_caracter = corp_octeti.decode("utf-8")

print("Primele 200 de caractere: \n",corp_caracter[:200])


# Afisarea .staus
# Cod de stare (urllib): 200


#Afisarea primelor 200 de caractere

# Primele 200 de caractere:
#  <!DOCTYPE html>
# <html lang="en">
#
# <head>
#     <meta charset="UTF-8">
#     <title>httpbin.org</title>
#     <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Tit




# Exercitiul 5

import requests
print(dir(requests))

# get - functie , urllib3 - modul , Request - clasa


# Exercitiul 6

import time
import requests

help(requests.get)

time.sleep(1)

raspuns_6 = requests.get(BASE_URL, timeout=TIMEOUT)
print("Stare cod:",raspuns_6.status_code)




# Exercitiul 7

import time
import requests

time.sleep(1)

inainte = time.perf_counter()
rapsuns_7 = requests.get(BASE_URL, timeout=TIMEOUT)
dupa = time.perf_counter()

timp_cronometrat = rapsuns_7.elapsed
print("Timpul cronometrat de catre cerere este:", timp_cronometrat)




# Exercitiul 8


try:
    import bs4
    print("Modulul bs4 importat cu succes")

except ImportError:
    print("Instalați modulul cu: pip install beautifulsoup4")


# Modulul este un simplu file care contine colectii de functii si variabile globale cu extensia .py
# Pachetele sunt registre de adrese care contin colectii de module
# O bilioteca e o colectie de pachete si moduli care te ajuta sa rezolvi o problema

