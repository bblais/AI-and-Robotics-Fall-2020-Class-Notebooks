#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# For the robot to reconstruct the state of the game:
# 
# 1. take picture of the board (robot.take_picture('board.jpg'))
# 2. slice the image into subimages - how many sub images?  num rows x num cols
# 3. for each sub image --> interpret the image piece #1, piece #2, or empty. 
#    need to classify the sub image into a category
# 4. make an empty state with num row, num cols.  go through each square, 
#     recognize the piece from the subimage, 
#     then assign state[square]=category we detected
# 5.  goal  e.g. state = [ 0 0 0 ; 0 1 0 ; 2 1 0]

# In[2]:


x1=rand(10)


# In[3]:


x1


# In[4]:


x1.shape


# In[5]:


x2=rand(3,5)


# In[6]:


x2


# In[7]:


x2[0,1]


# In[8]:


x2[0,1:4]


# In[9]:


list(range(1,4))


# In[11]:


x2[1:3,1:4]


# In[ ]:





# In[ ]:





# In[14]:


x2.shape


# In[15]:


x1


# In[19]:


x1[2:8],x1[8:]


# In[20]:


x1[2:]


# In[21]:


x1[:5]


# In[22]:


x2


# In[24]:


x2[1:5]


# In[25]:


x2[1:5].shape


# In[29]:


x2


# In[27]:


x2[0:1,2:4]


# In[30]:


x2[0,2:4]


# In[28]:


x2[0:2,2:4]


# In[31]:


x2


# In[32]:


x2[:,3]


# In[33]:


x2[1,:]


# In[37]:


x3=rand(5,4,3)
x3.shape


# In[38]:


x3


# In[39]:


x5=rand(5,4,3,4,3)


# In[40]:


x5


# In[41]:


x3


# In[42]:


x3[:,:,0]


# In[43]:


x3[:,:,0].shape


# In[12]:


im=imread('images/dogs.jpg')


# In[13]:


im.shape


# In[14]:


imshow(im)


# In[5]:


imshow(im[:,:,0],cmap=cm.gray)
colorbar()


# In[74]:


imshow(im[:,:,1],cmap=cm.gray)
colorbar()


# In[75]:


imshow(im[:,:,2],cmap=cm.gray)
colorbar()


# In[76]:


imshow(im)


# In[15]:


subimage=im[0:600,400:800,:]
imshow(subimage)


# In[ ]:





# In[ ]:





# In[16]:


count=1
width=370
height=580

offset_x=0
offset_y=0

for row in range(2):
    for col in range(3):
        
        start_col=col*width+offset_x
        end_col=(col+1)*width+offset_y
        
        start_row=row*height
        end_row=(row+1)*height
        
        subimage=im[start_row:end_row,start_col:end_col,:]
        
        subplot(2,3,count)
        imshow(subimage)
        
        
        count+=1


# In[ ]:





# In[ ]:





# In[6]:


subimage = im[550:,400:820,:]
imshow(subimage)


# In[80]:


imsave('images/onedog.jpg',subimage)


# In[ ]:





# In[62]:


im=imread('images/dogs2.png')


# In[57]:


imshow(im)


# In[58]:


im.shape


# In[59]:


imshow(im[:,:,3],cmap=cm.gray)
colorbar()


# In[60]:


imshow(im[:,:,0],cmap=cm.gray)
colorbar()


# In[ ]:




