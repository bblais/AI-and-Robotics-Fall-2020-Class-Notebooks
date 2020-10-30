#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')


# In[2]:


from classy import *


# In[4]:


ls ../data/digits/


# In[5]:


images=image.load_images('../data/digits')


# In[6]:


data=image.images_to_vectors(images)


# In[7]:


data.vectors/=255


# In[9]:


summary(data)


# In[10]:


data_train,data_test=split(data,test_size=0.2)


# In[13]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[15]:


C.means.shape


# In[16]:


data.target_names


# In[17]:


prototypes=C.means


# In[18]:


pr1=prototypes[0,:]


# In[19]:


pr1.shape


# In[20]:


pr1=pr1.reshape(8,8)
imshow(pr1)


# In[21]:


pr2=prototypes[1,:].reshape(8,8)
imshow(pr2)


# In[23]:


for i,name in enumerate(data.target_names):
    pr=prototypes[i,:].reshape(8,8)
    subplot(3,4,i+1)
    imshow(pr)
    title(name)


# In[24]:


test_vector=rand(64)


# In[26]:


C.predict(test_vector.reshape(1,64))


# In[27]:


imshow(test_vector.reshape(8,8))


# In[ ]:





# In[28]:


C=kNearestNeighbor()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[29]:


C.predict(test_vector.reshape(1,64))


# In[ ]:




