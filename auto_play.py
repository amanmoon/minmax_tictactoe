from minmax import node as n
from tic_tac_toe import tic_tac_toe as t
game=t()
state=game.initialise_state()
human=int(input("As what you wish to play:"))
state=n(state,human)
n.run_backprop(state)



while True:
    print(state)
    print(t.valid_moves(state.state))
    move=int(input("Enter a move:"))
    while True:
        if move not in t.valid_moves(state.state):
            print(t.valid_moves(state.state))
            move=int(input("Enter a valid move:"))
        else:
            break
    state=state.noob_move(move)
    state=state.sigma_move_max() if human==-1 else state.sigma_move_min()
    end,winner=t.check_terminal_state(state.state,move,state.player)
    if end and winner==human:
        print("You Won! Congatulations")
        break
    elif end and winner==-human:
        print("you lost bitch.")
        break
    elif end and winner==0:
        print("The game is tie.")
        break