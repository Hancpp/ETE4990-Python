#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
            

