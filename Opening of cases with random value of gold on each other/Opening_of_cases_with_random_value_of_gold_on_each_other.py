
"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""
import random

def function(list):
    choice_for_nothing = random.choices([0,1],[40,60],k = 5)
    len = 0
    for i in choice_for_nothing:
        if i == 1:
            len += 1
    list_value = random.choices(list,[75,20,4,1],k = len)
    return list_value
    
def to_count(list):
    count = 0
    for i in list:
        if i == 'zielony':
            count += 1000
        elif i == 'pomarańczowy':
            count += 4000
        elif i == 'fioletowy':
            count += 9000
        elif i == 'złota' :
            count += 16000
    return count


list = ['zielony','pomarańczowy','fioletowy','złota']
list_from_function = function(list)
print(list_from_function)
value_from_count = to_count(list_from_function)
print("Value from the cases: ",value_from_count)