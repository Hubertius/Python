"""
Napisz program, który pobierze pytania ze strony stackoverflow i posortuje je w taki sposób, że spełnią następujące wymagania:
będą wypisane malejąco
minimum 15 punktów
z ostatniego tygodnia
z kategorii python
"""
import requests
import json
import pprint
parameters = {
                "site" : "stackoverflow",
                "sort" : "votes",
                "order": "desc",
                "fromdate": "2019-08-20",
                "tagged" : "python",
                "min" : 15
             }
r = requests.get("https://api.stackexchange.com/2.2/questions/", parameters)
if r.status_code == 200:
    print("Page is existing.")
else:
    print("Page isn't existing.")
    exit(1)
try:
    get_json = r.json()
except json.decoder.JSONDecoderError:
    print("Something is wrong with decoding of json from this page.  :(")
    exit(1)
pprint.pprint(get_json)
