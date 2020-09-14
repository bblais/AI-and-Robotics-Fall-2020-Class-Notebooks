#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# https://en.wikipedia.org/wiki/Four_Field_Kono
# 
# The goal of each player is to capture the other player's pieces and reduce it to one. This is because with only one piece, a player can no longer execute a capture. Another way to win is for a player to immobilize the other player's pieces so that they cannot move or capture.
# 
# The game is played according to these rules.[1]
# 
# 1. Players decide what color marbles to play, and who goes first.
# 2. The board is completely filled with the 16 marbles in the beginning. Each player's marbles are set up on their half of the board.
# 3. Since the board is filled up in the beginning and hence no vacant holes, the first move by the first player will be a capturing move.
# 4. A capturing move requires a player's marble to jump over one of his own adjacent marbles orthogonally (not diagonally), and to land onto an enemy marble which is then removed from the board and replaced with the player's marble. Only one marble can be used to capture or move per turn. Multiple captures are not allowed. Once a marble has captured one enemy marble, the turn is completed. Captures are not compulsory.
# 5. A marble can move orthogonally (not diagonally) one space per turn onto a vacant hole.
# 6. Players alternate their turns throughout the game.
# 
# 
# 
# <img src="images/2019-09-24 07.21.03 am.png" width=100>
# 
# 
# <img src="images/2019-09-24 07.24.27 am.png" width=400>
# 

# In[4]:


def initial_state():
    state=Board(4,4)
    
    for r in range(4):
        for c in range(2):
            state[r,c]=1
            state[r,c+2]=2
    return state


# In[6]:


state=initial_state()
state.show_locations()
state


# In[7]:


def show_state(state):
    print(state)
    
def update_state(state,player,move):
    # a move is a start and an end
    start,end=move
    new_state=state
    new_state[start]=0
    new_state[end]=player
    return new_state


# In[8]:


def win_status(state,player):
    if player==1:
        other_player=2
    else:
        other_player=1
        
    if not valid_moves(state,other_player):
        return 'win'
    
    # count the pieces of the other player
    count=0
    for i in range(16):
        if state[i]==other_player:
            count+=1
    if count==1:
        return 'win'
    
    return None  # middle of the game


# In[ ]:


def valid_moves(state,player):
    
    #  0  1  2  3 
    #  4  5  6  7 
    #  8  9 10 11 
    # 12 13 14 15     
    

    # right-moving capture
    for start in []
    

