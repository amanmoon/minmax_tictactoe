from typing import Any
from tic_tac_toe import tic_tac_toe as t
class node:
    def __init__(self,state,player,child=[]):
        self.child=child
        self.player=player 
        self.state=state
        
    def expand(self):
        valid_moves=t.valid_moves(self.state)
        children=list()
        for move in valid_moves:
            child_state=t.state_modify(self.state.copy(),move,-self.player)
            children.append(node(child_state,-self.player))
        self.child=children
        return children

    def __repr__(self):
        return f"{self.state}"
        
        
        
g=t()
state=g.initialise_state()
n=node(state,1)
n.expand()
k=n.child[0].expand()[0].expand()[1]
print(k)