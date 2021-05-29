# Write a program to display all prime numbers within a range

print("Enter two numbers between which you want to find prime numbers ")
start = int(input("Enter your starting number : "))
end = int(input("Enter your ending number : "))
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
