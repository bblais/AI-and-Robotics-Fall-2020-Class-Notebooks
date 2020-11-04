#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


import classy


# In[10]:


import classy as cl


# In[12]:


import numpy as np
import pandas as pd


# In[ ]:





# In[11]:


images=cl.image.load_images('Nim Images/')


# In[4]:


data=classy.image.images_to_vectors(images)


# In[5]:


data_train,data_test=classy.split(data)


# In[ ]:





# In[6]:


import mynim


# In[7]:


mynim.initial_state()


# In[8]:


plot(rand(1000))


# In[9]:


mynim.plot(rand(1000))


# In[14]:


get_ipython().magic('pinfo2 plot')


# In[16]:


mynim.__file__


# In[17]:


get_ipython().magic('pinfo2 mynim.plot')


# In[18]:


plot1=plot
plot2=mynim.plot


# In[19]:


plot1(rand(100))


# In[20]:


from mynim import plot as plot3


# In[21]:


plot3('asdasd')


# In[22]:


from mynim import initial_state


# In[ ]:




