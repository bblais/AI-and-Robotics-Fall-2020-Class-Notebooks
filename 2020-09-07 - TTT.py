#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():
    board=Board(3,3)
    
    return board


# In[3]:


def show_state(state):
    print(state)


# In[4]:


def valid_moves(state,player):  # returns a list of all of the possible moves given a state
    moves=[]
    
    for i in range(9):
        if state[i]==0:
            moves.append(i)
    
    return moves
    


# In[5]:


def update_state(state,player,move):
    
    new_state=state
    state[move]=player
    
    return new_state


# In[6]:


def win_status(state,player):
    # "win" if the player wins
    # "lose" if the player loses
    # "stalemate" if a tie
    # None if the game continues
    
    # 0 1 2
    # 3 4 5
    # 6 7 8
    
    if state[0]==player and state[1]==player and state[2]==player:
        return "win"
    if state[3]==player and state[4]==player and state[5]==player:
        return "win"
    if state[6]==player and state[7]==player and state[8]==player:
        return "win"
    if state[0]==player and state[3]==player and state[6]==player:
        return "win"
    if state[1]==player and state[4]==player and state[7]==player:
        return "win"
    if state[2]==player and state[5]==player and state[8]==player:
        return "win"
    if state[0]==player and state[4]==player and state[8]==player:
        return "win"
    if state[6]==player and state[4]==player and state[2]==player:
        return "win"
    
    if player==1:
        other_player=2
    else:
        other_player=1
        
        
    if not valid_moves(state,other_player):
        return "stalemate"
    
    
    return None
    


# In[7]:


def human_move(state,player):
    print("""
     0 1 2
     3 4 5
     6 7 8
    """)
    
    move=int(input("What move?"))
    
    return move


# In[8]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


# In[9]:


human_agent=Agent(human_move)
random_agent=Agent(random_move)


# In[10]:


g=Game()
g.run(human_agent,random_agent)


# In[ ]:




