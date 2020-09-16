import requests
from bs4 import BeautifulSoup

base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soap = BeautifulSoup(r.text)
