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


# In[45]:


images=image.load_images('armen images/')


# In[46]:


data=image.images_to_vectors(images)
data.vectors/=255


# In[47]:


data_train,data_test=split(data,test_size=0.2)


# In[48]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# # Prototypes
# 
# These prototypes look all the same....why?

# In[49]:


figure(figsize=(12,6))
p={}
for i in range(3):
    subplot(1,3,i+1)
    p[i] = C.means[i].reshape(data.shape)
    imshow(p[i])
    title(data.target_names[i])


# In[51]:


data.target_names


# In[53]:


piece1=0
piece2=2
blank=1


# look at differences -- piece 2 minus blank, and piece 1 minus blank, rescaled to fill the color space.

# In[54]:


d=p[piece1]-p[blank]
d=d-d.min()
d=d/d.max()
imshow(d)


# In[55]:


d=p[piece2]-p[blank]
d=d-d.min()
d=d/d.max()
imshow(d)


# In[ ]:




