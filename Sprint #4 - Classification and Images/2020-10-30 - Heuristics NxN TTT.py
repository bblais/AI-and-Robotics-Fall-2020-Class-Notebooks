#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():
    N=3
    state=Board(N,N)
            
    return state


# In[3]:


def show_state(state):
    print(state)


# In[4]:


def valid_moves(state,player):
    moves=[]
    N=state.shape[0]  # notice I am not hardcoding the size
    for i in range(N*N):
        if state[i]==0:
            moves.append(i)        
    return moves


# In[5]:


def win_status(state,player):
    if player==1:
        other_player=2
    else:
        other_player=1
        
    N=state.shape[0]  # notice I am not hardcoding the size        
    if N==3 or N==4:
        N_in_a_row=3
    else:
        N_in_a_row=4
        
        
    for in_a_row in state.diags(N_in_a_row):
        if in_a_row ==[player]*N_in_a_row:
            return 'win'

    for in_a_row in state.rows(N_in_a_row):
        if in_a_row ==[player]*N_in_a_row:
            return 'win'
        
    for in_a_row in state.cols(N_in_a_row):
        if in_a_row ==[player]*N_in_a_row:
            return 'win'
                
    if not valid_moves(state,other_player):
        return 'stalemate'
    
    


# In[6]:


def update_state(state,player,move):
    # make a new state, and modify it (technically there is a lazy hack here)
    new_state=state
    new_state[move]=player
    
    return new_state


# In[7]:


def human_move(state,player):
    state.show_locations()
    
    while True:
        move=int(input("What square?"))

        if move in valid_moves(state,player):
            break
        
    return move

human_agent=Agent(human_move)


# In[8]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


random_agent=Agent(random_move)


# In[9]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[10]:


g=Game(1)
result=g.run(random_agent,random_agent)


# In[12]:


g=Game(1)
result=g.run(minimax_agent,random_agent)


# In[13]:


def initial_state():
    N=4
    state=Board(N,N)
            
    return state


# In[14]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True,maxdepth=3)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[15]:


def in_a_row_with_zero(vec,player,num):
    L=len(vec)
    for i in range(L-num):
        if vec[i:i+num+1] == [0] + [player]*num or vec[i:i+num+1] == [player]*num + [0]:
            return True
        
    return False
def two_in_a_row_with_zero(vec,player):
    return in_a_row_with_zero(vec,player,2)
def three_in_a_row_with_zero(vec,player):
    return in_a_row_with_zero(vec,player,3)


# In[16]:


def in_a_row_heuristic(state,player):
    if player==1:
        other_player=2
    else:
        other_player=1
    
    N=state.shape[0]  # notice I am not hardcoding the size        
    if N==3 or N==4:
        N_in_a_row=3
    else:
        N_in_a_row=4
    
    count=0
    rcount=0
    for in_a_row in state.diags(N_in_a_row):
        count+=1
        if two_in_a_row_with_zero(in_a_row,player):
            rcount+=1
        if two_in_a_row_with_zero(in_a_row,other_player):
            rcount-=1
            
    for in_a_row in state.rows(N_in_a_row):
        count+=1
        if two_in_a_row_with_zero(in_a_row,player):
            rcount+=1
        if two_in_a_row_with_zero(in_a_row,other_player):
            rcount-=1
        
    for in_a_row in state.cols(N_in_a_row):
        count+=1
        if two_in_a_row_with_zero(in_a_row,player):
            rcount+=1
        if two_in_a_row_with_zero(in_a_row,other_player):
            rcount-=1
    v1=rcount/count       
    
    count=0
    rcount=0
    for in_a_row in state.diags(N_in_a_row):
        count+=1
        if three_in_a_row_with_zero(in_a_row,player):
            rcount+=1
        if three_in_a_row_with_zero(in_a_row,other_player):
            rcount-=1
            
    for in_a_row in state.rows(N_in_a_row):
        count+=1
        if three_in_a_row_with_zero(in_a_row,player):
            rcount+=1
        if three_in_a_row_with_zero(in_a_row,other_player):
            rcount-=1
        
    for in_a_row in state.cols(N_in_a_row):
        count+=1
        if three_in_a_row_with_zero(in_a_row,player):
            rcount+=1
        if three_in_a_row_with_zero(in_a_row,other_player):
            rcount-=1
    v2=rcount/count       
    
    
    return v2*.8 + v1*.2   # weighted average



# In[17]:


def heuristic(state,player):
    
    v=in_a_row_heuristic(state,player)
    
    return v

    


# In[18]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    print("heuristic ",heuristic(state,player))
    return move


random_agent=Agent(random_move)


# In[20]:


g=Game(1)
result=g.run(random_agent,random_agent)


# In[ ]:





# In[21]:


g=Game(1)
result=g.run(minimax_agent,random_agent)


# In[ ]:




