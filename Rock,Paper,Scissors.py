#!/usr/bin/env python
# coding: utf-8

# In[32]:


from random import choice
choices=["Rock","Paper","Scissors"]
computer=choice(choices)
player=input("Please enter either rock,paper,scissors: ").capitalize()
print(f"You chose:  {player} ")
print(f"computers choice: {computer}".capitalize())



while True:
    if player==computer:
        print("That's a draw 😁.Jaribu tena my guy😂")
        
    elif player=="Scissors" and computer=="Paper":
        print("You Won😎.Wewe ni mzii")
        
    elif player=="Paper" and computer=="Rock":
        print("You won😊.Cool Cool😎")
        
    elif player=="Rock" and computer=="Scissors":
        print ("You won😍.Good Good")
        
    else:
        print("You lost dumbhead😒.Sasa wewe")
        
    break


# In[ ]:




