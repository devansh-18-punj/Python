n = int(input("Enter your number : "))
def mine(n):
    for i in range(0, n):

        for j in range(0, i + 1):
            print("* ", end="")

        # ending line after each row
        print("\r")

mine(n)
