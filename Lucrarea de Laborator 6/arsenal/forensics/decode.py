# A1

import base64
import re
from urllib.parse import unquote

s = "Salut"
b = s.encode()  # bytes
print(b, b[0])  # b'Salut' 83

print(b.hex())
b_from_hex = bytes.fromhex(b.hex())
print("Bytes din hex:", b_from_hex)


# A2
def ghici_strat(s):
    if "%" in s:
        return "url"
    if re.fullmatch(r"[0-9a-fA-F]+", s) and len(s) % 2 == 0:
        return "hex"
    if re.fullmatch(r"[0-9a-zA-Z+/=]+", s):
        return "base64"
    return "necunoscut"


print(ghici_strat("%2Fetc"))  # url
print(ghici_strat("48656c6c6f"))  # hex


# A3

def desfa(s):
    strat = ghici_strat(s)
    if strat == "base64":
        return strat, base64.b64decode(s)
    elif strat == "hex":
        return strat, bytes.fromhex(s)
    elif strat == "url":
        return strat, unquote(s).encode("utf-8")

    return strat, s.encode("utf-8")


# A4

def citibil(b):
    return len(b) > 0 and all(32 <= c < 127 for c in b)

val = "NTM1OTU3NTk="
for _ in range(8):
    strat, b = desfa(val)

    if citibil(b):
        print(f"Găsit text citibil [{strat}]:", b.decode())
        break
    else:
        try:
            val = b.decode("utf-8")
        except UnicodeDecodeError:
            break

# A5

date = open("probe/xor.bin", "rb").read()
for k in range(256):
    clar = bytes(b ^ k for b in date)
    if citibil(clar):
        print("cheie: ", k, clar.decode())

# cheie:  128 Un singur octet tine tot secretul... gaseste-l! FLAG{xor_un_octet}


# A6

import hashlib

tinta = open("probe/hashuri.txt").readline().strip()
print(len(tinta))   # 32 md5 / 40 sha1 / 64 sha256

for cuv in open("probe/wordlist.txt", encoding="latin1"):
    cuv = cuv.strip()
    # TODO: daca hashlib.md5(cuv.encode()).hexdigest()
    if hashlib.md5(cuv.encode()).hexdigest() == tinta:
        print("gasit:",cuv)
        break


# A7

import argparse, json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("intrare")
p.add_argument("--fisier", action="store_true")
a = p.parse_args()

# TODO: daca a.fisier, citeste octetii din cale; altfel trateaza intrarea ca sir
if a.fisier:
    cale = Path(a.intrare)
    if not cale.is_file():
        print(f"Eroare: Fișierul '{a.intrare}' nu există.")
        exit(1)
    date = cale.read_bytes()
else:
    date = a.intrare.encode("utf-8")

strat = "text_sau_format_detectat"
try:
    rezultat = date.decode("utf-8", errors="ignore")
except Exception:
    rezultat = date.hex()

# TODO: salveaza {strat, rezultat} in arsenal/forensics/fisa.json
cale_iesire = Path("fisa.json")
cale_iesire.parent.mkdir(parents=True, exist_ok=True)

date_json = {
    "strat": strat,
    "rezultat": rezultat
}

with open(cale_iesire, "w", encoding="utf-8") as f:
    json.dump(date_json, f, indent=4, ensure_ascii=False)

# python decode.py probe/mesaj.txt --fisier ( comanda de rulare in terminal)