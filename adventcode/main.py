# guess the number game
import random

print("Hello, what is your name?")
name = input()

print("Well, " + name + " I am thinking of a number between 1 and 20")
secretNumber = random.randint(1,20)

for guessesTaken in range(1, 7):
    print("take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("your guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    else:
        break #this condition is for the correct guess

if guess == secretNumber:
    print("good job, " + name +" you guessed my name in " + str(guessesTaken) + " guses")
else:
    print("Nope, the number I was thinking of was " + str(secretNumber))






