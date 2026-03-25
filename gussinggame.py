import random
import time
print()
print()
time.sleep(1)
print("                                                          Number Guessing Game")
time.sleep(0.75)
print()
print("Guess the number between 1 and 10")
time.sleep(0.75)
print()
print("You Have Infinite Tries")
time.sleep(0.75)
print()
print("Type 'exit' for Exiting the Game (In guess column)")
while True :
    exited = False 
    secret = random.randint(1, 10)
    print()
    time.sleep(0.75)
    while True:
        guess = input("Your guess: ")
        if guess.lower() =="exit":
            print("Game exited")
            exited = True 
            break
        elif not guess.isdigit() :
            print("Invalid Input ❌")
            print()
            print("(Enter number between 1 to 10)")   
            continue 
        elif int(guess) > 10 or int(guess) < 1:
            print("Invalid Input ❌")
            print()
            print("Enter number between 1 to 10") 
            continue
        else:
            if int(guess) == secret:
                time.sleep(0.25)
                print()
                print("Correct! 🎉")
                print("You Win! 🎉")
                break
            elif int(guess) > secret:
                time.sleep(0.25)
                print("Wrong!")
                print("Your guess is high.")
                continue
            elif int(guess) < secret:
                time.sleep(0.25)
                print("Wrong!")
                print("Your guess is low.")
                continue
    if exited:
        break
    time.sleep(0.5)
    print()
    choose=input("Do you want to play again yes/no :")
    if choose =="yes":
        continue
    elif choose =="no":
        print("Game exited")
        break
print()
if not exited:
    time.sleep(0.25)
    print()
    print(f"The number was {secret}.")
    print("THANK YOU".center(125,"-"))
    print()