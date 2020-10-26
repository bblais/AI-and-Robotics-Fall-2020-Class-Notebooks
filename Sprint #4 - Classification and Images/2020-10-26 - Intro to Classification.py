#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


from classy import *


# https://archive.ics.uci.edu/ml/datasets.php

# In[3]:


ls ../data


# In[32]:


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

# In[46]:


data=load_excel('../data/iris.xls')


# In[47]:


C=NaiveBayes()


# In[48]:


data_train=data


# In[49]:


C.fit(data_train.vectors,data_train.targets)


# In[50]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))


# In[51]:


C=kNearestNeighbor()


# In[52]:


C.fit(data_train.vectors,data_train.targets)


# In[53]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))


# In[54]:


data_train,data_test=split(data,test_size=0.2)


# In[55]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[56]:


C=kNearestNeighbor()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:




