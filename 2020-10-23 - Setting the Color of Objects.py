#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


from RobotSim373 import *


# In[3]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4,
             name='bob')   # default size is 1,1

    box2=Box(robot,
             x=3,
             y=6,
             name='sally')   # default size is 1,1
    
    circle=Disk(robot,
               x=2,
               y=5,
               radius=0.4,
               name='center')
    
    connect(box1,box2,'weld')
    connect(box1,circle,'weld')
    
def act(t,robot):
    robot['sally'].F=0.4
    robot['bob'].F=0.4


# In[5]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)

for j in range(10):
    for i in range(10):
        Disk(env,
            x=10+j,
            y=3+0.5*i,
            radius=.2,
            density=0.01)



run_sim(env,act,
        total_time=60,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
       )


# # Setting the color 
# 
# You can set the color value as an argument when you make the object, or afterward directly on the object.  You can set the color of the individual pieces of the robot or, if you prefer, set the color of the robot and all of the pieces will have that same color.
# 
# A list of colors can be found here:  https://matplotlib.org/3.3.1/gallery/color/named_colors.html
# 
# You can also use the hex format '#c2a245', or a tuple of rgb  (0.3,0.5,0.9)

# In[8]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)

for j in range(10):
    for i in range(10):
        Disk(env,
            x=10+j,
            y=3+0.5*i,
            radius=.2,
            density=0.01,
            color='r')    # <----- set the color to red



run_sim(env,act,
        total_time=60,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
       )


# In[11]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)

robot.color='cyan'      # <----- make the robot a different color

for j in range(10):
    for i in range(10):
        Disk(env,
            x=10+j,
            y=3+0.5*i,
            radius=.2,
            density=0.01,
            color=(rand(),rand(),rand()),     # <----- set the color to a random r,g,b
            )



run_sim(env,act,
        total_time=60,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
       )


# In[ ]:




