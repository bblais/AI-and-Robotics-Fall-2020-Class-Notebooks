#!/usr/bin/env python
# coding: utf-8

# * linearDamping in environment
# * taking a picture

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from RobotSim373 import *


# In[3]:


def build(robot):

    left=Box(robot,2,12,width=1,height=1,name='left')
    right=Box(robot,2,10,width=1,height=1,name='right')

    connect(left,right,'weld')  # revolves around the middle of the second object



# In[12]:


def act(t,robot):
        
    if robot['left'].x<10:
        robot['left'].F=.2
        robot['right'].F=.2
    else:
        robot['left'].F=0
        robot['right'].F=0
        


# In[14]:


env=Environment(image='images/black red and blue.jpg')
robot=Robot(env)
build(robot)

for i in range(10):
    Box(env,x=rand()*15+5,
            y=rand()*13+2.5,
        width=0.5,height=0.5,angle=rand()*360)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
        figure_width=8,
       )


# In[ ]:





# In[ ]:




