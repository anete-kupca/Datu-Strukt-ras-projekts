import requests
from bs4 import BeautifulSoup

#darbs = input("Ievadi darba nosaukumu: ")
url = "https://cv.lv/lv/search?limit=20&offset=0&categories%5B0%5D=INFORMATION_TECHNOLOGY&fuzzy=true&searchId=dba27038-d36b-4d0a-98c6-b92385b9568b"

lapa = requests.get(url)

if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.text, "html.parser")
    print(lapas_saturs.prettify())