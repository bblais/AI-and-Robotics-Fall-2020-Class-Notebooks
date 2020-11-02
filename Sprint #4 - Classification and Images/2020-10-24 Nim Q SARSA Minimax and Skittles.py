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

# In[23]:


def initial_state():
    return randint(10,24)

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


# In[24]:


def human_move(state,player):
    print("Player ",player)
    move=int(input("How many sticks?"))
    return move

human_agent=Agent(human_move)


# In[25]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move
random_agent=Agent(random_move)


# In[26]:


def perfect_move(state,player):
    move=(state-1)%4
    if move==0:
        move=1
    return move
perfect_agent=Agent(perfect_move)


# In[27]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[28]:


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


# In[29]:


def Q_move(state,player,info):
    Q=info.Q
    last_action=info.last_action
    last_state=info.last_state
    
    α=info.α
    γ=info.γ
    ϵ=info.ϵ
    

    # if Ive never seen this state before
    if not state in Q:
        actions=valid_moves(state,player)

        Q[state]=Table()
        for action in actions:
            Q[state][action]=0     
    
    # deal with random vs top choice here
    if random.random()<ϵ:
        move=random_move(state,player)  
    else:
        move=top_choice(Q[state]) 
    
    # what if there are no skittles for a particular state?
    # move is None in that case
    
    if not last_action is None:  # not the first move
        # learn a little bit
        # change equation here
        reward=0
        
        # Bellman equation
        Q[last_state][last_action] += α*(reward+
                         γ*max([Q[state][a] for a in Q[state]])  - 
                                Q[last_state][last_action])
    
        
    
    return move

def Q_after(status,player,info):
    Q=info.Q
    last_action=info.last_action
    last_state=info.last_state

    α=info.α
    γ=info.γ
    ϵ=info.ϵ
    
    if status=='lose':
        reward=-1
    elif status=='win':
        reward=1
    elif status=='stalemate':
        reward=0.5
    else:
        reward=0
        
    # learn a little bit
    Q[last_state][last_action] += α*(reward-Q[last_state][last_action])
        


Q_agent=Agent(Q_move)
Q_agent.Q=LoadTable('Q_data.json')
Q_agent.post=Q_after

Q_agent.α=0.3  # learning rate
Q_agent.γ=0.9  # memory constant, discount factor
Q_agent.ϵ=0.1  # probability of a random move during learning


# ## Training stage
# 
# - the Q values can change
# - that the agent takes random moves sometimes

# In[30]:


Q_agent.α=0.3  # learning rate
Q_agent.ϵ=0.1  # probability of a random move during learning


# In[31]:


g=Game(100)
g.display=False
g.run(perfect_agent,Q_agent);


# ## Testing stage
# 
# - the Q values **do not change**
# - that the agent **never takes random moves**

# In[32]:


Q_agent.α=0.0  # learning rate
Q_agent.ϵ=0.0  # probability of a random move during learning


# In[33]:


g=Game(10)
g.display=False
g.run(perfect_agent,Q_agent);


# In[34]:


g.report()


# In[35]:


Q_agent.Q


# In[36]:


SaveTable(Q_agent.Q,'Q_data.json')


# In[ ]:





# ## Q vs Q with progress

# In[37]:


Q1_agent=Agent(Q_move)
Q1_agent.Q=LoadTable('Q1_data.json')
Q1_agent.post=Q_after

Q1_agent.α=0.3  # learning rate
Q1_agent.γ=0.9  # memory constant, discount factor
Q1_agent.ϵ=0.1  # probability of a random move during learning

Q2_agent=Agent(Q_move)
Q2_agent.Q=LoadTable('Q2_data.json')
Q2_agent.post=Q_after

Q2_agent.α=0.3  # learning rate
Q2_agent.γ=0.9  # memory constant, discount factor
Q2_agent.ϵ=0.1  # probability of a random move during learning


# In[38]:


total_number_of_games=0
for epoch in range(100):
    
    number_training_games=10
    number_of_testing_games=10
    
    #=================
    # traning cycle
    Q1_agent.α=0.3  # learning rate
    Q1_agent.ϵ=0.1  # probability of a random move during learning
    Q2_agent.α=0.3  # learning rate
    Q2_agent.ϵ=0.1  # probability of a random move during learning
    
    g=Game(number_training_games)
    g.display=False
    g.run(Q1_agent,Q2_agent)

    #=================
    # testing cycle
    Q1_agent.α=0.0  # learning rate
    Q1_agent.ϵ=0.0  # probability of a random move during learning
    Q2_agent.α=0.0  # learning rate
    Q2_agent.ϵ=0.0  # probability of a random move during learning
    
    
    g=Game(number_of_testing_games)
    g.display=False
    result=g.run(Q1_agent,Q2_agent)
    
    total_number_of_games+=number_training_games
    win_percentage=sum([r==1 for r in result])/number_training_games*100
    loss_percentage=sum([r==2 for r in result])/number_training_games*100
    tie_percentage=sum([r==0 for r in result])/number_training_games*100

    print(total_number_of_games,":",win_percentage," ",end="")
    
    SaveTable(Q1_agent.Q,'Q1_data.json')
    SaveTable(Q2_agent.Q,'Q2_data.json')    
    


# ## SARSA Agent

# In[39]:


def SARSA_move(state,player,info):
    Q=info.Q
    last_action=info.last_action
    last_state=info.last_state
    
    α=info.α
    γ=info.γ
    ϵ=info.ϵ
    

    # if Ive never seen this state before
    if not state in Q:
        actions=valid_moves(state,player)

        Q[state]=Table()
        for action in actions:
            Q[state][action]=0     
    
    # deal with random vs top choice here
    if random.random()<ϵ:
        move=random_move(state,player)  
    else:
        move=top_choice(Q[state]) 
    
    # what if there are no skittles for a particular state?
    # move is None in that case
    
    if not last_action is None:  # not the first move
        # learn a little bit
        # change equation here
        reward=0
        
        # Bellman equation
        Q[last_state][last_action] += α*(reward+
                         γ*Q[state][move] - 
                                Q[last_state][last_action])
    
        
    
    return move

def SARSA_after(status,player,info):
    Q=info.Q
    last_action=info.last_action
    last_state=info.last_state

    α=info.α
    γ=info.γ
    ϵ=info.ϵ
    
    if status=='lose':
        reward=-1
    elif status=='win':
        reward=1
    elif status=='stalemate':
        reward=0.5
    else:
        reward=0
        
    # learn a little bit
    Q[last_state][last_action] += α*(reward-Q[last_state][last_action])
        


# In[40]:


SARSA1_agent=Agent(SARSA_move)
SARSA1_agent.Q=LoadTable('SARSA1_data.json')
SARSA1_agent.post=Q_after

SARSA1_agent.α=0.3  # learning rate
SARSA1_agent.γ=0.9  # memory constant, discount factor
SARSA1_agent.ϵ=0.1  # probability of a random move during learning

SARSA2_agent=Agent(Q_move)
SARSA2_agent.Q=LoadTable('SARSA2_data.json')
SARSA2_agent.post=Q_after

SARSA2_agent.α=0.3  # learning rate
SARSA2_agent.γ=0.9  # memory constant, discount factor
SARSA2_agent.ϵ=0.1  # probability of a random move during learning


# In[41]:


total_number_of_games=0
for epoch in range(100):
    
    number_training_games=10
    number_of_testing_games=10
    
    #=================
    # traning cycle
    SARSA1_agent.α=0.3  # learning rate
    SARSA1_agent.ϵ=0.1  # probability of a random move during learning
    SARSA2_agent.α=0.3  # learning rate
    SARSA2_agent.ϵ=0.1  # probability of a random move during learning
    
    g=Game(number_training_games)
    g.display=False
    g.run(SARSA1_agent,SARSA2_agent)

    #=================
    # testing cycle
    SARSA1_agent.α=0.0  # learning rate
    SARSA1_agent.ϵ=0.0  # probability of a random move during learning
    SARSA2_agent.α=0.0  # learning rate
    SARSA2_agent.ϵ=0.0  # probability of a random move during learning
    
    
    g=Game(number_of_testing_games)
    g.display=False
    result=g.run(SARSA1_agent,SARSA2_agent)
    
    total_number_of_games+=number_training_games
    win_percentage=sum([r==1 for r in result])/number_training_games*100
    loss_percentage=sum([r==2 for r in result])/number_training_games*100
    tie_percentage=sum([r==0 for r in result])/number_training_games*100

    print(total_number_of_games,":",win_percentage," ",end="")
    
    SaveTable(SARSA1_agent.Q,'SARSA1_data.json')
    SaveTable(SARSA2_agent.Q,'SARSA2_data.json')    
    


# In[42]:


SARSA1_agent.Q


# In[ ]:




