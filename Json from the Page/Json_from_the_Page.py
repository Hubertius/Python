def get_dictionary_of_id_with_true(dictionary):
    dictionary_of_id = dict()
    for element in dictionary:
        if element["completed"] == True:
            try:
                dictionary_of_id[element["userId"]] += 1
            except:
                dictionary_of_id[element["userId"]] = 1
    return dictionary_of_id
def get_keys_with_max_values(dictionary):
    return [key for key,value in dictionary.items() if value == max(dictionary.values())]

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")
try:
    materials = r.json()
except:
    print("Error!")
else:
    dictionary_of_id_with_values = get_dictionary_of_id_with_true(materials)
    list = get_keys_with_max_values(dictionary_of_id_with_values)
    print(list)
finally:
    print("THE END")
exit(0)


