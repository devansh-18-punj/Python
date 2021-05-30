print("It's a game of guessing the right key word for the computer to unlock, Guess the right word and unlock "
      " the computer ")
print("Enter only one character between A to Z (in capital) at a time")
code = "J"
No_of_guesses = 6
for i in range(1, 7):
    code = input("Enter your guess key word : ")
    if code == "J":
        print("Congo!! You nailed the game by guessing it in", i, "chances")
        break
    elif code > "J":
        print("You are wrong, guess some low key word")
        print("Now you are left with", No_of_guesses - i, "chances")
    elif code < "J":
        print("You are wrong, guess some high key word")
        print("Now you are left with", No_of_guesses - i, "chances")
    else:
        print("You are entering something wrong")