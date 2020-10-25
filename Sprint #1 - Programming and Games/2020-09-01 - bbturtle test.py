#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('gui', 'tk')


# In[2]:


from bbturtle import *


# In[3]:


forward(50)
done()


# In[4]:


reset()
for i in range(20):
    forward(50)
    backward(50)
    right(5)
done()


# In[ ]:




