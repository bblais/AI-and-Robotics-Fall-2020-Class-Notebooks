#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')
from classy import *


# ## make a fake image data set without square images

# In[4]:


for i in range(100):
    im=rand(20,10,3)*0.3
    imsave('test images/cat/%d.jpg' % i,im)
imshow(im)


# In[5]:


for i in range(100):
    im=rand(20,10,3)*0.3+.6
    imsave('test images/dog/%d.jpg' % i,im)
imshow(im)


# In[6]:


images=image.load_images('test images/')


# In[7]:


data=image.images_to_vectors(images)


# In[8]:


data.vectors/=255


# In[9]:


data_train,data_test=split(data,test_size=0.2)


# In[10]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[12]:


C.means.shape


# In[13]:


p = C.means[0].reshape(20,10,3)


# In[15]:


imshow(p)


# In[16]:


p = C.means[1].reshape(20,10,3)


# In[17]:


imshow(p)


# In[ ]:




