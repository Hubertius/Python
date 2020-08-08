import requests
import json
import webbrowser
while True:
    choose = int(input("How many photos of Shibe dogs do you want to have (choose from 1-100): "))
    if choose < 1 or choose > 100:
        print("Incorrect! Try again!")
    else:
        print("Good! You will see your photos in your browser now. :)")
        break;
params = {
            "count" : choose
         }
r = requests.get("http://shibe.online/api/shibes",params)
if r.status_code == 200:
    print("Page is existing!")
else:
    print("Page isn't existing!")
try:
    shibe_content = r.json()
except json.decoder.JSONDecodeError:
    print("Something is wrong with content of this page. :(")
    exit(1)
for dog in shibe_content:
    webbrowser.open_new_tab(dog)
exit(0)
