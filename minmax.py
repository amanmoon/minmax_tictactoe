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
        
    def expand(self,computer_player):
        if node.check_terminal(self,computer_player):
            exit
        valid_moves=t.valid_moves(self.state)
        children=list()
        for move in valid_moves:
            child_state=t.state_modify(self.state.copy(),move,self.player)
            children.append(node(child_state,-(self.player),self))
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
                return True
                
        for col in range(3):
            if np.sum(self.state[:, col] == -3*computer_player):
                self.value=-computer_player
                return True

        if np.trace(self.state) == self.player * -3 or np.trace(np.fliplr(self.state)) == computer_player * -3:
            self.value=-computer_player
            return True
        
        return False
    
    def __repr__(self):
        return f"{self.state}"
        

    def calculate_win(self,computer_player):
        for children in self.child:
            if children.value==self.player:
                self.value=self.player
            if children.value==-self.player:
                self.value=-self.player
            if children.value==computer_player:
                self.win+=1
                
    def sigma_move(self,game_state,computer_player):
        for children in self.child:
            if children.value==-computer_player:
                self.child.remove(children)
            
        bestmove_list=self.child.sort(key=lambda node:(node.win),reverse=True)
        bestmove=bestmove_list.pop(0)
        game_state=bestmove
        return game_state
    
    @staticmethod
    def node_search(node,computer_player):
        topo=[]    
        visited=set()
        def build_topo(v):
            if v not in visited:
                v.expand()
                visited.add(v)
                for child in v.child:
                    build_topo(child)
                topo.append(v)
        build_topo(node)
        return topo
        for nodes in topo:
            if nodes.check_terminal(computer_player):
                continue
            nodes.calculate_win(computer_player)
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
            if nodes.check_terminal(computer_player):
                continue
            nodes.calculate_win(computer_player)
            
def visualize_tree(node, depth=0):
    indentation = "  " * depth
    print(f"{indentation}Value: {node.value}, Win: {node.win}")
    
    for child in node.child:
        visualize_tree(child, depth + 1)
        
game=t()
state=game.initialise_state()
sta=node(state,1)

print(node.run_backprop(sta,-1))