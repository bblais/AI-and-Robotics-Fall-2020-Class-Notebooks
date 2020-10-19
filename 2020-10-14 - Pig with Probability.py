#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# In[29]:


def valid_moves(state,player):
    return ["roll","hold"]

def initial_state():
    # your current score, their current score, turn score, max_score, last die
    return [0,0,0,101,0]


# In[30]:


def show_state(state):
    
    i,j,k,max_score,last_die=state
    
    if last_die==0:  # new turn
        print("====")
    else:
        print("Rolled ",last_die)
        
    print("%d\t%d\t%d" % (i,j,k))
    
    print()
    


# In[31]:


def win_status(state,player):
    
    max_score=state[3]
    
    if player==1:
        current_score=state[0]
        other_score=state[1]
    else:
        current_score=state[1]
        other_score=state[0]
        
    turn_score=state[2]
    
    if current_score+turn_score>=max_score:
        return 'win'
    
    


# In[32]:


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
        last_die=0
        state[4]=last_die
        
    else:  #  roll
        dice=random.randint(1,6)
        
        if dice==1:
            new_state[2]=0  # reset the turn score
        else:
            new_state[2]+=dice
            
        last_die=dice
        state[4]=last_die
    
    return new_state


# In[33]:


def repeat_move(state,player,move):
    turn_score=state[2]
    
    if turn_score>0:
        return True
    
    return False
    


# In[34]:


def human_move(state,player):
    print("Player ",player)
    s=input("hold or roll?")
    
    if s[0]=='h':
        return 'hold'
    else:
        return 'roll'
    
human_agent=Agent(human_move)


# In[35]:


def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


random_agent=Agent(random_move)


# In[36]:


saved_p={}
saved_p_win_roll={}
saved_p_win_hold={}
saved_whether_roll={}

def p_win(i,j,k,max_score=21):  # i = my score, j is the other score, k is the turn score
    
    if i+k>=max_score:
        return 1
    
    if j>=max_score:
        return 0.0
    
    
    if (i,j,k,max_score) in saved_p:
        return saved_p[(i,j,k,max_score)]
    

    # if I roll a one
    #p_win_roll=1-(probability that I lose, handing it off to the other)
    p_win_roll=1-p_win(j,i+1,0,max_score)
    
    # if I roll a two, three,
    for dice in [2,3,4,5,6]:  # range(2,6+1) is equal but unreadable
        p_win_roll+=p_win(i,j,k+dice,max_score)
    
    p_win_roll/=6
    
    if k==0:  # add 1 even when the turn score is zero
        p_win_hold=1-p_win(j,i+1,0,max_score)
    else:
        p_win_hold=1-p_win(j,i+k,0,max_score)

        
    # assume that we are rational
    if p_win_roll>p_win_hold:
        p=p_win_roll
        saved_whether_roll[(i,j,k,max_score)]=True
    else:
        p=p_win_hold
        saved_whether_roll[(i,j,k,max_score)]=False
        
    
    saved_p[(i,j,k,max_score)]=p
    saved_p_win_roll[(i,j,k,max_score)]=p_win_roll
    saved_p_win_hold[(i,j,k,max_score)]=p_win_hold
    
    return p


# In[37]:


i,j,k,max_score=(20,18,0,30)
p=p_win(i,j,k,max_score)
saved_p_win_roll[(i,j,k,max_score)],saved_p_win_hold[(i,j,k,max_score)]


# In[38]:


keys=list(saved_p_win_roll.keys())


# In[39]:


for i,key in enumerate(keys):
    print(key,saved_p_win_roll[key])
    if i>10:
        break


# In[40]:


def probability_move(state,player):
    
    i,j,k,max_score,last_die=state
    
    p=p_win(i,j,k,max_score)
    roll=saved_whether_roll[(i,j,k,max_score)]
    
    if roll:
        return "roll"
    else:
        return "hold"
    
probability_agent=Agent(probability_move)


# In[ ]:





# In[41]:


g=Game(number_of_games=1)
g.display=True
g.run(probability_agent,random_agent);


# In[42]:


g=Game(number_of_games=1000)
g.display=False
g.run(probability_agent,random_agent);


# In[43]:


g.percent_win_lose_tie()


# In[44]:


def bob_move(state,player):
    return "roll"

bob=Agent(bob_move)


# In[91]:


g=Game(number_of_games=1000)
g.display=False
g.run(probability_agent,bob);


# In[92]:


g.percent_win_lose_tie()


# For Bob to win, he has to roll non-1's up until the max_score.  What is the probability of doing that?

# In[50]:


101/2,101/6


# if bob has to roll $n$ times, the probability of doing that (and not getting a 1) is $(5/6)^n$

# In[51]:


saved_p_win_hold[(0,0,0,101)]


# In[54]:


from numpy.random import randint


# In[86]:


count=0
mx=1000
for i in range(mx):
    r=randint(6,size=50)+1
    r[r==1]=-1e6
    cs=r.cumsum()
    if any(cs>=101):
        count+=1
        
count/mx*100


# In[90]:


1-0.99**17


# In[99]:


g=Game(number_of_games=100)
g.display=False
g.run(bob,bob);


# In[100]:


g.percent_win_lose_tie()


# In[ ]:




