#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().magic('pylab inline')
from classy import *


# Make sure to update:
# 
# 1. classy
# 2. numpynet
# 3. tqdm

# # Perceptron aka Linear Neuron

# In[43]:


data=make_dataset(bob=[[0,0],[1,1]],sally=[[0,1],[1,0]])


# In[44]:


plot2D(data,axis_range=[-.55,1.5,-.5,1.5])


# In[45]:


data


# In[46]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'output':(2,'linear'),  # number of classes
    'cost':'mse',
})


# In[47]:


C.fit(data.vectors,data.targets)


# In[48]:


print((C.predict(data.vectors)))
print(("On Training Set:",C.percent_correct(data.vectors,data.targets)))


# In[49]:


plot2D(data,classifier=C,axis_range=[-.55,1.5,-.5,1.5])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Backprop

# In[50]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'hidden':[(5,'logistic'),],
    'output':(2,'logistic'),  # number of classes
    'cost':'mse',
})


# In[51]:


C.fit(data.vectors,data.targets,epochs=3000)


# In[52]:


print((C.predict(data.vectors)))
print(("On Training Set:",C.percent_correct(data.vectors,data.targets)))


# In[53]:


plot2D(data,classifier=C,axis_range=[-.55,1.5,-.5,1.5])


# # Curvy Data

# In[54]:


data=load_excel('../data/center-surround.xlsx')
data_train,data_test=split(data,test_size=0.2)


# In[55]:


plot2D(data,axis_range=[-1.5,1.5,-1.5,1.5])


# In[56]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'hidden':[(5,'logistic'),],
    'output':(2,'logistic'),  # number of classes
    'cost':'mse',
})


# In[57]:


C.fit(data.vectors,data.targets,epochs=3000)


# In[58]:


print((C.predict(data.vectors)))
print(("On Training Set:",C.percent_correct(data.vectors,data.targets)))


# In[59]:


plot2D(data,classifier=C,axis_range=[-.55,1.5,-.5,1.5])


# # Iris

# In[73]:


data=load_excel('../data/iris.xls')
data_train,data_test=split(data,test_size=0.2)


# In[74]:


C=NumPyNetBackProp({
    'input':4,               # number of features
    'hidden':[(5,'logistic'),],
    'output':(3,'logistic'),  # number of classes
    'cost':'mse',
})


# In[75]:


C.fit(data.vectors,data.targets,epochs=3000)


# In[76]:


C.weights[0]


# In[77]:


C.weights[0].shape


# In[78]:


C.weights[1]


# In[79]:


C.weights[1].shape


# # Eye

# In[80]:


data=load_excel('../data/eye.xlsx')


# In[81]:


C=NumPyNetBackProp({
    'input':8,               # number of features
    'hidden':[(3,'logistic'),],
    'output':(8,'logistic'),  # number of classes
    'cost':'mse',
})


# In[95]:


C.fit(data.vectors,data.targets,epochs=10000)


# In[96]:


print((C.predict(data.vectors)))
print(("On Training Set:",C.percent_correct(data.vectors,data.targets)))


# In[97]:


C.weights


# In[98]:


C.weights[0]


# In[99]:


C.weights[0].shape


# In[ ]:





# In[100]:


C.weights[1]


# In[101]:


C.weights[1].shape


# In[102]:


C.output(data.vectors)[0]


# In[104]:


h,y=C.output(data.vectors)


# In[105]:


around(h,2)


# In[ ]:




