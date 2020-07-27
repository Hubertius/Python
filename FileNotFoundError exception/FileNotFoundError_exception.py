"""
Stwórz funkcję, która obsługuje otwieranie pliku do wczytywania danych.
Zapytaj się użytkownika o nazwę pliku, który chce otworzyć do wczytania.
Jeśli plik nie istnieje wypisz mu odpowiedni komunikat.
Jeśli plik istnieje wczytaj całą jego zawartość i zwróć jako wynik funkcji.
"""
def open_the_file(string):
    list = []
    with open(string,"r", encoding = "UTF-8") as file:
        list = file.readlines().splitlines()
    file.close()
    return list
string = input("Write a name of the file: ")
try:
    list = open_the_file(string)
    print(list)
except:
    print("File doesn't exist!")
exit(0)
