#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[6]:


def initial_state():
    board=[0,0,0,0,0,0,0,0,0]
    return board


# In[7]:


def initial_state():
    board=Board(3,3)
    
    return board


# In[8]:


# debugging code....
initial_state()


# In[9]:


state=initial_state()


# In[10]:


state


# In[11]:


state[5]=2


# In[13]:


state[0]=5


# In[14]:


state


# In[15]:


state[0,0]


# In[16]:


state[1,2]


# In[17]:


def show_state(state):
    print(state)


# In[18]:


show_state(state)


# In[23]:


def valid_moves(state,player):  # returns a list of all of the possible moves given a state
    moves=[]
    
    for i in range(9):
        if state[i]==0:
            moves.append(i)
    
    return moves
    


# In[24]:


state=initial_state()
valid_moves(state,1)


# In[25]:


state=initial_state()
state[4]=1
state[2]=2
valid_moves(state,1)


# In[26]:


show_state(state)


# In[20]:


a=[]
a.append(2)
a.append(5)
a


# In[21]:


a.append(5)


# In[22]:


a


# In[29]:


def update_state(state,player,move):
    
    new_state=state
    state[move]=player
    
    return new_state


# In[30]:


state=initial_state()
player=1
move=4


# In[31]:


state=update_state(state,player,move)
state


# In[32]:


state=update_state(state,2,8)


# In[33]:


state


# In[34]:


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
    


# In[35]:


state=initial_state()
win_status(state,1)


# In[36]:


for i in range(9):
    state[i]=1
state


# In[37]:


win_status(state,1)


# In[38]:


win_status(state,2)


# In[42]:


def human_move(state,player):
    print("""
     0 1 2
     3 4 5
     6 7 8
    """)
    
    move=int(input("What move?"))
    
    return move


# In[43]:


state=initial_state()
player=1
move=human_move(state,player)


# In[44]:


move


# In[45]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


# In[ ]:





# In[47]:


state=initial_state()
player=1
move=random_move(state,player)
move


# In[48]:


player=1
state=initial_state()

while True:
    
    print("Player",player)
    show_state(state)
    
    if player==1:
        move=human_move(state,player)
    else:
        move=random_move(state,player)
        
    if not move in valid_moves(state,player):
        print("BADBADBAD")
        break
        
    state=update_state(state,player,move)
    if win_status(state,player)=='win':
        print("win!")
        break
    if win_status(state,player)=='lose':
        print("lose!")
        break
    if win_status(state,player)=='stalemate':
        print("tie!")
        break
        
    if player==1:
        other_player=2
    else:
        other_player=1

    player,other_player=other_player,player


# In[ ]:




