#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from RobotSim373 import *


# In[11]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             angle=45,
             name='right')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4  
    robot['right'].F_angle=-robot['right'].angle

    if t<10:
        robot.message='Early'
    else:
        robot.message='Late'


# In[13]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[9]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             name='right')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4    

    robot.message=robot['right'].position


# In[11]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)
build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[12]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             name='right')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4    

    robot.message=robot['right'].position


# In[13]:


env=Environment(image='images/black_stripes.jpg')  # size of the environment
robot=Robot(env)
build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[14]:


def build(robot):
    box1=Box(robot,
             x=3,
             y=4.5,
             name='right')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4    

    robot.message=robot['right'].read_color()


# In[16]:


env=Environment(image='images/black_stripes.jpg')  # size of the environment
robot=Robot(env)
build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[25]:


def build(robot,start_x=4):
    box1=Box(robot,
             x=start_x,
             y=rand()*20+2,
             name='right')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4    

    robot.message=robot['right'].read_color()


# In[29]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)


build(robot,20)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[30]:


def build(robot):
    box1=Box(robot,
             x=12,
             y=12,
             angle=rand()*360,
             name='right')   # default size is 1,1
    
def act(t,robot):
    robot['right'].F=0.4    

    robot.message=robot['right'].read_color()


# In[36]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)


build(robot)

run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[41]:


def build(robot):
    box1=Box(robot,
             x=2.5,
             y=3,
             width=1,
             height=0.2,
             angle=90,
             name='bob')   # default size is 1,1
    box2=Box(robot,
             x=2.5,
             y=5,
             width=1,
             height=0.2,
             angle=90,
             name='sally')   # default size is 1,1
    disk1=Disk(robot,
             x=1.5,
             y=4,
             radius=0.8,
             name='frank')   # default size is 1,1

    connect(disk1,box1,'weld')
    connect(disk1,box2,'weld')
    
def act(t,robot):
    robot['bob'].F=0.01
    robot['sally'].F=0.01
    
    if t<10:
        robot['frank'].F=0.4
    elif t<20:
        robot['frank'].F=-0.4
    else:
        robot['frank'].F=0.4
        
    


# In[42]:


env=Environment(24,24)  # size of the environment
robot=Robot(env)


build(robot)

run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
       )


# In[ ]:




