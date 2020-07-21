"""
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 
"""
try:
    num = int(input("Podaj liczbę: "))
except:
    print("You didn't write a number. Program will immediately shutdown")
    exit(1)
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")



