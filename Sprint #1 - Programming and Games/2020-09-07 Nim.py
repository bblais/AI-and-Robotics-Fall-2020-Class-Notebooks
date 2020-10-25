#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# # Nim
# 
# Rules:
# 
# 1. start with 21 sticks -- state = number of sticks
# 2. turns alternate taking 1,2, or 3 sticks
# 3. player taking last stick loses

# In[2]:


def initial_state():
    return 21

def show_state(state):
    print("There are ",state,"sticks.")
    
def valid_moves(state,player):
    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]
    
def update_state(state,player,move):
    # move = number of sticks to pick up
    new_state=state-move # remove the sticks
    return new_state

def win_status(state,player):
    if state==0:
        return 'lose'
    elif state==1:
        return 'win'
    else:
        return None
    
    # there is no stalemate


# In[5]:


def human_move(state,player):
    print("Player ",player)
    move=int(input("How many sticks?"))
    return move

human_agent=Agent(human_move)


# In[7]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move
random_agent=Agent(random_move)


# In[6]:


g=Game()
g.run(human_agent,human_agent)


# In[ ]:




