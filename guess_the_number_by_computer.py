from random import randint 
import time 
print("Welcome to Guess the Number Game!")
print("I have selected a number between 1 and 100. Try to guess it!")
number = 0
number_of_guesses = 0
while number < 1 or number >100:
    number = int(input("\n\nEnter a number for the computer to guess: "))
    if number > 100:
        print ("Number must be lower than or equal to 100!")
    if number < 1:
        print ("Number must be greater than or equal to 1!")

guess = randint(1, 100)

print ("The computer takes a guess...", guess)
while guess != number:
    if guess > number :
        time.sleep(1)
        guess -= 1
        
        guess = randint(1 , guess)
        number_of_guesses += 1 
    else:
        guess += 1
        guess = randint(guess, 100)
        time.sleep(1)
        number_of_guesses += 1  
    print ("The computer takes a guess...", guess)

print ("The computer guessed", guess, "and it was correct!")    
print("the attempts are :" , number_of_guesses )