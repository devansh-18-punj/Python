# Suppose i am a fitness trainer and nutritionist and many people as client come to me for training and for problems
# related to body like spine pain and legs pain and muscle pain and all
# and my work is to design the diet plan and exercise for all those people
# I have 3 clients - Rohan, Harry and Hammad
# I have to manage the diet plan of them
# I have to make total of 6 files - 3 files for their food plan and 3 files for their exercises
# Write a function which when executed takes as input client names
# Like - 1 for Rohan, 2 for harry..................
# Then for exercise and diet - 1 for exercise, 2 for diet

def getdate():
    import datetime
    return datetime.datetime.now()

def dietplan():
    print("Enter 1 to write and print data for Rohan ")
    print("Enter 2 to write and print data for harry ")
    print("Enter 3 to write and print data for hammad")
    n = int(input("So, enter your number whom you want to lock schedule : "))
    if n == 1:
        print("Enter 1 to lock diet plan of Rohan and enter 2 to lock exercise plan for rohan ")
        u = int(input("Enter your number : "))
        if u == 1:
            value = input("type here\n")
            with open("Rohan_diet.txt", "a") as f:
                f.write(str([str(getdate())]) + ": \n" + value + "\n")
            print("successfully written, you can check")
        elif u == 2:
            value = input("Type here : \n")
            with open("Rohan_exercise.txt", "a") as f:
                f.write(str([str(getdate())]) + ": \n" + value + "\n")
            print("Successfully written, you can check")
        else:
            print("Please enter number 1 or 2")
    elif n == 2:
        print("Enter 1 to lock diet plan of Harry and enter 2 to lock exercise plan for Harry ")
        u = int(input("Enter your number : "))
        if u == 1:
            value = input("Type here : \n")
            with open("Harry_diet.txt", "a") as f:
                f.write(str([str(getdate())]) + ": \n" + value + "\n")
            print("Successfully written, you can check ")
        elif u == 2:
            value = input("Type here : \n")
            with open("Harry_exercise.txt", "a") as f:
                f.write(str([str(getdate())]) + ": \n" + value + "\n")
                print("Successfully done, check it now")
        else:
            print("Please enter number 1 or 2")
    elif n == 3:
        print("Enter 1 to lock diet plan of Hammad and enter 2 to lock exercise plan for Hammad ")
        u = int(input("Enter your number : "))
        if u == 1:
            value = input("Type here : \n")
            with open("Hammad_diet.txt", "a") as f:
                f.write(str([str(getdate())]) + ": \n" + value + "\n")
            print("Successfully done, check it now")
        elif u == 2:
            value = input("Type here : \n")
            with open("Hammad_exercise.txt", "a") as f:
                f.write(str([str(getdate())]) + ": \n" + value + "\n")
            print("Successfully done, check it once")
    else:
        print("Enter a valid number please :)")
dietplan()
