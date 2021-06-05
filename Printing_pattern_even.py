# It will print star pattern when even number and reverse star pattern when n is odd

def star():
    n = int(input("Enter your number : "))
    for i in range(n):
       if (n % 2) == 0:
           print("*" * (i + 1))
       else:
           print("*" * (n - i))
    return n
star()

