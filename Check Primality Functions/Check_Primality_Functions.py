"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""
def is_prime(number):
    if number < 2:
        return False
    else:
        count = 0
        for i in range(number,1,-1):
            if number % i == 0:
               count += 1
        if count == 1:
            return True
        else:
            return False
try:
    choice = int(input("Write a number, so I can check if it is prime:"))
except:
    print("Error! Program will shutdown immediately!")
    exit(1)
check = is_prime(choice)
if check == True:
    print("Yes, it is prime!")
else:
    print("No, it isn't prime!")
exit(0)


