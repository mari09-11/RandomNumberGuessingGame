import random

def GuessGame() :
    number = random.randint(0,25)
    print("Guess the random number:")
    for attempt in range(1,11):
        guess = int(input())
        if guess > number :
            attempt = 10 - attempt
            print("The number is below your guess!!")
            print("you have "+ str(attempt) +" attempts left! Try again! :")
        elif guess < number : 
            print("The number is greater than your guess!!")
            print("you have "+ str(attempt) +" attempts left! Try again! :")
        else :
            print("Congrats! You win !!")
            return
    print("You ran out of attempts :(...,Try Again next time!!")
    print("The number was "+ str(number) + " btw")

GuessGame()