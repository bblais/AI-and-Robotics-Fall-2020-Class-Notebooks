#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


from RobotSim373 import *


# In[3]:


def build(robot):
    bob=Box(10,5,width=3,height=1)


# In[4]:


def act(t,robot):
    robot['bob'].F=4


# In[ ]:




