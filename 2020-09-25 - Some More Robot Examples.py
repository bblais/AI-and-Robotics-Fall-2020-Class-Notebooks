#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from RobotSim373 import *


# In[15]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally')

    robot.storage=Storage()
    
    return robot
    
def act(t,robot):
    
    if t==0.0:
        robot['sally'].F=1
    
    
    if t<7:
        robot['sally'].F=1
    else:
        robot['sally'].F=-1
    
    color=robot['sally'].read_color()
    robot.storage += t,color[0],color[1],color[2]
    
    
    


# In[16]:


env=Environment(image='images/black red and blue.png') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
        figure_width=8,
       )


# In[17]:


t,r,g,b=robot.storage.arrays()
plot(t,r,'r')
plot(t,g,'g')
plot(t,b,'b')


# In[24]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally')

    robot.storage=Storage()
    
    return robot
    
def act(t,robot):
    
    if t==0.0:
        robot['sally'].F=1
    
    
    color=robot['sally'].read_color()
    
    r,g,b,a=color
    if b>.1:
        robot['sally'].F=-robot['sally'].F
        
    
    
    robot.storage += t,r,g,b
    
    
    


# In[25]:


env=Environment(image='images/black red and blue.png') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=30,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
        figure_width=8,
       )


# In[28]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally')

    robot.storage=Storage()
    
    return robot
    
def act(t,robot):
    
    if t==0.0:
        robot['sally'].F=1
    
    
    color=robot['sally'].read_color()
    
    r,g,b,a=color
    if b>.4:
        robot['sally'].F=-1
    elif b>.1:
        robot['sally'].F=1
    
    
    robot.storage += t,r,g,b
    
    
    


# In[29]:


env=Environment(image='images/black red and blue.png') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=30,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
        figure_width=8,
       )


# In[ ]:




