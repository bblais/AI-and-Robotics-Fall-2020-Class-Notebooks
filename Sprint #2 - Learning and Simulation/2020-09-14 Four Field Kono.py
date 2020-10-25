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


# In[13]:


def valid_moves(state,player):
    
    #  0  1  2  3 
    #  4  5  6  7 
    #  8  9 10 11 
    # 12 13 14 15     
    if player==1:
        other_player=2
    else:
        other_player=1
    
    moves=[]
    # right/left-moving capture
    for start in [0,1,4,5,8,9,12,13]:
        middle=start+1
        end=start+2
        
        # right jump
        if state[start]==player and state[middle]==player and state[end]==other_player:
            moves.append([start,end])
        # left jump
        if state[end]==player and state[middle]==player and state[start]==other_player:
            moves.append([start,end])
    
    # up/down-moving capture
    for start in [0,1,2,3,4,5,6,7]:
        middle=start+4
        end=start+8
        
        # down jump
        if state[start]==player and state[middle]==player and state[end]==other_player:
            moves.append([start,end])
        # up jump
        if state[end]==player and state[middle]==player and state[start]==other_player:
            moves.append([start,end])
        
    # right/left moves
    for r in range(4):
        # right
        for c in range(3):
            if state[r,c]==player and state[r,c+1]==0:
                moves.append([
                        state.index_from_rc(r,c),
                        state.index_from_rc(r,c+1)
                ])
                
        for c in range(1,4):
            if state[r,c]==player and state[r,c-1]==0:
                moves.append([state.index_from_rc(r,c),state.index_from_rc(r,c-1)])                
                
    # up/down moves
    for c in range(4):
        # up
        for r in range(3):
            if state[r,c]==player and state[r+1,c]==0:
                moves.append([state.index_from_rc(r,c),state.index_from_rc(r+1,c)])
        # down     
        for r in range(1,4):
            if state[r,c]==player and state[r-1,c]==0:
                moves.append([state.index_from_rc(r,c),state.index_from_rc(r-1,c)])                

    return moves


# In[14]:


state=initial_state()
show_state(state)
state.show_locations()

print(valid_moves(state,1))


# In[15]:


state=initial_state()
state[4]=0
show_state(state)
state.show_locations()

print(valid_moves(state,1))


# In[16]:


def human_move(state,player):
    print("Player ",player)
    state.show_locations()
    
    start=int(input("What location to start?"))
    end=int(input("What location to end?"))
    move=[start,end]
    
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


# In[19]:


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


skittles_agent2=Agent(skittles_move)
skittles_agent2.S=Table()
skittles_agent2.post=skittles_after


# In[21]:


g=Game()
g.run(random_agent,random_agent)


# In[ ]:




