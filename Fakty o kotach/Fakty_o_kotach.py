import requests
import json
import webbrowser
parameters = {
                 "amount" : 5 ,
                 "animal_type" : "dog"
             }
r = requests.get("https://cat-fact.herokuapp.com/facts/random",parameters)
try:
    cats = r.json()
except json.decoder.JSONDecodeError:
    print("Wrong format!")
    exit(1)
else:
    for cat in cats:
        print(cat["text"])
        print()
exit(0)



