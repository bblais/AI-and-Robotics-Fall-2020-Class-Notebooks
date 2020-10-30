#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from numpy import nan,mean


# In[13]:


names={}

names['Sprint #1']=list(pd.read_csv('data/Original Sprint #1 Scrum Kanban- Programming and Games.csv')['Name'])
names['Sprint #2']=list(pd.read_csv('data/Original Sprint #2 Scrum Kanban - Learning and Simulation.csv')['Name'])
names['Sprint #3']=list(pd.read_csv('data/Original Sprint #3 Scrum Kanban - Probability and Robot Tasks.csv')['Name'])
#names['Sprint #4']=list(pd.read_csv('data/Original Sprint #4 Scrum Kanban - Classification and Images.csv')['Name'])
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





# In[14]:


# replace these file names with the ones you downloaded for each sprint

data1=pd.read_csv('/Users/bblais/Downloads/Export-ff4d13c5-8e2a-4e13-a411-cf5ae684007d.zip')  # sprint #1
data2=pd.read_csv('/Users/bblais/Downloads/Export-b4b07873-f08b-4cf9-851e-81dbb896bb4c.zip')  # sprint #2
data3=pd.read_csv('/Users/bblais/Downloads/Export-191fbcb8-a0c4-44d3-8c19-5c5402a71d81.zip')  # sprint #3
display(data1)
display(data2)
display(data3)


# collect all the feedback into one group
feedback={}
for data in [data1,data2,data3]:
    for row in data.iterrows():
        feedback[row[1]['Name']]=row[1]['Feedback Code']
    


# In[15]:


feedback


# In[43]:


def letter_grade(total):
    if total>99:
        total=99
        
    tens=int(total//10)
    ones=int(total%10)
    
    if ones>=7:
        mod='+'
    elif ones>=4:
        mod=''
    else:
        mod='-'
        
    letter='FFFFFFDCBA'[tens]
    
    grade=letter+mod
    if grade=='A+':
        grade='A'
    if grade=='D-':
        grade='F'
    if letter=='F':
        grade='F'
        
    return grade


# In[44]:


for i in range(100):
    print(i,letter_grade(i)," ; " ,end="")


# In[45]:


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
print("Overall Average: ",total)
print("Letter Grade:",letter_grade(total))

    


# In[ ]:




