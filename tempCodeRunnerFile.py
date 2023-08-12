visited.add(v)
                for child in v.child:
                    build_topo(child)
                topo.append(v)
        build_topo(initial_node)
        for nodes in topo:
            if nodes.check_terminal(computer_player):
                continue            
            nodes.calculate_win(computer_player)