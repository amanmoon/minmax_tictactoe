from tic_tac_toe import tic_tac_toe as t
import numpy as np
class node:
    def __init__(self,state,player,parent=None):
        self.value=0
        self.child=list()
        self.player=player 
        self.state=state
        self.parent=parent
        self.win=0
        self.loss=0
        
    def expand(self):
        valid_moves=t.valid_moves(self.state)
        children=list()
        for move in valid_moves:
            child_state=t.state_modify(self.state.copy(),move,-self.player)
            children.append(node(child_state,-self.player,self))
        self.child=children
        
    def check_terminal(self,computer_player):
        
        for row in range(3):
            if np.sum(self.state[row, :] == 3*computer_player):
                self.value=computer_player
                self.win=1
                return True
                
        for col in range(3):
            if np.sum(self.state[:, col] == 3*computer_player):
                self.value=computer_player
                self.win=1
                return True

        if np.trace(self.state) == computer_player * 3 or np.trace(np.fliplr(self.state)) == computer_player * 3:
            self.value=computer_player
            self.win=1
            return True

        if 0 not in self.state.reshape(-1):
            return True
        
        for row in range(3):
            if np.sum(self.state[row, :] == -3*computer_player):
                self.value=-computer_player
                self.loss=1
                return True
                
        for col in range(3):
            if np.sum(self.state[:, col] == -3*computer_player):
                self.value=-computer_player
                self.loss=1
                return True

        if np.trace(self.state) == self.player * -3 or np.trace(np.fliplr(self.state)) == computer_player * -3:
            self.value=-computer_player
            self.loss=1
            return True
        
        return False
    
    def __repr__(self):
        return f"{self.state}"
        

    def calculate_win_loss(self,computer_player):
        for children in self.child:
            if children.value==computer_player:
                self.win+=1
            if children.value==-(computer_player):
                self.loss+=1
                
    def sigma_move(self,game_state):
        bestmove_list=self.child.sort(key=lambda node:((node.win)+1)/((node.loss)+1))
        bestmove=bestmove_list[0]
        game_state=bestmove
        return game_state         
        
g=t()
state=g.initialise_state()
a=node(state,1)
a.expand()
b=a.child[0]
b.expand()
c=b.child[5]
c.expand()
d=c.child[3]
d.expand()
e=d.child[0]
e.expand()
f=e.child[0]
f.expand()
g=f.child[0]
g.expand()
h=g.child[0]
h.expand()
i=h.child[0]
i.expand()
j=i.child[0]
j.check_terminal(-1)
i.calculate_win_loss(-1)
print(j,"\n",i.win,i.loss,j.player)