def palindrom(string):
    new_string = ''.join(reversed(string))
    if( new_string == string):
        return True
    else:
        return False
string = input("Write a string: ")
boolean_check = palindrom(string)
if boolean_check == True:
    print("That's a palindrom!")
else:
    print("That's not a palindrom!")
exit(0)
