"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
"""
import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.nytimes.com/")
if r.status_code == 200:
    print("Page opened successfully.")
    soup = BeautifulSoup(r.text,'html.parser')
    result = soup.find_all('h2')
    headlines = []
    for i in result:
        if result.index(i) < len(result)-2:
            headlines.append(i.text)
else:
     print("Page not found!")
     exit(1)
print(headlines)
exit(0)