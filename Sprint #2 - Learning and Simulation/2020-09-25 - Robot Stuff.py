#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from RobotSim373 import *


# In[17]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally')

    robot.storage=Storage()
    
    robot.a=5
    
    return robot
    
def act(t,robot):
    
    if t==0.0:
        robot['sally'].F=1
    
    
    if t<3:
        robot['sally'].F=1
    else:
        robot['sally'].F=0
    
    color=robot['sally'].read_color()
    
    robot.storage += t,robot['sally'].x,robot['sally'].vx
    
    


# In[18]:


env=Environment(image='images/black red and blue.png') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
        figure_width=8,
       )


# In[19]:


t,x,v=robot.storage.arrays()


# In[20]:


plot(t,x)


# In[22]:


plot(t,v)


# In[31]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally',
        linearDamping=0)

    robot.storage=Storage()
    
    robot.a=5
    
    return robot
    
def act(t,robot):
        
    if t<10:
        
        a=0.15
        m=robot.mass
        
        robot['sally'].F=m*a
    else:
        robot['sally'].F=0
    
    color=robot['sally'].read_color()
    
    robot.storage += t,robot['sally'].x,robot['sally'].vx
    
    


# In[32]:


env=Environment(image='images/black red and blue.png') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
        figure_width=8,
       )


# In[33]:


t,x,v=robot.storage.arrays()


# In[34]:


plot(t,v)


# If I want to have the robot take 10 seconds to reach 1.5 m/s, that would be an accleration of:

# In[30]:


a=1.5/10
a


# Force and acceleration are related, with
# 
# $$
# F=ma
# $$

# In[29]:


robot.mass


# If I want to travel some distance, $d$, then these are related
# 
# $$
# d = d_o + v_o t + \frac{1}{2} a t^2
# $$
# 
# solve for a,
# 
# $$
# a = 2\frac{d-d_o - v_o t}{t^2}
# $$

# In[ ]:





# In[44]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally',
        linearDamping=5)

    robot.storage=Storage()
    
    robot.a=5
    
    return robot
    
def act(t,robot):
        
    
    t_rem=1
    
    a=2*(15-robot['sally'].x - robot['sally'].vx*t_rem)/(t_rem**2)
        
    if t<10:
        
        m=robot.mass
        
        robot['sally'].F=m*a
    else:
        robot['sally'].F=0
    
    color=robot['sally'].read_color()
    
    robot.storage += t,robot['sally'].x,robot['sally'].vx
    
    


# In[48]:


env=Environment(image='images/black red and blue.png') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=None,  # make this larger for a faster display
        figure_width=8,
       )


# In[49]:


t,x,v=robot.storage.arrays()


# In[50]:


plot(t,x)


# # a little about color

# In[58]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally')

    robot.storage=Storage()
    
    robot.a=5
    
    return robot
    
def act(t,robot):
    
    
    if t<7:
        robot['sally'].F=1
    else:
        robot['sally'].F=-1
    
    color=robot['sally'].read_color()
    
    r,g,b,a=color
    
    robot.storage += t,r,g,b
    
    


# In[59]:


env=Environment(image='images/black red and blue.png') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=20,  # seconds
        dt=1/60,
        dt_display=0.5,  # make this larger for a faster display
        figure_width=8,
       )


# In[60]:


t,r,g,b=robot.storage.arrays()


# In[64]:


plot(t,r,'r')
plot(t+.1,b,'b')
plot(t+.2,g,'g')


# In[70]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally')

    robot.storage=Storage()
    
    robot.a=5
    
    return robot
    
def act(t,robot):
    
    if t==0.0:
        robot['sally'].F=1
        
    color=robot['sally'].read_color()
    r,g,b,a=color

    if b>0.5:
        robot['sally'].F=-1
    elif b>.1:
        robot['sally'].F=1
        
    
    
    robot.storage += t,r,g,b,a
    
    


# In[71]:


env=Environment(image='images/black red and blue.png') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
        figure_width=8,
       )


# In[72]:


t,r,g,b,a=robot.storage.arrays()


# In[73]:


plot(t,r,'r')
plot(t+.1,b,'b')
plot(t+.2,g,'g')


# In[74]:


plot(t,a)


# In[76]:


def build(robot):


    Disk(robot,
        x=10,
        y=10,
        radius=1,
        name='sally')

    robot.storage=Storage()
    
    robot.a=5
    
    return robot
    
def act(t,robot):
    
    if t==0.0:
        robot['sally'].F=1
        
    color=robot['sally'].read_color()
    r,g,b=color

    if b>0.5:
        robot['sally'].F=-1
    elif b>.1:
        robot['sally'].F=1
        
    
    
    robot.storage += t,r,g,b
    
    


# In[78]:


env=Environment(image='images/black red and blue.jpg') 
robot=Robot(env)

robot=build(robot)

run_sim(env,act,
        total_time=40,  # seconds
        dt=1/60,
        dt_display=1,  # make this larger for a faster display
        figure_width=8,
       )


# In[79]:


t,r,g,b=robot.storage.arrays()


# In[80]:


plot(t,r,'r')
plot(t+.1,b,'b')
plot(t+.2,g,'g')


# In[ ]:




