from boardValue import calculate_node_value

def min_max_agent(root, depth, agent):
    '''
    Maximizar ou minimizar lucro
    '''

    if(depth == 0):
        return calculate_node_value(agent, root.board) , root

    # Cria filhos do nó:
    root.create_children()

    if(agent == 'player_1'):
        max_value = -float('inf')
        max_child = root

        for child in root.children :
            value , child = min_max_agent(child, depth-1, 'player_2')

            if(value > max_value):
                max_value = value
                max_child = child

        return max_value , max_child

    else:
        min_value = float('inf')
        min_child = root

        for child in root.children :
            value , child = min_max_agent(child, depth-1, 'player_1')

            if(value < min_value):
                min_value = value
                min_child = child

        return min_value , min_child