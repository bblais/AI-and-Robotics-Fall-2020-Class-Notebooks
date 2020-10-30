#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Game import *


# In[12]:


def initial_state():
    N=4
    state=Board(N,N)
    
    for col in range(N):
        state[0,col]=2
        state[N-1,col]=1
        
    return state


# In[20]:


def show_state(state):
    print(state)


# In[13]:


def valid_moves(state,player):
    if player==1:
        moves=state.moves(1,"n","xne","xnw")
    elif player==2:
        moves=state.moves(2,"s","xse","xsw")
    else:
        raise ValueError("You can't get there from here.")
        
    return moves


# In[14]:


def win_status(state,player):
    if player==1:
        other_player=2
    else:
        other_player=1
        
    N=state.shape[0]  # notice I am not hardcoding the size
    for col in range(N):
        if player==1 and state[0,col]==1:
            return 'win'
        if player==2 and state[N-1,col]==2:
            return 'win'        
        
    if not valid_moves(state,other_player):
        return 'win'
    
    


# In[15]:


def update_state(state,player,move):
    start,end=move
    
    # make a new state, and modify it (technically there is a lazy hack here)
    new_state=state
    new_state[start]=0 
    new_state[end]=player
    
    return new_state


# In[16]:


def human_move(state,player):
    state.show_locations()
    
    while True:
        start=int(input("What starting square?"))
        end=int(input("What ending square?"))

        move=[start,end]

        if move in valid_moves(state,player):
            break
        
    return move

human_agent=Agent(human_move)


# In[17]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


random_agent=Agent(random_move)


# In[18]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[21]:


g=Game(1)
result=g.run(random_agent,random_agent)


# In[22]:


g=Game(1)
result=g.run(minimax_agent,random_agent)


# In[23]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True,adjust_values_by_depth=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[24]:


g=Game(1)
result=g.run(minimax_agent,random_agent)


# In[30]:


def initial_state():
    N=5
    state=Board(N,N)
    
    for col in range(N):
        state[0,col]=2
        state[N-1,col]=1
        
    return state


# In[31]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True,maxdepth=3)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[35]:


def material_advantage_heuristic(state,player):
    # material advantage
    N_player=len(state.find(player))
    N_other_player=len(state.find(other_player))
    
    v1=(N_player-N_other_player)/(N_player+N_other_player)

    return v1

def forward_progression_heuristic(state,player):
    N_player=len(state.find(player))
    N_other_player=len(state.find(other_player))

    locations=state.find(player)
    v1=0
    for index in locations:
        row,col = state.rc_from_index(index)
        if player==1:  # player 1, lower rows = better
            v1+=N-row
        else:
            v1+=row
    # the maximum v2 can be is N*N_player
    v1/=N*N_player

    locations=state.find(other_player)
    v2=0
    for index in locations:
        row,col = state.rc_from_index(index)
        if player==1:  # player 1, lower rows = better
            v2+=N-row
        else:
            v2+=row
    # the maximum v2 can be is N*N_player
    v2/=N*N_other_player

    return v1-v2
     


# In[36]:


def heuristic(state,player):
    
    v1=material_advantage_heuristic(state,player)
    v2=forward_progression_heuristic(state,player)
    
    return v1*.8 + v2*.2   # weighted average

    


# In[ ]:





# In[37]:


g=Game(1)
result=g.run(minimax_agent,random_agent)


# In[ ]:




