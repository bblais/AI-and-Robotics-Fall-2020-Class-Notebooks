#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


x=rand(1000)
v=randn(1000)


# In[3]:


plot(x)


# In[4]:


plot(x)
plot(v)


# In[6]:


subplot(2,1,1)
plot(x)

subplot(2,1,2)
plot(v)


# In[7]:


for i in range(4):
    subplot(4,1,i+1)
    
    imshow(rand(100,100))


# In[8]:


for i in range(4):
    subplot(2,2,i+1)
    
    imshow(rand(100,100))


# In[9]:


for i in range(4):
    subplot(1,4,i+1)
    
    imshow(rand(100,100))


# In[10]:


subplot(2,1,1)
plot(x)


subplot(2,2,3)
imshow(rand(100,100))

subplot(2,2,4)
imshow(rand(100,100))


# In[ ]:




