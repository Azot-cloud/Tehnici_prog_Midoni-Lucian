#Laborator: funcții, metode și importuri pe web

# Student: <Midoni Lucian>


BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10  # secunde #



# Exercitiul 9


# import time
# import requests
#
# time.sleep(1)
#
#
# raspuns_9 = requests.get(BASE_URL,timeout=TIMEOUT)
#
# print("Raspuns cod de stare: ",raspuns_9.status_code)   # Este un atribut
# print("Afisare OK:", raspuns_9.ok)                      # Este un atribut
# print("Afisare URL:",raspuns_9.url)                     # Este un atribut
# print("Afisare Encoding:",raspuns_9.encoding)           # Este un atribut





# Exercitiul 10



# import time
# import requests
#
#
# raspuns_10 = requests.get(BASE_URL, timeout=TIMEOUT)
# raspuns_10.raise_for_status()
#
# time.sleep(1)
#
# url_gresit = BASE_URL + "/this-page-does-not-exist"
#
# try:
#     raspuns_gresit = requests.get(url_gresit, timeout=TIMEOUT)
#     raspuns_gresit.raise_for_status()
#
# except requests.HTTPError:
#     print("Incercati din nou  :)")
#
# print("Cod de stare: ",raspuns_10.status_code)




# Exercitiul 11


# import time
# import requests
#
# raspuns_11 = requests.get(BASE_URL, timeout=TIMEOUT)
#
# time.sleep(1)
#
# for nume, valoare in raspuns_11.headers.items():
#     print(f"{nume}:{valoare}")
#
# print("Afisarea Antetelor:",raspuns_11)
# print("Cod de stare: ",raspuns_11.status_code)






# Exercitiul 12


# import time
# import requests
#
# raspuns_12 = requests.get(BASE_URL, timeout=TIMEOUT)
#
# time.sleep(1)
#
# server = raspuns_12.headers.get("Server","lipseste")
# tip_continut = raspuns_12.headers.get("content-type","lipseste")
#
# print(f"Server: {server}")
# print(f"content-type: {tip_continut}")
#
# print("Afisare stare cod:"raspuns_12.status_code)




# Exercitiul 13


# import time
# import requests
#
# time.sleep(1)
#
# response = requests.get(ECHO_URL, timeout=TIMEOUT)
#
# numara_cyber = response.text.lower().count("cyber")
#
# print("Afisarea numerotarii cuvantului cyber",numara_cyber)
# print("Afisarea cod de stare:", response.status_code)


# Putem folosi .lower().count()
# pentru că fiecare metodă returnează un obiect peste care se poate aplica următoarea metodă.



