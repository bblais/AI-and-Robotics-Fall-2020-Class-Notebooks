from Game import *

def initial_state(N=20):
    return N

def show_state(state):
    print("There are ",state,"sticks.")
    
def valid_moves(state,player):
    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]
    
def update_state(state,player,move):
    # move = number of sticks to pick up
    new_state=state-move # remove the sticks
    return new_state

def win_status(state,player):
    if state==0:
        return 'lose'
    elif state==1:
        return 'win'
    else:
        return None
    
def human_move(state,player):
    print("Player ",player)
    move=int(input("How many sticks?"))
    return move

def random_move(state,player):
    possible_moves=valid_moves(state,player)
    move=random.choice(possible_moves)
    return move


random_agent=Agent(random_move)


def plot(something):
    print("Here I am!")