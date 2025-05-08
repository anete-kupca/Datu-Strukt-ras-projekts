import requests as rq
from bs4 import BeautifulSoup

darbs = input("Ievadi darba nosaukumu: ")
url = "https://cv.lv/lv/search?limit=20&offset=0&categories%5B0%5D=INFORMATION_TECHNOLOGY&fuzzy=true&searchId=dba27038-d36b-4d0a-98c6-b92385b9568b"

lapa = rq.get(url)

if lapa.status_code == 200:
    print("Lapa ir pieejama")