from tic_tac_toe import tic_tac_toe as t
import numpy as np
class node:
    def __init__(self,state,player,parent=None,child=[]):
        self.child=child
        self.player=player 
        self.state=state
        self.parent=parent
        
    def expand(self):
        valid_moves=t.valid_moves(self.state)
        children=list()
        for move in valid_moves:
            child_state=t.state_modify(self.state.copy(),move,-self.player)
            children.append(node(child_state,-self.player,self))
        self.child=children
        
    def check_terminal(self):
        
        for row in range(3):
            if np.all(self.state[row, :] == self.player):
                return True, self.player
                
        for col in range(3):
            if np.all(self.state[:, col] == self.player):
                return True, self.player

        if np.trace(self.state) == self.player * 3:
            return True, self.player

        if np.trace(np.fliplr(self.state)) == self.player * 3:
            return True, self.player
        return False,None
    
    
    
    def __repr__(self):
        return f"{self.state}"
        



        
g=t()
state=g.initialise_state()
a=node(state,1)
a.expand()
b=a.child[0]
b.expand()
c=b.child[5]
c.expand()
d=c.child[3]

print(d)