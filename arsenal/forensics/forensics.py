# Extinderea B1-B4 / forensics.py


# B1

from pathlib import Path

def tip_real(cale):
    cap = open(cale, "rb").read(8)
    # TODO: daca cap incepe cu b"%PDF" -> "pdf"
    if cap.startswith(b"%PDF"):
        return "pdf"
    #       b"\x89PNG" -> "png" ; b"\xff\xd8" -> "jpeg"
    if cap.startswith(b"\x89PNG"):
        return "png"
    if cap.startswith(b"\xff\xd8"):
        return "jpeg"
    #       b"PK\x03\x04" -> "zip/docx"
    if cap.startswith(b"\x03\x04"):
        return "zip/docx"
    return cap.hex()
print(tip_real("probe/foto.jpg"))


# B2

import re
date = open("probe/ascuns.png", "rb").read()
# TODO: for m in re.findall(rb"[ -~]{4,}", date):
for m in re.findall(rb"[-~]{4,}",date):
    text = m.decode("latin1")
    print(text)


# B3

from PIL import Image
from PIL.ExifTags import TAGS
img  = Image.open("probe/foto.jpg")
exif = img._getexif() or {}
for id, val in exif.items():
    print(TAGS.get(id, id),"=",val)
# TODO: ia blocul GPS (tag 34853) si tipareste

gps_info = exif.get(34853)
if gps_info:

    lat_data = gps_info.get(2)
    lat_ref = gps_info.get(1)

    long_data = gps_info.get(4)
    long_ref = gps_info.get(3)

    #       latitudinea si longitudinea
print(f"Latitudine: {lat_data},{lat_ref}")
print(f"Longitudine: {long_data},{long_ref}")


# B4

date = open("probe/ascuns.png", "rb").read()
i = date.find(b"PK\x03\x04")

# TODO: daca i != -1:
if i!= -1:
    #   open("gasit.zip","wb").write(date[i:])
    arhiva = open("probe/gasit.zip", "wb").write(date[i:])

#   print("arhiva extrasa de la octetul", i)
    print(f"Arhiva extrasa de la octetul : {arhiva}")
    print("Arhiva extrasa de la octetul: ",i)

# apoi dezarhiveaza si vezi ce era inauntru
    dezarhivarea = open("probe/gasit.zip", "rb").read()
    print(f"Continutul dezarhivarii:",dezarhivarea)

#x00secret.txtFLAG{ascuns_prin_carving}










