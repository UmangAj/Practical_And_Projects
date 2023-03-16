
# guess the number game.


print("Please guess the number between 1 to 100")
i = 1
for i in range(1, 10):
    n = int(input("Guess the number :\n"))
    if n < 18:
        print("You guess low number. Please guess high number")
    elif n > 18:
        print("You guess high number. Please guess low number")
    else:
        print("congratulations you won the game !!! ")
        print(i, "no. of guesses he took to finish")
        break
    print(9 - i, "numbers of guesses lest !!")

print("Game Over !!!!")












