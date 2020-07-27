"""
Wczytaj zawartość pliku.
Następnie do osobnych plików (o nazwach "imiona.txt" i "nazwiska.txt") zapisz osobno imiona i nazwiska.
"""
list = []
with open("Names_and_surnames.txt","r",encoding = "UTF-8") as file:
    for line in file:
        list.append(tuple(line.replace("\n","").split(" ")))
    file.close()
print(list)
with open("imiona.txt","w+",encoding = "UTF-8") as file:
    for item in list:
        file.write(item[0] + "\n")
    file.seek(0)
    print(file.read())
    file.close()
with open("nazwiska.txt","w+",encoding = "UTF-8") as file:
    for item in list:
        try:
            file.write(item[1] + "\n")
        except:
            continue
    file.seek(0)
    print(file.read())
    file.close()
exit(0)