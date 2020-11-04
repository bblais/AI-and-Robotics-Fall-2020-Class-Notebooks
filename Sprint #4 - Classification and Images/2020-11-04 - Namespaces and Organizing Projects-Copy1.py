#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


from classy import *


# In[3]:


images=image.load_images('Nim Images/')


# In[4]:


data=image.images_to_vectors(images)


# In[5]:


data_train,data_test=split(data)


# In[ ]:





# In[6]:


from mynim import *


# In[7]:


initial_state()


# In[8]:


plot(rand(1000))


# In[ ]:




