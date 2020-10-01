#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[8]:


def initial_state():
    state=Board(3,5)
    
    state[4]=state[9]=state[14]=1
    
    return state


# In[ ]:





# In[9]:


state=initial_state()
state


# In[7]:


state.show_locations()


# In[ ]:




