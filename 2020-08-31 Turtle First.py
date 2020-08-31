#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('gui', 'tk')


# In[2]:


from turtle import *


# In[3]:


forward(50)


# In[4]:


forward(100)


# In[10]:


reset()


# # Draw a square

# In[5]:


reset()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[6]:


reset()
pencolor("red")
print("start")
for i in range(4):
    print("inside the loop")
    forward(50)
    right(90)    

print("done.")


# In[8]:


length=80

reset()
pencolor("red")
print("start")
for i in range(4):
    print("inside the loop")
    forward(length)
    right(90)    

print("done.")


# left off here after 1st class

# In[9]:


def square():
    for i in range(4):
        forward(50)
        right(90)


# In[10]:


reset()
square()


# In[16]:


reset()
square()

penup()
forward(100)
pendown()


square()


# In[19]:


def square(size):
    # as if we had
    # size=50  when we call square(50)
    for i in range(4):
        forward(size)
        right(90)
        
def space(length):
    penup()
    forward(length)
    pendown()
    


# In[22]:


reset()
square(50)

# penup()
# forward(100)
# pendown()

space(80)

square(10)


# In[24]:


reset()
for i in range(10):
    print("i has the value",i)
    square(20)
    space(30)


# In[27]:


reset()
speed("fastest")
for i in range(10):
    print("i has the value",i)
    
    if i>5:
        print("red is the new black")
        pencolor("red")
    else:
        pencolor("black")
    
    square(20)
    space(30)


# In[37]:


count=0
for i in range(3):
    for j in range(4):
        print(i,j)
        count=count+1
        
print("the final countdown ",count)


# In[29]:


a=5


# In[30]:


a


# In[33]:


a=a+3


# In[34]:


a


# In[39]:


reset()
for i in range(5):
    forward(50)
    left(5)


# In[40]:


reset()
for i in range(5):
    forward(50)
    left(170)


# In[41]:


def draw_shape(type_of_shape):
    
    if type_of_shape==4 or type_of_shape=='square':
        square(50)


# In[42]:


draw_shape(4)


# In[43]:


draw_shape('square')


# In[44]:


reset()


# How would I draw the letter "B"?
# 
# * vertical line (and back)
# * half-circle for the top part?  - is there a circle function?
# * half circle for the bottom part?

# In[52]:


reset()

right(90)
forward(100)
backward(100)
left(90)

right(90)
forward(50)
left(90)
circle(25,180)

# right(90)
# forward(100)
# left(90)
# circle(25,180)

# now I'm facing to the left
left(90)
forward(100)
left(90)
circle(25,180)

# return back
right(90)
forward(50)
right(90)


# In[53]:


def letter_B():
    right(90)
    forward(100)
    backward(100)
    left(90)

    right(90)
    forward(50)
    left(90)
    circle(25,180)

    # now I'm facing to the left
    left(90)
    forward(100)
    left(90)
    circle(25,180)

    # return back
    right(90)
    forward(50)
    right(90)    


# In[54]:


reset()
letter_B()


# alternating values

# In[56]:


a=5
b=10

for i in range(5):
    print("a is ",a,"and b is ",b)
    
    a,b=b,a


# In[59]:


reset()
new_direction,old_direction=left,right
new_color,old_color="red","black"

for i in range(10):
    pencolor(new_color)
    forward(20)
    new_direction(45)
    
    new_direction,old_direction=old_direction,new_direction
    new_color,old_color = old_color,new_color


# In[60]:


5+5


# In[62]:


5 % 3  # remainder


# In[ ]:





# In[63]:


reset()
new_direction,old_direction=left,right

for i in range(10):
    if i % 2 == 0:
        pencolor("red")
    else:
        pencolor("black")
    
    
    forward(20)
    new_direction(45)
    
    new_direction,old_direction=old_direction,new_direction


# In[64]:


def iseven(N):
    if N % 2 == 0:
        return True
    else:
        return False


# In[66]:


iseven(2)


# In[ ]:





# In[67]:


reset()
new_direction,old_direction=left,right

for i in range(10):
    if iseven(i):
        pencolor("red")
    else:
        pencolor("black")
    
    
    forward(20)
    new_direction(45)
    
    new_direction,old_direction=old_direction,new_direction


# In[ ]:





# In[68]:


a=6


# In[69]:


a


# In[70]:


b=5.6


# In[71]:


b


# In[72]:


type(a)


# In[73]:


type(b)


# In[74]:


3/2


# In[79]:


23.1**500


# In[80]:


23**500


# In[81]:


b=[1,4,6,8,4]


# In[82]:


b


# In[83]:


c=['hello',5,[4,5,6]]


# In[84]:


b[0]


# In[85]:


b[2]


# In[86]:


b[3]


# In[87]:


b


# In[88]:


for value in b:
    print("value",value)


# In[89]:


list(range(10))


# In[90]:


c


# In[91]:


for value in c:
    print("value",value)


# In[92]:


b


# In[93]:


b[-1]


# In[94]:


b[-2]


# In[95]:


b[1:4]


# In[96]:


b[1:]


# In[97]:


board=[ 'X','','O',]


# In[102]:


board = [1,0 ,2, 0 ,0, 0, 0,0,0]


# In[103]:


board


# In[104]:


len(board)


# In[109]:


i=9


# In[111]:


if i>=4 and i<9:
    print("between")
else:
    print("not there")


# In[5]:


from pylab import rand


# In[6]:


def done():
    pass


# In[1]:


get_ipython().run_line_magic('gui', 'tk')
from turtle import *
from pylab import rand
def done():
    pass


# In[2]:


try:
    reset()
    for i in range(1000):
        forward(rand()*50)
        right(rand()*90)
        bob
except:
    done()
    raise
    


# In[ ]:




