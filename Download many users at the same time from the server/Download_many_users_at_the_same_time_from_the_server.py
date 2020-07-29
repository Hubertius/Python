import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()
usersWithMaxValues = [5,10]
print("Users Id with maximum values:",usersWithMaxValues)
for user in users:
    if(user["id"] in usersWithMaxValues):
        print("This user is the same who have the maximum values. His id is:",user["id"])
        usersWithMaxValues.remove(user["id"])
        print("There is only left on the maximum list:",usersWithMaxValues)
exit(0)