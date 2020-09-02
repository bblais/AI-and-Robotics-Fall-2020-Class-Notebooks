#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from mplturtle import *


# In[3]:


reset()
bgcolor('orange')

forward(50)

right(90)
pencolor('red')
pensize(10)
forward(50)

right(90)
pencolor('blue')
forward(50)

right(90)
pencolor('green')
forward(50)

write('hello',fontsize=20)

right(90)

pencolor('black')
pensize(1)
circle(75)


# In[4]:


animate(1)  # animate with 1 second for each step


# In[5]:


reset()

circle(50)


# In[6]:


animate(5,20)


# In[ ]:




