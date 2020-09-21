#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from numpy import nan,mean


# In[2]:


names={}

names['Sprint #1']=list(pd.read_csv('data/Original Sprint #1 Scrum Kanban- Programming and Games.csv')['Name'])
names['Sprint #2']=list(pd.read_csv('data/Original Sprint #2 Scrum Kanban - Learning and Simulation.csv')['Name'])
names


# 1. Upper right corner of your notebook (the three dots), Export...
# 
# <img src="images/Screen Shot 2020-09-21 at 08.59.24.png" width=300>
# 
# 2. Choose Markdown & CSV, and it will save as a .zip file
# 
# <img src="images/Screen Shot 2020-09-20 at 15.13.33.png" width=500>
# 

# In[ ]:





# In[4]:


# replace these file names with the ones you downloaded for each sprint

data1=pd.read_csv('/Users/bblais/Downloads/Sprint 1 Export-486501b0-1668-4c6f-b04b-7bb8e87ec9f5.zip')
data2=pd.read_csv('/Users/bblais/Downloads/Sprint 2 Export-e24a0a56-f9ea-46c4-b03d-66d72e0b9c1d.zip')
display(data1)
display(data2)

feedback={}
for row in data1.iterrows():
    
    feedback[row[1]['Name']]=row[1]['Feedback Code']
for row in data2.iterrows():
    feedback[row[1]['Name']]=row[1]['Feedback Code']
    


# In[5]:


feedback


# In[6]:


student_item_names=feedback.keys()
total=0
count=0

scores={'cc':100,'c2':90,'c1':60,'c0':30,'00':0,'nan':0,
       'p2':90,'p1':60,'p0':30}

for sprint in names:
    sprint_count=0
    sprint_total=0
    
    for name in names[sprint]:


        fb=None
        if name in student_item_names:
            fb=feedback[name]
        else:
            for sn in student_item_names:
                if sn[:20]==name[:20]:  # match beginning
                    fb=feedback[sn]
                    break


        if not fb:
            raise ValueError(name)

        codes=str(fb).split(",")

        score=mean([scores[_.strip()] for _ in codes])
        print(name,"\t",fb,"\t",score)
        total+=score
        count+=1
        sprint_total+=score
        sprint_count+=1
        
    print()
    print("%s Average: %.2f" % (sprint,sprint_total/sprint_count))
    print()
    
total=total/count
print()
print("Average: ",total)

    


# In[ ]:




