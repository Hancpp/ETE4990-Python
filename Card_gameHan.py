#!/usr/bin/env python
# coding: utf-8

# In[45]:


#
import random

class Player(object): #introduces player
    def __init__(self, name, health, hand, maps, rounds):
        self.name = name
        self.health = health
        self.hand = hand # This will be a list 
        self.maps = maps
        self.rounds = rounds 
        
    def hand_roll(self): #randomizer
        return random.randint(1,5)
    
    def end_round(self):
        self.rounds += 1 

    def card_sort(self): #sorts cards
        
        new_hand = []
        for item in self.hand:
            if item == 1:
                item = "wizard"
                new_hand.append("wizard")
            elif item == 2:
                item = "thief"
                new_hand.append("thief")
            elif item == 3:
                item = "warrior"
                new_hand.append("warrior")
            elif item == 4:
                item = "medic"
                new_hand.append("medic")
            elif item == 5:
                item = "Shield"
                new_hand.append("Shield")
                
        return new_hand
    
    def map_roll(self):
        return random.randint(1,3)


    def maps_sort(self):
        if self.maps == 1:
            return "castle"
        elif self.maps == 2:
            return "battle_Field"
        elif self.maps == 3:
            return "market"
        
            
    
    def player_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Hand: {self.hand}")
        print(f"Maps: {self.maps}")   
        print(f"Rounds: {self.rounds}")   
        
    def damage(self, target):
         target.health -= self.damage
            
    def computer_turn(self):
        count = 0
        for item in self.hand:
            count += 1
        
        choice = random.randint(1,count)
        picked_card = self.hand[choice]
        
        return picked_card
    
    def heal(self):
        self.health += 20
       

        
class warrior(Player):
    
    def __init__(self, name, health, hand, maps, rounds):
        super().__init__(name, health, hand, maps, rounds)
        if maps == "battle_Field":
            self.damage = 20
        else:
            self.damage = 10
            
    def do_damage(self, target):
        target.health -= self.damage
        
    def pop_warrior(self):
        self.hand.remove("warrior")
        
        
class thief(Player):
    
    def __init__(self, name, health, hand, maps, rounds):
        super().__init__(name, health, hand, maps, rounds)
        
            
    def steal(self, target):
        if maps == "market":
            for i in range(2):
                transfer = target.hand.pop()
                self.hand.append(transfer)
                print(f"{transfer} was stolen")
        else:
            transfer = target.hand.pop()
            self.hand.append(transfer)
            print(f"{transfer} was stolen")
                
    def pop_thief(self):
        self.hand.remove("thief")
        
class wizard(Player):
    
    def __init__(self, name, health, hand, maps, rounds):
        super().__init__(name, health, hand, maps, rounds)
        
            
    def poison_spell(self, target):
        rounds_to_poison = self.rounds + 1
    
        if maps == "castle":
                self.damage = 20
        else:
                self.damage = 10
        
        while self.rounds < rounds_to_poison:
            target.health -= self.damage
        
            

                
    def pop_wizard(self):
        self.hand.remove("wizard")         
        
        
class medic(Player): 
    
    def __init__(self, name, health, hand, maps, rounds):
        super().__init__(name, health, hand, maps, rounds)
        
            
  
    def pop_medic(self):
        self.hand.remove("medic")    
        
class shield(Player): 
    
    def __init__(self, name, health, hand, maps, rounds):
        super().__init__(name, health, hand, maps, rounds)
        
    def block_attack(self, target):
        target.damage = 0        
  
    def pop_shield(self):
        self.hand.remove("shield")    



#Player initialization         
name = input("Enter player name: ")
health = 100 
hand = []
maps = 0
rounds = 0
player = Player(name, health, hand, maps, rounds)


for i in range(5):
    hand.append(player.hand_roll())


player.hand = player.card_sort()

player.maps = player.map_roll()
player.maps = player.maps_sort()

player.player_stats()
print("\n\n")

#Computer Stats
print("Now getting Computer's Stats: ")
com_health = 100 
com_name = "Jarvis"
com_hand = []
com_maps = player.maps
computer = Player(com_name, com_health, com_hand, player.maps, rounds)

for i in range(5):
    com_hand.append(player.hand_roll())


computer.hand = computer.card_sort()
computer.player_stats()
print("\n")
        
active = True 
while active:
    
    choice = int(input("Please make a choice: 1) Make a move 2) End Turn 3) Display Stats"))
    if choice == 1:
        pick = input("Please pick a card: ")
        if pick == "warrior":
            if "warrior" in player.hand:
                warrior_card = warrior(player.name, player.health, player.hand, player.maps, player.rounds)
                warrior_card.do_damage(computer)
                warrior_card.pop_warrior()
                player.end_round()
                computer.end_round()
                player.player_stats()
                print("\n")
                computer.player_stats()
                print("\n")
            else:
                print("You do not have a warrior")
                
        if pick == "thief":
            if "thief" in player.hand:
                thief_card = thief(player.name, player.health, player.hand, player.maps, player.rounds)
                thief_card.steal(computer)
                thief_card.pop_thief()
                player.end_round()
                computer.end_round()
                player.player_stats()
                print("\n")
                computer.player_stats()
                print("\n")
            else:
                print("You do not have a thief")
                
        if pick == "wizard":
            if "wizard" in player.hand:
                wizzard_card = wizard(player.name, player.health, player.hand, player.maps, player.rounds)
                wizzard_card.poison_spell(computer)
                wizzard_card.pop_wizard()
                player.end_round()
                computer.end_round()
                player.player_stats()
                print("\n")
                computer.player_stats()
                print("\n")
            else:
                print("You do not have a wizard")
           
        if pick == "medic":
            if "medic" in player.hand:
                medic_card = medic(player.name, player.health, player.hand, player.maps, player.rounds)
                player.heal()
                medic_card.pop_medic()
                player.end_round()
                computer.end_round()
                player.player_stats()
                print("\n")
                computer.player_stats()
                print("\n")
            else:
                print("You do not have a medic")
                
        if pick == "shield":
            if "shield" in player.hand:
                shield_card = medic(player.name, player.health, player.hand, player.maps, player.rounds)
                shield_card.block_attack(computer)
                shield_card.pop_shield()
                player.end_round()
                computer.end_round()
                player.player_stats()
                print("\n")
                computer.player_stats()
                print("\n")
            else:
                print("You do not have a shield")
        else:
            print("Invalid Choice")
                
    card = computer.computer_turn()
    
    print(card)
   
            
    
    
    
    


    



# In[ ]:




