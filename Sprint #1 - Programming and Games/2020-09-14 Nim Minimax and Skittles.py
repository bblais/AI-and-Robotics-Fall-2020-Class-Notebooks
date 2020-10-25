#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# # Nim
# 
# Rules:
# 
# 1. start with 21 sticks -- state = number of sticks
# 2. turns alternate taking 1,2, or 3 sticks
# 3. player taking last stick loses

# In[7]:


def initial_state():
    return 25

def show_state(state):
    print("There are ",state,"sticks.")
    
def valid_moves(state,player):
    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]
    
def update_state(state,player,move):
    # move = number of sticks to pick up
    new_state=state-move # remove the sticks
    return new_state

def win_status(state,player):
    if state==0:
        return 'lose'
    elif state==1:
        return 'win'
    else:
        return None
    
    # there is no stalemate


# In[8]:


def human_move(state,player):
    print("Player ",player)
    move=int(input("How many sticks?"))
    return move

human_agent=Agent(human_move)


# In[9]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move
random_agent=Agent(random_move)


# In[10]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[11]:


def skittles_move(state,player,info):
    S=info.S
    last_action=info.last_action
    last_state=info.last_state
    
    
    # if Ive never seen this state before
    if not state in S:
        actions=valid_moves(state,player)

        S[state]=Table()
        for action in actions:
            S[state][action]=3     
    
    move=weighted_choice(S[state])  # weighted across actions
    
    # what if there are no skittles for a particular state?
    # move is None in that case
    
    if move is None:
        # learn a little bit
        if last_state:
            S[last_state][last_action]=S[last_state][last_action]-1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0
        
        move=random_move(state,player)
    
    return move

def skittles_after(status,player,info):
    S=info.S
    last_action=info.last_action
    last_state=info.last_state

    if status=='lose':
        # learn a little bit
        S[last_state][last_action]=S[last_state][last_action]-1
        if S[last_state][last_action]<0:
            S[last_state][last_action]=0
        
    


skittles_agent=Agent(skittles_move)
skittles_agent.S=Table()
skittles_agent.post=skittles_after


# In[ ]:





# In[ ]:





# In[ ]:





# Some miscellaneous table stuff

# In[9]:


S=Table()


# In[16]:


state=Board(3,3)
state[4]=1
state


# In[17]:


state


# In[18]:


S[state]=2


# In[19]:


S


# In[24]:


S=Table()
state=initial_state()
actions=valid_moves(state,1)

S[state]=Table()
for action in actions:
    S[state][action]=3  # nunber of skittles


# In[25]:


S


# In[26]:


state=2
S[state]=Table()
actions=valid_moves(state,1)
for action in actions:
    S[state][action]=3  # nunber of skittles


# In[27]:


S


# In[52]:


skittles_agent.S=Table()


# In[26]:


g=Game(1000)
g.display=False
g.run(random_agent,skittles_agent);


# In[27]:


g.report()


# In[55]:


skittles_agent.S


# In[33]:


SaveTable(skittles_agent.S,'nim skittles table.json')


# In[32]:


sorted(list(skittles_agent.S.keys()))


# In[57]:


skittles_agent.S=LoadTable('nim skittles table.json')


# In[ ]:





# In[6]:


g=Game()
g.run(minimax_agent,random_agent)


# In[7]:


g=Game(10)
g.display=False
g.run(minimax_agent,random_agent)


# In[ ]:




