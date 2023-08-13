from tic_tac_toe import tic_tac_toe as t
import numpy as np
import random
class node:
    def __init__(self,state,player,depth=0,parent=None):
        self.value=0
        
        self.child=list()
        self.player=player 
        self.state=state
        self.parent=parent
        self.depth=depth
        
    def expand(self):
        if self.check_terminal():      
            return
        valid_moves=t.valid_moves(self.state)
        children=list()
        for move in valid_moves:
            child_state=t.state_modify(self.state.copy(),move,self.player)
            children.append(node(child_state,-(self.player),self.depth+1,self))
        self.child=children
        
    def check_terminal(self):
        for row in range(3):
            if np.all(self.state[row, :] == -(self.player)):
                self.value = -self.player/self.depth
                return True
                    
        for col in range(3):
            if np.all(self.state[:, col] == -(self.player)):
                self.value = -self.player/self.depth
                return True
    
        if np.trace(self.state) == -(self.player * 3) or np.trace(np.fliplr(self.state)) == -(self.player * 3):
            self.value = -self.player/self.depth
            return True
    
        if 0 not in self.state.reshape(-1):
            return True
        return False
    
    def __repr__(self):
        return f"{self.state}"          
            
    def sigma_move_max(self):
        maxvalue=list()
        for children in self.child:
            maxvalue.append(children.value)
        if all(i == 0 for i in maxvalue):
            return self.child[random.randrange(len(maxvalue))]
        print(maxvalue)
        index_max=maxvalue.index(max(maxvalue))
        print(index_max)
        return self.child[index_max]

    def sigma_move_min(self):
        minvalue=list()
        for children in self.child:
            minvalue.append(children.value)
        if all(i == 0 for i in minvalue):
            return self.child[random.randrange(len(minvalue))]
        print(minvalue)
        index_min=minvalue.index(min(minvalue))
        print(index_min)
        return self.child[index_min]
        
    def noob_move(self,action):
        pass
    def calculate_win(self):
        child_value=list()
        for children in self.child:
            child_value.append(children.value)
            
        if self.player==1:
            self.value=max(child_value)            
        if self.player==-1:
            self.value=min(child_value)
        
    def get_layers_deepest_first(root,computer_player):
        current_layer=[root]
        next_layer=[]
        deepest_first_list=list()
        
        while True:
            for childrens in current_layer:
                childrens.expand(computer_player)
                next_layer.extend(childrens.child)
            deepest_first_list=next_layer+deepest_first_list
            current_layer=next_layer.copy()
            next_layer.clear()
            if current_layer==[]:
                break
        return deepest_first_list
        
    def run_backprop(root,computer_player):
        list=node.get_layers_deepest_first(root,computer_player)
        for nodes in list:
            if nodes.check_terminal():
                continue
            nodes.calculate_win()






# game=t()
# state=game.initialise_state()
# status=node(state,1)
# node.run_backprop(status,-1)
# status=status.sigma_move_max()
# status=status.sigma_move_min()