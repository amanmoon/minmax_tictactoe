from minmax import node as n
from tic_tac_toe import tic_tac_toe as t

def play(player):
    computer_player=-int(input("What you wish to play as:"))
    game=t()
    state=game.initialise_state()
    while True:
        print(state)
        action=int(input("Your turn enter move: "))
        t.state_modify(state,action,player)
        nodestate=n(state,player=-computer_player)
        runbackpropagation(nodestate,computer_player)
        # n.check_terminal()
        n.sigma_move(nodestate,state,computer_player)
    
    
play(1)