#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().run_line_magic('pylab', 'inline')


# In[8]:


from mplturtle import *


# In[9]:


reset()
forward(50)

right(90)
pencolor('red')
forward(50)

right(90)
pencolor('blue')
forward(50)

right(90)
pencolor('green')
forward(50)

right(90)


# In[10]:


animate(1)  # animate with 1 second between


# In[ ]:




