#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from mplturtle import *


# In[4]:


reset()

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
right(90)


# In[16]:


def down_and_over():
    penup()
    right(90)
    forward(80)
    right(90)
    forward(300)
    right(90)
    right(90)
    pendown()    


# In[15]:


reset()

for j in range(3):
    
    for i in range(4):
        forward(50)
        right(90)

    penup()
    forward(100)
    pendown()

penup()
right(90)
forward(80)
right(90)
forward(300)
right(90)
right(90)
pendown()

for j in range(3):
    
    for i in range(4):
        forward(50)
        right(90)

    penup()
    forward(100)
    pendown()


# In[18]:


reset()

for j in range(3):
    
    for i in range(4):
        forward(50)
        right(90)

    penup()
    forward(100)
    pendown()

down_and_over()

for j in range(3):
    print(j)
    for i in range(4):
        forward(50)
        right(90)

    penup()
    forward(100)
    pendown()


# In[ ]:




