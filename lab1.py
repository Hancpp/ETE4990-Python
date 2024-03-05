#!/usr/bin/env python
# coding: utf-8

# # Lists
# 
# ## Background
# Lists are one of the most commonly used data structures in Python and are very similar to arrays from other programming languages. A list can store many items or values inside of one overall object or structure, unlike a variable which can only store one item or value inside one object. 
# 
# The items in a list can be accessed by using what is called an “index” value, which simply refers to the position of a certain item inside of a list, as lists are ordered from item 0 to the number of elements - 1. Therefore a list with 5 elements will have index positions 0 through 4. 
# 
# Any data can be stored inside a list, numbers, strings, or objects, but it is common practice to only have one data type per list. Therefore if my list has integers, it would ONLY have integers, not strings, doubles, objects, etc.

# ## Mini-project - Guessing game
# Create a number guessing game and set a secret number at the beginning of the program. 
# The program will ask the player to enter a number to guess what the number is, then it’ll inform the player if they got it right or wrong.

# In[6]:


active = True
while active:
    user = int(input("Guess the secret number "))
    secretnum = 35
    if user == secretnum:
        print(user, " is the correct guess")
        active = False
    elif user <= secretnum:
        print(user, " is too low")
    else:
         print(user, " is too high")


# ## Mini-Project - Dice Roll
# 
# Part 1:
# Create a random number generator using dice. 
# You must create at least 5 dice
# The game must use conditionals (If, Else, Elif)
# The game must use nested conditionals (if 0=0:if 1=1: do something)
# 
# What lists should we create for the project?
# How many loops do we need?
# 
# Part 2:
# Create a list to store your gameplay. 
# Create at least 2 lists to store your game statistics.
# 
# Part 3:
# At the end of the output your gameplay statistics
# 
# Part 4:
# Exchange code with your partner and begin adding comments on improvements (save your original version)
# 
# Part 5:
# Return the code and create a comparison 
# 
# Part 6:
# Upload the code and comparison it to Canvas. 

# In[23]:


print("Welcome to the Dice Rolling Game!")
print("You and the computer will each roll a dice four times, and the one with the lowest number wins.")
active = True
while active:
    input("Press Enter to roll the dice...")
    user_roll1 = random.randint(1, 6)
    computer_roll1 = random.randint(1, 6)
        
    input("Press Enter to roll the dice again...")
    user_roll2 = random.randint(1, 6)
    computer_roll2 = random.randint(1, 6)
        
    input("Press Enter to roll the dice again...")
    user_roll3 = random.randint(1, 6)
    computer_roll3 = random.randint(1, 6)
        
    input("Press Enter to roll the dice again...")
    user_roll4 = random.randint(1, 6)
    computer_roll4 = random.randint(1, 6)
        
    usernum = [user_roll1, user_roll2, user_roll3, user_roll4]
    comnum = [computer_roll1, computer_roll2, computer_roll3, computer_roll4]
    print("You rolled: ",usernum)
    print("Computer rolled: ",comnum)
    
    usertot = user_roll1 + user_roll2 + user_roll3 + user_roll4
    comtot = computer_roll1 + computer_roll2 + computer_roll3 + computer_roll4
    print("Your total is: ",usertot)
    print("Computer total is: ",comtot)
    if usertot < comtot:
            print("Congratulations! You win!")
    elif usertot > comtot:
            print("Sorry, you lost. Better luck next time!")
    else:
            print("It's a tie!")
            
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
            print("Thanks for playing!")
            active = False
            


# ## Sample code
# Below you will find a Chat GPT generated Dice game.
# 
# Lets talk about it. 

# In[7]:


import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    print("You and the computer will each roll a dice, and the one with the higher number wins.")

    while True:
        input("Press Enter to roll the dice...")
        
        user_roll = roll_dice()
        computer_roll = roll_dice()

        print("You rolled:", user_roll)
        print("Computer rolled:", computer_roll)

        if user_roll > computer_roll:
            print("Congratulations! You win!")
        elif user_roll < computer_roll:
            print("Sorry, you lost. Better luck next time!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


# In[ ]:




