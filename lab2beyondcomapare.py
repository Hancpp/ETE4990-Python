#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ef dice_game(user_choice):
    import random 
    active = True
    while active:
        if user_choice == "yes":
                user_score = [] 
                com_score = []
                count = 0
                input("Press Enter to roll the dice...")
                while count != 4: 
                    
                    user_roll = random.randint(1, 6)
                    user_score.append(user_roll)  
                    computer_roll = random.randint(1, 6)
                    com_score.append(computer_roll) 
                    count += 1 
                
                usertot = sum(user_score)
                comtot = sum(com_score)
                usernum = {'Your roll':  user_score, 'Your total': usertot}
                comnum = {'Computer roll': com_score,'Computer total': comtot}
                
                print(usernum)
                print(comnum)
                
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
        else:
                print("you selected no")
                active = False
        
       

