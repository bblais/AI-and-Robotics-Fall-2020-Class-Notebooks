#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Game import *


# ## Rules of the Game

# - before each roll, we can either choose to roll or hold
# - roll a die
#     - if it is a 1, turn score goes to zero (or 1), the turn stops and goes to the next player
#     - if not a 1, add to the turn score the number rolled, and have another turn
# - hold
#     - turn score gets added to my current score
#     - goes to the next player
# - first to 21 wins

# 1. what is a move?  (how do we represent it, what are possibilities)
#     - "roll", "hold"
# 2. what is a state?  (how do we represent it, what are possibilities)
#     - your current score, their current score, turn score

# In[3]:


def valid_moves(state,player):
    return ["roll","hold"]

def initial_state():
    # your current score, their current score, turn score
    return [0,0,0]


# In[4]:


def show_state(state):
    print("Player 1 score is ",state[0])
    print("Player 2 score is ",state[1])
    print("Turn score is ",state[2])    


# In[30]:


def win_status(state,player):
    
    # playing until 101
    max_score=101
    
    if player==1:
        current_score=state[0]
        other_score=state[1]
    else:
        current_score=state[1]
        other_score=state[0]
        
    turn_score=state[2]
    
    if current_score+turn_score>=max_score:
        return 'win'
    
    


# In[31]:


def update_state(state,player,move):
    
    # if hold, update the scores
    
    # if roll, then random number 1-6, if 1, ....
    # update turn score
    new_state=state
    
    if move=='hold':
        
        # state[player-1]+=state[2]
        
        if player==1:
            new_state[0]+=state[2]  # add the turn score to player 1's current score
        else:
            new_state[1]+=state[2]  # add the turn score to player 1's current score
        
        new_state[2]=0  # reset the turn score
        
    else:  #  roll
        dice=random.randint(1,6)
        
        if dice==1:
            new_state[2]=0  # reset the turn score
        else:
            new_state[2]+=dice
            
    
    return new_state


# In[32]:


def repeat_move(state,player,move):
    turn_score=state[2]
    
    if turn_score>0:
        return True
    
    return False
    


# In[33]:


def human_move(state,player):
    print("Player ",player)
    s=input("hold or roll?")
    
    if s[0]=='h':
        return 'hold'
    else:
        return 'roll'
    
human_agent=Agent(human_move)


# In[34]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


random_agent=Agent(random_move)


# In[35]:


max_score=101
saved_p={}
saved_whether_roll={}

def p_win(i,j,k):  # i = my score, j is the other score, k is the turn score
    
    if i+k>=max_score:
        return 1
    
    if j>=max_score:
        return 0.0
    
    
    if (i,j,k) in saved_p:
        return saved_p[(i,j,k)]
    

    # if I roll a one
    #p_win_roll=1-(probability that I lose, handing it off to the other)
    p_win_roll=1-p_win(j,i+1,0)
    
    # if I roll a two, three,
    for dice in [2,3,4,5,6]:  # range(2,6+1) is equal but unreadable
        p_win_roll+=p_win(i,j,k+dice)
    
    p_win_roll/=6
    
    if k==0:  # add 1 even when the turn score is zero
        p_win_hold=1-p_win(j,i+1,0)
    else:
        p_win_hold=1-p_win(j,i+k,0)

        
    # assume that we are rational
    if p_win_roll>p_win_hold:
        p=p_win_roll
        saved_whether_roll[(i,j,k)]=True
    else:
        p=p_win_hold
        saved_whether_roll[(i,j,k)]=False
        
    
    saved_p[(i,j,k)]=p
    
    return p


# In[36]:


def probability_move(state,player):
    
    i,j,k=state
    
    p=p_win(i,j,k)
    roll=saved_whether_roll[(i,j,k)]
    
    if roll:
        return "roll"
    else:
        return "hold"
    
probability_agent=Agent(probability_move)


# In[12]:


from Game.minimax import *
def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[13]:


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


# In[14]:


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
        


# In[15]:


Q1_agent=Agent(Q_move)
Q1_agent.Q=LoadTable('Q1_Pig_data.json')
Q1_agent.post=Q_after

Q1_agent.α=0.3  # learning rate
Q1_agent.γ=0.9  # memory constant, discount factor
Q1_agent.ϵ=0.1  # probability of a random move during learning

Q2_agent=Agent(Q_move)
Q2_agent.Q=LoadTable('Q2_Pig_data.json')
Q2_agent.post=Q_after

Q2_agent.α=0.3  # learning rate
Q2_agent.γ=0.9  # memory constant, discount factor
Q2_agent.ϵ=0.1  # probability of a random move during learning


# In[ ]:





# In[40]:


g=Game(number_of_games=1000)
g.display=False
g.run(probability_agent,random_agent);


# In[41]:


g.percent_win_lose_tie()


# In[42]:


def bob_move(state,player):
    return "roll"

bob=Agent(bob_move)


# In[43]:


g=Game(number_of_games=1000)
g.display=False
g.run(probability_agent,bob);


# In[44]:


g.percent_win_lose_tie()


# In[ ]:




