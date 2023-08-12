from minmax import node as n
from tic_tac_toe import tic_tac_toe as t

def play(player):
    computer_player=-int(input("What you wish to play as:"))
    game=t()
    state=game.initialise_state()
    nodestate=n(state,player=-computer_player)
    while True:
        print(state)
        action=int(input("Your turn enter move: "))
        t.state_modify(state,action,player)
        runbackpropagation(nodestate,computer_player)
        n.sigma_move(nodestate,state,computer_player)
    
    
def runbackpropagation(initial_node,computer_player):
        topo=[]    
        visited=set()
        def build_topo(v):
            if v not in visited:
                v.expand()
                visited.add(v)
                for child in v.child:
                    build_topo(child)
                topo.append(v)
        build_topo(initial_node)
        for nodes in topo:
            if nodes.check_terminal(computer_player):
                continue            
            nodes.calculate_win(computer_player)


play(1)