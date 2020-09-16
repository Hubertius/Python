def search(list, number):
    if number in list:
        return True
    else:
        return False


list = [1, 3, 5, 30, 42, 43, 500]
try:
    number = int(input("Write a number: "))
except:
    print("You wrote not a number! :(")
    exit(1)
check_boolean = search(list, number)
print(check_boolean)
exit(0)
