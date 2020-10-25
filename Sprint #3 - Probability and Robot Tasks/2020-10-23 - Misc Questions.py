#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(4,5)


# In[3]:


state


# In[5]:


state.show_locations()


# In[6]:


def valid_moves(state,player):
    
    moves=[]
    
    for i in range(5):
        if state[0,i]==0:
            moves.append(i)
            
    return moves


# In[7]:


def update_state(state,player,move):
    
    # run through the rows, from the bottom up, at the column given by move
    # when you reach a zero, place the piece in that square
    
    pass


# In[ ]:




