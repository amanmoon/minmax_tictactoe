from minmax import node as n
from tic_tac_toe import tic_tac_toe as t

def play():
    
    game=t()
    state=game.initialise_state()
    action=int(input("Your turn enter move: "))
    t.state_modify(state,action,player)