#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')
from classy import *


# ## make a fake image data set without square images

# In[2]:


for i in range(100):
    im=rand(20,10,3)*0.3
    imsave('test images/cat/%d.jpg' % i,im)
imshow(im)


# In[3]:


for i in range(100):
    im=rand(20,10,3)*0.3+.6
    imsave('test images/dog/%d.jpg' % i,im)
imshow(im)


# In[4]:


images=image.load_images('test images/')


# In[5]:


data=image.images_to_vectors(images,verbose=False)


# In[6]:


data.vectors/=255


# In[7]:


summary(data)


# In[8]:


data_train,data_test=split(data,test_size=0.2)


# In[15]:


C=NumPyNetBackProp({
    'input':20*10*3,               # number of features
    'hidden':[(5,'logistic'),(7,'logistic'),],
    'output':(2,'logistic'),  # number of classes
    'cost':'mse',
})


# In[16]:


C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[17]:


C.weights[0],C.weights[0].shape


# In[18]:


C.weights[1],C.weights[1].shape


# In[19]:


C.weights[2],C.weights[2].shape


# ## visualize the weights from the inputs to the first hidden layer

# In[21]:


W=C.weights[0]
W.shape


# In[23]:


vector=W[:,0]
vector.shape


# In[25]:


vector_image=vector.reshape(20,10,3)


# In[29]:


vector_image=vector_image-vector_image.min()  # make the minimum zero
vector_image=vector_image/vector_image.max()  # scale the new maximum to 1


# In[30]:


vector_image.min(),vector_image.max()


# In[31]:


imshow(vector_image)


# In[33]:


imshow(C.weights[2])
colorbar()


# In[ ]:





# In[ ]:





# In[ ]:




