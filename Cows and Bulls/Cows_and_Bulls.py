import random

def random_operations():
    a = random.randint(1000,9999)
    last = a % 10
    third = (a % 100) // 10
    second = (a % 1000) // 100
    first = a // 1000
    check = guess_the_number(first,second,third,last)
    return check
def guess_the_number(first,second,third,last):
    i = 0
    correct = 0
    while(True):
        print("Guess the number on his correct position: ")
        choice = int(input())
        if( i == 0 and choice == first):
            correct += 1
        elif( i == 1 and choice == second):
            correct += 1
        elif( i == 2 and choice == third):
            correct += 1
        elif( i == 3 and choice == last):
            correct += 1
        if( i == 3 ):
            break
        i += 1
    return correct

while(True):
    check = random_operations()
    if( check == 0):
        print("0 cows, 4 bulls!")
    elif( check == 1):
        print("1 cows, 3 bulls!")
    elif( check == 2 ):
        print("2 cows, 2 bulls!")
    elif( check == 3):
        print("3 cows, 1 bulls!")
    else:
        print("You guessed correct!")
        print("THE END")
        break
exit(0)



       
