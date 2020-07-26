"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
-Keep the game going until the user types “exit”
-Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
count = 0
while True:
    randomis = random.randint(1,9)
    choice = input("Write what number I had choose:")
    if choice == 'exit':
        print("You have chosen to end your program now. Thank you and goodbye.")
        print("But wait! Before you go, here is information about how many time you shot:",count)
        break;
    int_choice = int(choice)
    if int_choice < randomis:
        print("Too low! Try again!")
    elif int_choice > randomis:
        print("Too high! Try again!")
    else:
        print("Correct! Your shot was perfect!")
    count += 1
print("P.S: Before you end, here is information about how many times you wrote numbers:",count)
exit(0)




