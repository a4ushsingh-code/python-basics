import random

num = random.randint(1,10)

tries = 0 # keep tracks how many tries a person take to guess the number

while True :

    guess = int(input("Please guess your number :"))

    if num == guess:
        tries +=1
        print(f"Congrats! ,You are right and you guessed the number in {tries} tries  ")
        break # terminates program when guess matches num
        

    elif num > guess:
        print("go a little higher")
        tries +=1

    elif num < guess:
        print("go a little lower")
        tries +=1

    else:
        tries +=1
        print("Sorry! Try again please")


