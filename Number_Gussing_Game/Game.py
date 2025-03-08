import random 

CompNum = random.randint(1,100)
while True :
    try :
        num = int(input("Guess the number between 1 and 100 : "))
        if(num > CompNum):
            print('Number is Too High')
        elif(num < CompNum):
            print("Number is Too Low")
        else:
            print("Congratulations! you guessed the number")
            break
    except ValueError:
        print("enter valid number")