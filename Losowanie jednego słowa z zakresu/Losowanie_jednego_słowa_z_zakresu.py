import random
from random import shuffle
lista = ['kot','pies','dom']
choice = random.randint(0,3)
x = lista[choice]
operational = list(x)
shuffle(operational)
str = ''.join(operational)
while 1:
    a = input()
    if a == 'z' or a == 'Z':
        break;
    if a == str:
        print("Brawo! Zgadłeś!")
        break;
exit(0)

