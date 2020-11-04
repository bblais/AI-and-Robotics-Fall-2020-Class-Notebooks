#!/usr/bin/env python
# coding: utf-8

# In[1]:


from classy import *


# In[5]:


get_ipython().magic('pylab inline   # BAD BAD BAD')


# In[6]:


images=image.load_images('Nim Images/')


# In[7]:


data=image.images_to_vectors(images)


# In[8]:


data_train,data_test=split(data)


# In[ ]:




