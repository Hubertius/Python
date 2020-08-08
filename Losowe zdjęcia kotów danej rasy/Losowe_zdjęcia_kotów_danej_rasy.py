import requests
import json
import webbrowser
params = {
            "limit" : 5,
            "breed_id" : "beng"
         }
r = requests.get("https://api.thecatapi.com/v1/images/search/",params)
try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Wrong format!")
    exit(1)
#print(content)
for cat in content:
    webbrowser.open(cat["url"])
exit(0)
