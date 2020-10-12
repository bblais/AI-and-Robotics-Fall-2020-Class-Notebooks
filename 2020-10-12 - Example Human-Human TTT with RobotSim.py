#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


from RobotSim373 import *


# In[3]:


def build(robot):    
    
    left=Box(robot,2,12,width=1,height=1,name='left')
    right=Box(robot,2,10,width=1,height=1,name='right')
    
    connect(left,right,'weld')  # revolves around the middle of the second object
    
    robot.current_force=0
    robot.current_force_angle=0
    robot.time_to_next_decision=0
    
    


# In[10]:


def act(t,robot):
    
    return


# In[42]:


env=Environment(image='images/TTT Board.png',linearDamping=10) 
robot=Robot(env)

build(robot)

pieces=[]
y=14
for i in range(4):
    pieces.append(Box(env,23,y,width=0.5,height=0.5))
    y-=0.8
    
for i in range(4):
    pieces.append(Box(env,23,y,width=0.5,height=0.5,color='r'))
    y-=0.8


run_sim(env,act,
        total_time=10,  # seconds
        dt=1/60,
        dt_display=.5,  # make this larger for a faster display
        figure_width=8,
        plot_orientation=False,
       )


# In[43]:


def move_to_location(move):
    row,col=move//3, move%3
    
    x=col*6+6
    y=13-5*row
    
    return x,y


# In[44]:


move_to_location(2)


# In[45]:


def move(piece,location):
    
    def act(t,robot):
        
        x,y=piece.x,piece.y
        tx,ty=location
        
        d=sqrt((tx-x)**2+(ty-y)**2)
        angle=degrees(arctan2((ty-y),(tx-x)))
        
        k=1
        piece.F=k*d
        piece.F_angle=angle
        
        robot.message=piece.F_angle
            
    return act
        


# In[46]:



run_sim(env,move(pieces[0],move_to_location(2)),
        total_time=10,  # seconds
        dt=1/60,
        dt_display=.5,  # make this larger for a faster display
        figure_width=8,
        plot_orientation=False,
       )


# In[47]:



run_sim(env,move(pieces[4],move_to_location(4)),
        total_time=10,  # seconds
        dt=1/60,
        dt_display=.5,  # make this larger for a faster display
        figure_width=8,
        plot_orientation=False,
       )


# In[ ]:




