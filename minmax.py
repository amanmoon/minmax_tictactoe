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
        if all(i == maxvalue[0] for i in maxvalue):
            return self.child[random.randrange(len(maxvalue))]
        index_max=maxvalue.index(max(maxvalue))
        return self.child[index_max]

    def sigma_move_min(self):
        minvalue=list()
        for children in self.child:
            minvalue.append(children.value)
        if all(i == minvalue[0] for i in minvalue):
            return self.child[random.randrange(len(minvalue))]
        index_min=minvalue.index(min(minvalue))
        return self.child[index_min]
        
    def noob_move(self,action):
        row=action//3
        col=action%3
        self.state[row,col]=self.player
        for children in self.child:
            if (children.state == self.state).all():
                print(children)
                return children
        
    def calculate_win(self):
        child_value=list()
        for children in self.child:
            child_value.append(children.value)
            
        if self.player==1:
            self.value=max(child_value)            
        if self.player==-1:
            self.value=min(child_value)
        
    def get_layers_deepest_first(root):
        current_layer=[root]
        next_layer=[]
        deepest_first_list=list()
        
        while True:
            for childrens in current_layer:
                childrens.expand()
                next_layer.extend(childrens.child)
            deepest_first_list=next_layer+deepest_first_list
            current_layer=next_layer.copy()
            next_layer.clear()
            if current_layer==[]:
                break
        return deepest_first_list
        
    def run_backprop(root):
        list=node.get_layers_deepest_first(root)
        for nodes in list:
            if nodes.check_terminal():
                continue
            nodes.calculate_win()

game=t()
state=game.initialise_state()
human=int(input("As what you wish to play:"))
state=node(state,human)
node.run_backprop(state)



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