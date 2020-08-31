#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('gui', 'tk')


# In[7]:


from turtle import *


# In[8]:


forward(50)


# In[9]:


forward(100)


# In[10]:


reset()


# # Draw a square

# In[15]:


reset()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[17]:


reset()
pencolor("red")
print("start")
for i in range(4):
    print("inside the loop")
    forward(50)
    right(90)    

print("done.")


# In[19]:


length=200

reset()
pencolor("red")
print("start")
for i in range(4):
    print("inside the loop")
    forward(length)
    right(90)    

print("done.")


# In[ ]:




