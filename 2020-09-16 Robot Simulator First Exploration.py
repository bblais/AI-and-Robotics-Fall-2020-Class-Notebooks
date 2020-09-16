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

# # Tour

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

# In[4]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             name='right')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4


# In[6]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=2,  # make this larger for a faster display
       )


# In[7]:


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
    robot['left'].F=0.2


# In[10]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
       )


# In[18]:


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


# In[24]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


Disk(env,
    x=10,
    y=5,
    radius=0.5)

Box(env,
    x=12,
    y=7,
    width=4,
    height=2,
    angle=30,)


run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
       )


# In[34]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4,
             name='right')   # default size is 1,1

    box2=Box(robot,
             x=3,
             y=6,
             name='left')   # default size is 1,1
    
    circle=Disk(robot,
               x=2,
               y=5,
               radius=0.4,
               name='center')
    
    connect(box1,box2,'weld')
    connect(box1,circle,'weld')
    
def act(t,robot):
    robot['right'].F=0.4
    robot['left'].F=0.4


# In[36]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


Disk(env,
    x=10,
    y=5,
    radius=3)

Box(env,
    x=12,
    y=7,
    width=4,
    height=0.1,
    angle=30,)


run_sim(env,act,
        total_time=60,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
       )


# In[37]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)


Disk(env,
    x=10,
    y=5,
    radius=3,
    density=0.01)

Box(env,
    x=12,
    y=7,
    width=4,
    height=0.1,
    angle=30,)


run_sim(env,act,
        total_time=60,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
       )


# In[ ]:




