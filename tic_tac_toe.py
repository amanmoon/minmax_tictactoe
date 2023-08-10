import numpy as np
class tic_tac_toe:
    
    def __init__(self):
        self.row_number=3
        self.column_number=3

    def initialise_state(self):
        return np.zeros((self.column_number,self.row_number))

    def valid_moves(self,state):
        moves=list()
        for value,player in enumerate(state.reshape(-1)):
            if player==0:
                moves.append(value)
        return moves

    def state_modify(self,state,action,player):
        row=action//3
        col=action%3
        state[row,col]=player
        return state

    def check_terminal_state(self,state,action,player):
        row=action//3
        col=action%3
        if (np.sum(state[row,:])==player*self.row_number 
            or np.sum(state[:,col]==player*self.column_number) 
            or np.trace(state)==player*self.row_number 
            or np.trace(np.fliplr(state))==player*self.row_number):
            return True ,player
        elif 0 not in state.reshape(-1):
            return True,0
        else:
            return False,None                
            
    def change_player(self,player):
        return -player

# game=tic_tac_toe()
# state=game.initialise_state()
# player=1
# while True:
#     print(state)
#     print(game.valid_moves(state))
#     move=int(input("enter one move:"))
#     if move in game.valid_moves(state):
#         state=game.state_modify(state,move,player)
#     else:
#         print("right move daal madarchood")
#         continue
#     end,winner=game.check_terminal_state(state,move,player)
#     if end and winner!=0:
#         print(state)
#         print(f"the winner is {winner}")
#         break
#     elif end and winner==0:
#         print(state)
#         print("the game is draw")
#         break
#     player=game.change_player(player)