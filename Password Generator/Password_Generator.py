"""
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list].
"""
import string
import random
def creator_of_the_password(how_many):
    word =  string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(word) for i in range(how_many))

try:
    how_many = int(input("How many letters do you want to have in your password? "))
except:
    print("Error! Program will shutdown immediatelly!")
    exit(1)
string = creator_of_the_password(how_many)
print(string)
exit(0)




