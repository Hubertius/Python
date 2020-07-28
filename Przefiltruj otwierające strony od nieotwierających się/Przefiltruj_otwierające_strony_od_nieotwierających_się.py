"""
Wyobraź sobie, że szef zlecił Ci zadanie otwarcia z jego pliku tekstowego 5 stron i przefiltrowania ich w taki sposób, aby podać mu tylko te, które działają.
Szef chce, abyś działające strony zapisał do pliku tekstowego.
Szef nie przesłał Ci jeszcze pliku ze stronami. Wiesz tylko o tym, że będziesz musiał wykonać te zadanie następnego dnia.
Załóżmy, że tylko 2 strony z tej listy działa. Czy zrobiłbyś to wszystko ręcznie? A może zastosowałbyś Pythona i to co do tej pory poznałeś? :)
Masz czas na zastanowienie się co zrobić do następnego dnia. Możesz napisać krótki program, który zrobi robotę za Ciebie lub też będziesz wykonywał cały dzień żmudną robotę ;)

Podpowiedź:


"""
import requests

list = [
        "https://www.youtube.com/watch?v=M_mP6Ae63No",
        "https://drive.google.com/drive/folders/1AAxY92g2LrS-T0L5CaWC9MX00rJ0-y0X",
        "https://noifajnie",
        "https://coś",
        "https://nic"
       ]
with open("File_with_correct.txt","w+", encoding = "UTF-8") as file:
    for element in list:
        try:
            response = requests.get(element)
            #print("HERE")
            print(response)
            print(element)
            file.write(element + "\n")
        except:
            continue
exit(0)