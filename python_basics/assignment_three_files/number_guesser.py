#TODO: Part 3
import random
chosenNum = random.randint(1,9)
enteredNum = -1
while chosenNum != enteredNum:
    print('Enter a number between 1 and 9 inclusive')
    enteredNum = int(input())
print('Well guessed!')