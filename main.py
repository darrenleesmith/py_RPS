import random

code = random.randrange(1 ,3)
userName = input("What is your name? ")
dict = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}
print("1: Rock 2: Paper 3: Scissors")
userInput = int(input("Please select a option: "))
print("\nComputer selected: " + dict[code])
print(userName + " selected: " + dict[userInput])

if code == userInput:
    print("\nDraw")
    
if code == 1:
    if userInput == 2:
        print(userName + " won! " + dict[2] + " covers " + dict[1])
    if userInput == 3:
        print("Computer won " + dict[1] + " smashes " + dict[3])
        
if code == 2:
    if userInput == 1:
        print("Computer won! " + dict[2] + " covers " + dict[1])
    if userInput == 3:
        print(userName + " won!" + dict[3] + " cuts " + dict[2])
        
if code == 3:
    if userInput == 1:
        print(userName + " won! " + dict[1] + " smashes " + dict[3])
    if userInput == 2:
        print("Computer won! " + dict[3] + " cuts " + dict[2])
