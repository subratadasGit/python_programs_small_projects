import random
while True :
    choice = input("enter your choive (y/n)  ").lower()
    if (choice == "y") :
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f" ({dice1},{dice2}) ")
    elif (choice == "n"):
        print("Thanks For Playling")
        break
    else :
        print("Invalid Choice")

