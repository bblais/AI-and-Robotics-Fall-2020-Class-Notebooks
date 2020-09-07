#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


board=Board(5,5)


# In[3]:


for i in range(25):
    board[i]=i
    
print(board)


# In[4]:


board.rc_from_index(11)


# In[5]:


board.index_from_rc(2,1)


# In[6]:


board=Board(8,8)
board.show_locations()


# In[7]:


board


# In[8]:


board[34]=1


# In[9]:


board


# In[12]:


def find_the_one(board):
    
    for i in range(64):
        if board[i]==1:
            return i
        
def find_the_ones(board):
    
    locations=[]
    
    for i in range(64):
        if board[i]==1:
            locations.append(i)
                
    return locations


# In[14]:


find_the_one(board)


# In[15]:


find_the_ones(board)


# In[16]:


board[5]=1


# In[17]:


find_the_ones(board)


# In[18]:


find_the_one(board)


# In[20]:


row,col=board.rc_from_index(34)


# In[21]:


row


# In[22]:


col


# In[23]:


b=Board(3,4)


# In[24]:


b


# In[26]:


b[7]=2


# In[27]:


b


# In[28]:


b[1,2]=5


# In[29]:


b


# In[30]:


b.show_locations()


# In[ ]:




