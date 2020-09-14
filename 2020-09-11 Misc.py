#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(3,5)


# In[3]:


max_row,max_col=state.shape


# In[4]:


max_row


# In[5]:


max_col


# In[ ]:


def valid_moves(state,player):
    max_row,max_col=state.shape
    
    moves=[]
    for i in range(max_row*max_col):
        if stare[i]==0:
            moves.append(i)
            
    return moves


# In[6]:


state=Board(3,3,3)
state


# In[ ]:




