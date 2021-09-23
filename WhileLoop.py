correctNumber = 17
userGuess = 0
while userGuess != correctNumber:
    userGuess = int(input("Please guess number : "))
    if userGuess > correctNumber:
        print("Too Large")
    elif userGuess < correctNumber:
        print("Too small")
    else:
        print("Correct answer")