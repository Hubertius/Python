"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is
the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""
def all_of_Fibonnaci(number):
    list = []
    i = 0
    while i < number:
        get_value = fibonacci(i)
        list.append(get_value)
        i += 1
    return list
def fibonacci(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    else:
        return fibonacci(value - 1) + fibonacci(value - 2)
try:
     number = int(input("Tell me how many Fibonnaci numbers do you want to have in list:"))
except:
    print("Error! Program will shutdown immediately!")
    exit(1)
if number <= 0:
    print("Incorrect input data!")
    exit(2)
list = all_of_Fibonnaci(number)
print(list)
exit(0)

