import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    
    name = input("Hello! What is your name? ")
    print("Well,",name,", I am thinking of a number between 1 and 20.\nTake a guess.")
    
    attempts = 0
    while True:
        guess = int(input())
        attempts += 1
        
        if guess < secret_number:
            print("Your guess is too low.\nTake a guess.")
        elif guess > secret_number  :
            print("Your guess is too high.\nTake a guess.")
        else:
            print("Good job,",name,"! You guessed my number in",attempts," guesses!")
            break

guess_the_number()
