#!/usr/bin/env python
# coding: utf-8

# Definition of factorial
# 
# $$
# N! = 1 \cdot 2 \cdot 3 \cdots N
# $$

# $$
# N! = N\cdot (N-1)!
# $$

# In[3]:


def factorial(N):
    if N==0:
        return 1
    
    
    return N*factorial(N-1)


# In[5]:


factorial(120)


# In[15]:


max_score=35
saved_p={}
saved_whether_roll={}

def p_win(i,j,k):  # i = my score, j is the other score, k is the turn score
    
    if i+k>=max_score:
        return 1
    
    if j>=max_score:
        return 0.0
    
    
    if (i,j,k) in saved_p:
        return saved_p[(i,j,k)]
    

    # if I roll a one
    #p_win_roll=1-(probability that I lose, handing it off to the other)
    p_win_roll=1-p_win(j,i+1,0)
    
    # if I roll a two, three,
    for dice in [2,3,4,5,6]:  # range(2,6+1) is equal but unreadable
        p_win_roll+=p_win(i,j,k+dice)
    
    p_win_roll/=6
    
    if k==0:  # add 1 even when the turn score is zero
        p_win_hold=1-p_win(j,i+1,0)
    else:
        p_win_hold=1-p_win(j,i+k,0)

        
    # assume that we are rational
    if p_win_roll>p_win_hold:
        p=p_win_roll
        saved_whether_roll[(i,j,k)]=True
    else:
        p=p_win_hold
        saved_whether_roll[(i,j,k)]=False
        
    
    saved_p[(i,j,k)]=p
    
    return p


# In[17]:


p_win(0,31,0)


# In[13]:


p_win(18,0,0)


# In[ ]:




