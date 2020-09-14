#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Game import *


# ## Rules of the Game

# In[3]:


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

# In[4]:


def human_move(state,player):
    print("""
     0 1 2
     3 4 5
     6 7 8
    """)
    
    move=int(input("What move?"))
    
    return move

human_agent=Agent(human_move)


# In[5]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


random_agent=Agent(random_move)


# In[6]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[7]:


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


# In[ ]:





# In[8]:


g=Game()
g.run(minimax_agent,skittles_agent)


# In[9]:


skittles_agent.S


# In[ ]:





# In[12]:


g=Game(100)
g.display=False
result=g.run(skittles_agent,skittles_agent2)
g.report()


# In[14]:


SaveTable(skittles_agent.S,"ttt player 1 skittles.json")
SaveTable(skittles_agent2.S,"ttt player 2 skittles.json")


# In[ ]:


number_of_batches=100
wins=[]
losses=[]
ties=[]
skittles_agent.S=Table()
total_number_of_games=0
for i in range(number_of_batches):
    N=1000
    g=Game(N)
    g.display=False
    result=g.run(skittles_agent,random_agent)
    wins.append(sum([r==1 for r in result]))
    losses.append(sum([r==2 for r in result]))
    ties.append(sum([r==0 for r in result]))
    total_number_of_games+=N
    print("total games ",total_number_of_games,"W L T",wins[-1],losses[-1],ties[-1])


# In[ ]:




