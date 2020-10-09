#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Rules of the Game

# - before each roll, we can either choose to roll or hold
# - roll a die
#     - if it is a 1, turn score goes to zero (or 1), the turn stops and goes to the next player
#     - if not a 1, add to the turn score the number rolled, and have another turn
# - hold
#     - turn score gets added to my current score
#     - goes to the next player
# - first to 21 wins

# 1. what is a move?  (how do we represent it, what are possibilities)
#     - "roll", "hold"
# 2. what is a state?  (how do we represent it, what are possibilities)
#     - your current score, their current score, turn score

# In[2]:


def valid_moves(state,player):
    return ["roll","hold"]

def initial_state():
    # your current score, their current score, turn score
    return [0,0,0]


# In[3]:


def show_state(state):
    print("Player 1 score is ",state[0])
    print("Player 2 score is ",state[1])
    print("Turn score is ",state[2])    


# In[4]:


def win_status(state,player):
    
    # playing until 21
    max_score=21
    
    if player==1:
        current_score=state[0]
        other_score=state[1]
    else:
        current_score=state[1]
        other_score=state[0]
        
    turn_score=state[2]
    
    if current_score+turn_score>=max_score:
        return 'win
    
    


# In[5]:


def update_state(state,player,move):
    
    # if hold, update the scores
    
    # if roll, then random number 1-6, if 1, ....
    # update turn score
    new_state=state
    
    if move=='hold':
        
        # state[player-1]+=state[2]
        
        if player==1:
            new_state[0]+=state[2]  # add the turn score to player 1's current score
        else:
            new_state[1]+=state[2]  # add the turn score to player 1's current score
        
        new_state[2]=0  # reset the turn score
        
    else:  #  roll
        dice=random.randint(1,6)
        
        if dice==1:
            new_state[2]=0  # reset the turn score
        else:
            new_state[2]+=dice
            
    
    return new_state


# In[6]:


def repeat_move(state,player,move):
    turn_score=state[2]
    
    if turn_score>0:
        return True
    
    return False
    


# In[10]:


def human_move(state,player):
    print("Player ",player)
    s=input("hold or roll?")
    
    if s[0]=='h':
        return 'hold'
    else:
        return 'roll'
    
human_agent=Agent(human_move)


# In[9]:


human_move(None,1)


# In[11]:


g=Game()
g.run(human_agent,human_agent)


# In[ ]:




