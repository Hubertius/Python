"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
"""
i = 0
count_a = 0
count_b = 0
while True:
    while i < 3:
        a = input("Player A is choosing Rock-Paper-scissors: ")
        a = a.upper()
        if( a != 'ROCK' and a != 'SCISSORS' and a != 'PAPER'):
            print("ERROR! Program will shutdown immediately!")
            exit(1)
   
        b = input("Player B is choosing Rock-Paper-scissors: ")
        b = b.upper()
        if( b != 'ROCK' and b != 'SCISSORS' and b != 'PAPER'):
            print("ERROR! Program will shutdown immediately!")
            exit(1)
        if a == b:
            count_a += 1
            count_b += 1
        elif a == 'ROCK' and  b == 'SCISSORS':
            count_a += 1
        elif a == 'SCISSORS' and b == 'PAPER':
            count_a += 1
        elif a == 'PAPER' and b == 'ROCK':
            count_a += 1
        else:
            count_b += 1
        if count_a == 2 and i == 1:
            print("Player A has won, because he has already two points. Game is over!")
            break
        elif count_b == 2 and i == 1:
            print("Player B has won, because he has already two points. Game is over!")
            break
        i += 1
    if count_a > count_b and i != 1:
        print("Player A won")
    elif count_b > count_a and i != 1:
        print("Player B won")
    elif count_b == count_a and i != 1:
        print("Draw")
    print("Do you want to play again? Y/N")
    choice = input()
    choice.upper()
    if choice == 'N':
        break
    elif choice == 'Y':
        print("So be it, program will ontinue to run")
    else:
        print("EROR! Program will shutdown immediately!")
        exit(1)
exit(0)




