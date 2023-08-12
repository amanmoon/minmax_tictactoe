import numpy as np
class tic_tac_toe:
    
    def __init__(self):
        self.row_number=3
        self.column_number=3

    def initialise_state(self):
        return np.zeros((self.column_number,self.row_number))

    def valid_moves(state):
        moves=list()
        for value,player in enumerate(state.reshape(-1)):
            if player==0:
                moves.append(value)
        return moves

    def state_modify(state,action,player):
        row=action//3
        col=action%3
        state[row,col]=player
        return state

    def check_terminal_state(self,state,action,player):
        row=action//3
        col=action%3
        print("the row and col is",row,col,player)
        if (sum(state[row,:])==player*self.row_number 
            or sum(state[:,col])==player*self.column_number
            or np.trace(state)==player*self.row_number 
            or np.trace(np.fliplr(state))==player*self.row_number):
            return True ,player
        elif 0 not in state.reshape(-1):
            return True,0
        else:
            return False,None                
            
    def change_player(player):
        return -player

    def play(self,start_player):
        player=start_player
        state=self.initialise_state()
        while True:
            print(state)
            print(tic_tac_toe.valid_moves(state))
            move=int(input(f"Turn of player {player} \nEnter valid move:"))
            if move not in tic_tac_toe.valid_moves(state):
                print("Please enter valid move:")
                continue
            tic_tac_toe.state_modify(state,move,player)
            terminate,winner=self.check_terminal_state(state,move,player)
            if terminate and(winner!=0):
                print(state)
                print(f"the winner is {winner}")
                break
            if terminate and (winner==0):
                print(state)
                print("The game is tie")
                break
            player=tic_tac_toe.change_player(player)
            
if __name__ == "__main__":
    game = tic_tac_toe()
    game.play()
    
# game=tic_tac_toe()
# game.play(-1)