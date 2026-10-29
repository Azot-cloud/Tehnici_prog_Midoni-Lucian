#Laborator: funcții, metode și importuri pe web

# Student: <Midoni Lucian>


BASE_URL = "https://cybercor.org"

ECHO_URL = "https://httpbin.org"

TIMEOUT = 10  # secunde #

# Exercitiul 39

from html.parser import HTMLParser


class ImageFinder(HTMLParser):

    def __init__(self):
        super().__init__()

        self.images = []

    def handle_starttag(self, tag, attrs):


        pass


