#!/usr/bin/env python
# coding: utf-8

# In[57]:


"""
This code is broken!
Daniel had too many beers and forgot how programming works
ribbit ribbit
This is not the most efficient implementation 
its up to you if you want to rewrite the whole program
Good luck!
"""
from random import randint
from IPython.display import clear_output

t = ["Rock","Paper", "Scissors"]

def main():   
    computer = t[randint(0,2)]
    while True:
        player = input("Rock, Paper or Scissors?")
        if ((player == "Paper") or (player == "paper") or (player == "Rock") or (player == "rock") or (player == "Scissors") or (player == "scissors")):
            if player == computer:
                print("Computer uses ", computer)
                print("Tie!")
                break
            elif player == "Paper" or "paper":
                if computer == "Rock":
                    print("You win! Computer uses ", computer, "and you cover it!")
                    break
                else:
                    print("You lose... Computer uses ", computer, "and it cuts paper!")
                    break
            elif player == "Rock" or player == "rock":
                if computer == "Paper":
                    print("You lose! Computer uses ", computer, " and covers you!")
                    break
                else:
                    print("You win! Computer uses ", computer, " and you smash them!")
                    break
            elif player == "Scissors" or "scissors":
                if computer == "Rock" or player == "rock":
                    print("You lose... Computer uses ", computer, " and smashes you.")
                    break
                else:
                    print("You win! Computer uses ", computer, " and you cut it!")
                    break
        else:
            print("Check your spelling!")

main()            
while True:
    NewGame = input('Do you want to play again?')
    if NewGame == 'y' or NewGame =='yes' or NewGame =='Y':
        print('-----------------------------------')
        clear_output()
        main()
    else:
        clear_output()
        print('Game Over')
        break
            
                    
                    



# In[51]:





# In[ ]:




