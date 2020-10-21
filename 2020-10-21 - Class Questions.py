#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[1,3,4,6,7,3,4,6]


# - write a loop to change the 4 into a 999

# In[2]:


a=[1,3,4,6,7,3,4,6]

for i in range(len(a)):
    if a[i]==4:
        a[i]=999
        
a


# - write a loop to change only the first 4 that is found to a 999

# In[3]:


a=[1,3,4,6,7,3,4,6]

for i in range(len(a)):
    if a[i]==4:
        a[i]=999
        break
        
a


# In[4]:


for i in range(10):
    print(i)


# In[5]:


for i in range(10,0,-1):
    print(i)


# In[8]:


for i in range(10,-1,-1):
    print(i)


# In[9]:


for i in range(10-1,-1,-1):
    print(i)


# In[10]:


for i in range(2,10):
    print(i)
    
for i in range(10,18):
    print(i)

for i in range(18,23):
    print(i)
    


# In[11]:


get_ipython().magic('pinfo range')


# In[ ]:




