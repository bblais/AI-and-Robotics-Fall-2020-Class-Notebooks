#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Rules of the Game

# In[2]:


def initial_state():
    board=Board(3,3)
    board.pieces=['.','X','O']
    return board

def show_state(state):
    print(state)
    
def valid_moves(state,player):  # returns a list of all of the possible moves given a state
    moves=[]
    
    for i in range(9):
        if state[i]==0:
            moves.append(i)
    
    return moves
    
def update_state(state,player,move):
    
    new_state=state
    state[move]=player
    
    return new_state

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
    


# ## Agents

# In[3]:


def human_move(state,player):
    print("""
     0 1 2
     3 4 5
     6 7 8
    """)
    
    move=int(input("What move?"))
    
    return move

human_agent=Agent(human_move)


# In[4]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


random_agent=Agent(random_move)


# ## Minimax agent
# 
# <img src='images/ttt minimax 1.jpeg' width=750>
# <br>
# <img src='images/ttt minimax 2.jpeg' width=750>
# <br>
# <img src='images/ttt minimax 3.jpeg' width=750>
# <br>
# 

# In[ ]:








# In[ ]:





# In[5]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[6]:


state=initial_state()
for loc in [0,7,8]:
    state[loc]=2
    
for loc in [2,3,6]:
    state[loc]=1


state


# In[7]:


minimax_values(state,1)


# ## how does it work?

# In[8]:


def minimax_values_example(current_state,player):

    from copy import deepcopy
    
    if player==1:
        other_player=2
    else:
        other_player=1

    values=[]
    states=[]

    moves=valid_moves(current_state,player)
    available_states=[update_state(deepcopy(current_state),player,move)
                                for move in moves]
    
    print("minimax_values_example current state\n")
    print(current_state)
    print("Getting MIN value for states")
    for s in available_states:
        print(s)
    
    for state in available_states:
        value=minvalue_example(state,other_player)
        values.append(value)
        states.append(state)

    return values,moves


# In[9]:


def minvalue_example(current_state,player,depth=1):
    if player==1:
        other_player=2
    else:
        other_player=1

    # since win_status is called with a player and an updated state
    # the current state is really the updated state from the
    # other player's last move.

    tabs='\t'*depth
    print(tabs,"MIN value current state\n")
    s=current_state
    print('\n'.join([tabs +_ for _ in str(s).split('\n')]))    
    
    status=win_status(current_state,other_player)

    if status=='win':  # bad for min
        print(tabs,"end state value: 1")
        return 1
    elif status=='lose':  # good for min
        print(tabs,"end state value: -1")
        return -1
    elif status=='stalemate':  # draw
        print(tabs,"end state value: 0")
        return 0


    moves=valid_moves(current_state,player)
    available_states=[update_state(deepcopy(current_state),player,move)
                                for move in moves]
    
    
    print(tabs,"Getting MAX value for states")
    for s in available_states:
        print('\n'.join([tabs +_ for _ in str(s).split('\n')]))    
    
    
    values=[]
    for state in available_states:
        value=maxvalue_example(state,other_player,depth+1)
        values.append(value)
                
    if not values:  # no available states  = stalemate
        return 0
    else:
        return min(values)
     
        
def maxvalue_example(current_state,player,depth=1):
    if player==1:
        other_player=2
    else:
        other_player=1

    # since win_status is called with a player and an updated state
    # the current state is really the updated state from the
    # other player's last move.
    tabs='\t'*depth
    print(tabs,"MAX value current state\n")
    s=current_state
    print('\n'.join([tabs +_ for _ in str(s).split('\n')]))    


    status=win_status(current_state,other_player)

    if status=='win':  # bad for max
        print(tabs,"end state value: -1")
        return -1
    elif status=='lose':  # good for max
        print(tabs,"end state value: 1")
        return 1
    elif status=='stalemate':  # draw
        print(tabs,"end state value: 0")
        return 0


    moves=valid_moves(current_state,player)
    available_states=[update_state(deepcopy(current_state),player,move)
                                for move in moves]
    print(tabs,"Getting MIN value for states")
    for s in available_states:
        print('\n'.join([tabs +_ for _ in str(s).split('\n')]))    
    
    values=[]
    for state in available_states:
        value=minvalue(state,other_player,depth+1)
        values.append(value)
                
    if not values:  # no available states  = stalemate
        return 0
    else:
        return max(values)
             


# In[10]:


minimax_values_example(state,1)


# # Minimax vs random

# In[13]:


g=Game()
g.run(minimax_agent,random_agent)


# ## Turning off the display, playing multiple games

# In[15]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[16]:


g=Game(number_of_games=10)
g.display=False
g.run(minimax_agent,random_agent)
g.report()


# In[ ]:

























# ## Maximum Depth -- need to set a heuristic

# In[18]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,maxdepth=2,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)

def heuristic(state,player):
    # a really bad heuristic -- just do random!
    return random.choice([-1,0,1])
    


# In[20]:


g=Game(number_of_games=10)
g.display=False
g.run(minimax_agent,random_agent)
g.report()


# In[ ]:




