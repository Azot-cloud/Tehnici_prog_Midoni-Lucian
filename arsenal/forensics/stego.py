# B5

from PIL import Image

img = Image.open("probe/foto.jpg").convert("RGB")
px = list(img.get_flattened_data())
mesaj = b"FLAG{ascuns_in_pixeli}"

biti = "".join(f"{x:08b}" for x in mesaj)
canal = []
for p in px:
    canal.extend(list(p))

# TODO: pentru fiecare bit, ia un canal si pune
for i,bit in enumerate(biti):
    canal[i] = (canal[i] & ~1) | int(bit)

px_nou = []
for i in range(0,len(canal),3):
    px_nou.append((canal[i], canal[i+1],canal[i+2]))

# TODO: img.putdata(px_nou); img.save("stego.png")
img.putdata(px_nou)
img.save("stego.png")


# B6

px = list(Image.open("stego.png").convert("RGB").get_flattened_data())
biti = ""

for (r, g, b) in px:
# TODO: aduna ultimii biti (r&1, g&1, b&1)
    biti += str(r & 1) + str(g & 1) + str(b & 1)
octeti = bytearray()

# TODO: grupeaza cate 8 biti -> octeti -> text
for i in range(0, len(biti), 8):
    octet = int(biti[i:i+8], 2)

#opreste-te la primul octet 0 (final de mesaj)
    if octet == 0:
        break
    octeti.append(octet)

mesaj_secret = octeti.decode("utf-8", errors="replace")
print(mesaj_secret)


