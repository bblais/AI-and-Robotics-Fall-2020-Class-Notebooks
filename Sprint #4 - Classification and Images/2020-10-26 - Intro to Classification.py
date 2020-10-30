#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


from classy import *


# https://archive.ics.uci.edu/ml/datasets.php

# In[3]:


ls ../data


# In[4]:


data=load_excel('../data/iris.xls')


# In[33]:


plot_feature_combinations(data)


# In[39]:


data_train=extract_features(data,[2,3])


# In[34]:


C=NaiveBayes()


# In[40]:


C.fit(data_train.vectors,data_train.targets)


# In[43]:


plot2D(data_train,C)
C.plot_centers()  # plot the classifier information


# In[44]:


C.means


# In[45]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))


# ## Full Data Set in 4 dimensions

# In[5]:


data=load_excel('../data/iris.xls')


# In[6]:


C=NaiveBayes()


# In[7]:


data_train=data


# In[8]:


C.fit(data_train.vectors,data_train.targets)


# In[9]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))


# In[51]:


C=kNearestNeighbor()


# In[52]:


C.fit(data_train.vectors,data_train.targets)


# In[53]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))


# In[10]:


data_train,data_test=split(data,test_size=0.2)


# In[11]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[12]:


C=kNearestNeighbor()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[57]:


get_ipython().magic('pinfo load_csv')


# In[58]:


load_csv('../data/krkopt.data')


# In[ ]:




