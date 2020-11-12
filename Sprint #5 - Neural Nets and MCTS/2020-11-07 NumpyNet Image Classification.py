#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('pylab inline')
from classy import *


# In[2]:


images=image.load_images('data/digits')


# In[3]:


summary(images)


# In[4]:


data=image.images_to_vectors(images)
data.vectors-=data.vectors.mean()
data.vectors/=data.vectors.std()


# In[5]:


data_train,data_test=split(data)
n=800
image.vector_to_image(data_train.vectors[n,:],(8,8))
title("The number %s" % str(data_train.target_names[data_train.targets[n]]))


# In[6]:


data_train.vectors.shape


# In[7]:


num_samples,num_features=data_train.vectors.shape
num_classes=len(data_train.target_names)


# ## Perceptron

# In[8]:


C=NumPyNetBackProp({
    'input':num_features,               # number of features
    'output':(num_classes,'linear'),  # number of classes
    'cost':'mse',
})


# In[9]:


C.fit(data_train.vectors,data_train.targets)


# In[10]:


print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[11]:


figure(figsize=(16,4))
for i,t in enumerate(data_train.target_names):
    subplot(2,10,i+1)
    vector=random_vector(data_train,t)
    image.vector_to_image(vector,(8,8))
    axis('off')
    
    subplot(2,10,i+11)
    image.vector_to_image(C.weights[0][:,i],(8,8))
    axis('off')
    


# ## Backprop

# In[12]:


C=NumPyNetBackProp({
    'input':num_features,               # number of features
    'hidden':[(12,'logistic'),],
    'output':(num_classes,'logistic'),  # number of classes
    'cost':'mse',
})


# In[13]:


C.fit(data_train.vectors,data_train.targets,epochs=5000)


# In[14]:


print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[15]:


weights_ih=C.weights[0]
weights_hy=C.weights[-1]


# In[16]:


weights_ih.shape


# In[17]:


for i in range(weights_ih.shape[1]):
    subplot(3,4,i+1)
    image.vector_to_image(weights_ih[:,i],(8,8))
    axis('off')


# ## Convolutional Neural Net

# In[19]:


images=image.load_images('data/digits')
num_classes=len(images.target_names)
images.data=[_/255.0 for _ in images.data]


C=NumPyNetImageNN(
    Convolutional_layer(size=3, filters=32, stride=1, pad=True, activation='Relu'),
    BatchNorm_layer(),
    Maxpool_layer(size=2, stride=1, padding=True),
    Connected_layer(outputs=100, activation='Relu'),
    BatchNorm_layer(),
    Connected_layer(outputs=num_classes, activation='Linear'),
    Softmax_layer(spatial=True, groups=1, temperature=1.),
    )


# In[20]:


images_train,images_test=image.split(images,verbose=False)
summary(images_train)
summary(images_test)


# In[21]:


C.fit(images_train,epochs=10,batch=128)


# In[22]:


print("On Training Set:",C.percent_correct(images_train))
print("On Test Set:",C.percent_correct(images_test))


# In[ ]:




