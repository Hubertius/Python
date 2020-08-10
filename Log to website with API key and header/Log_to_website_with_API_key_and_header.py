import requests
import json
import webbrowser

from pprint import pprint

headers = {
                "x-api-key" : "2c5bc730-4156-45a3-bbb6-b00b61bbf38b"
          }
r = requests.get("https://api.thecatapi.com/v1/favourites", headers = headers)
try:
    content = r.json()
except:
    print("Wrong format!")
    exit(1)
else:
    print("Everything is okay!")
print(content)
exit(0)
