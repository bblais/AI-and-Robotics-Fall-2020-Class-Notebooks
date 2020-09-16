#!/usr/bin/env python
# coding: utf-8

# ## To Install
# 
# * from Anaconda prompt do:
# 
# ```
# pip install Box2d
# 
# pip install pyglet
# 
# pip install "git+git://github.com/bblais/RobotSim373" --upgrade
# ```

# ## Tour

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from RobotSim373 import *


# * Physics is simulated in 2D (top down perspective)
# * Everything is made up of rectangles or circular disks
# * There are objects associated with the robot and objects which just exist in the world
# * Objects can be connected in different ways:
#     1. weld
#     2. distance
#     3. (others to come)
# * Robot objects can have a force applied to them, always in the direction they face

# In[18]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             name='right')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4


# In[ ]:





# In[19]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
robot=build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[20]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
robot=build(robot)

# put in some objects

obj1=Box(env,  #<--- env, not robot
         x=15,
         y=4,
         angle=10,
         width=2,height=1)



run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[21]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             name='right')   # default size is 1,1
    box2=Box(robot,
             x=3,
             y=6,
             name='left')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4
    robot['left'].F=0.4


# In[23]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
robot=build(robot)

# put in some objects

obj1=Box(env,  #<--- env, not robot
         x=15,
         y=4,
         angle=10,
         width=2,height=1)



run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[24]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             name='right')   # default size is 1,1
    box2=Box(robot,
             x=3,
             y=6,
             name='left')   # default size is 1,1
    
    connect(box1,box2,'weld')
    
def act(t,robot):
    robot['right'].F=0.4
    robot['left'].F=0.4


# In[25]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
robot=build(robot)

# put in some objects

obj1=Box(env,  #<--- env, not robot
         x=15,
         y=4,
         angle=10,
         width=2,height=1)



run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[26]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             name='right')   # default size is 1,1
    box2=Box(robot,
             x=3,
             y=6,
             name='left')   # default size is 1,1
    
    connect(box1,box2,'distance')
    
def act(t,robot):
    robot['right'].F=0.4
    robot['left'].F=0.4


# In[27]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
robot=build(robot)

# put in some objects

obj1=Box(env,  #<--- env, not robot
         x=15,
         y=4,
         angle=10,
         width=2,height=1)



run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[28]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
robot=build(robot)

# put in some objects

obj1=Disk(env,  #<--- env, not robot
         x=15,
         y=4,
         angle=10,
         radius=1)



run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[ ]:




