from copy import deepcopy

def create_new_board(board, move, id):

    new_board = deepcopy(board)
    key = [1,0] if id == 'player_1' else [0,1]

    if(move in [0,3,6]):
        new_board[0][move // 3] = key
    elif(move in [1,4,7]):
        new_board[1][move // 3] = key
    else:
        new_board[2][move // 3] = key

    return new_board

def calculate_static_value(agent , board):
    '''
    Retorna pontos adquiridos na atual configuração do tabuleiro
    '''

    #             -------- PONTUAÇÕES --------
    # 10 pontos:
    #
    #   X | X | X   ou   X |    ou    X |   |
    #                    X |            | X |
    #                    X |            |   | X
    #

    # 10 pontos :
    #
    #   X | - | X   ou  X |   ou    X |   |
    #                   - |           | - |
    #                   X |           |   | X

    # 1 ponto :
    #
    #   X |   |     ou   X |   ou    X |   |
    #                    X |           | O |
    #                    O |           |   | X

    # Busca o mínimo ou o máximo?
    if(agent == 'player_1'):
        me = [1,0]
        adversary = [0,1]
    else:
        me = [0,1]
        adversary = [1,0]

    points = 0

    # print(board)
    for board_line in board:
        event_me = board_line.count(me)
        event_adversary = board_line.count(adversary)

        if(event_adversary == 3):
            points += (-1)*100
        elif(event_adversary == 2):
            if(event_me == 0):
                points += (-1)*100
            else:
                points += (-1)
        elif(event_adversary == 1):
            points += (-1)

        if(event_me == 3):
            points += 100
        elif(event_me == 2):
            if(event_adversary == 0):
                points += 10
            else:
                points += 1
        elif(event_me == 1):
            points += 1
    # print(points)


    # Casos 'me' ou 'adversary' na coluna
    column_format = [[board[0][0] , board[1][0] , board[2][0]] ,
                    [board[0][1] , board[1][1] , board[2][1]] ,
                    [board[0][2] , board[1][2] , board[2][2]]]

    # print(column_format)
    for board_column in column_format:
        event_me = board_column.count(me)
        event_adversary = board_column.count(adversary)

        if(event_adversary == 3):
            points += (-1)*100
        elif(event_adversary == 2):
            if(event_me == 0):
                points += (-1)*10
            else:
                points += (-1)
        elif(event_adversary == 1):
            points += (-1)

        if(event_me == 3):
            points += 100
        elif(event_me == 2):
            if (event_adversary == 0):
                points += 10
            else:
                points += 1
        elif(event_me == 1):
            points += 1

    # Casos 'me' ou 'adversary' na diagonal
    diagonal_format = [ [board[0][0] , board[1][1] , board[2][2]] , [board[0][2] , board[1][1] , board[2][0]]]

    # print(diagonal_format)
    for diagonal in diagonal_format:
        event_me = diagonal.count(me)
        event_adversary = diagonal.count(adversary)

        if(event_adversary == 3):
            points += (-1)*100
        elif(event_adversary == 2):
            if(event_me == 0):
                points += (-1)*10
            else:
                points += (-1)
        elif(event_adversary == 1):
            points += (-1)
        if(event_me == 3):
            points += 100
        elif(event_me == 2):
            if(event_adversary == 0):
                points += 10
            else:
                points += 1
        elif(event_me == 1):
            points += 1

    # print(points)

    return points

def change_observation_format(obs):
    new_format = []
    for i in range(3):
        aux = []
        for column in obs['observation']:
            aux.append(column[i].tolist())

        new_format.append(aux)

    return new_format

def min_max_agent(root, depth, agent):
    '''
    Maximizar ou minimizar lucro
    '''

    if(depth == 0):
        # print(root.board, calculate_static_value(root.id, root.board), depth)
        return calculate_static_value(agent, root.board) , root

    if(agent == 'player_1'):
        max_value = -float('inf')
        max_child = root

        # Cria filhos do nó:
        root.create_children()

        for child in root.children :
            value , child = min_max_agent(child, depth-1, 'player_2')
            # print(child.board, value, depth)

            if(value > max_value):
                max_value = value
                max_child = child

        # print(f'MOVE MAX: {child.id_move}')
        # print(max_child.board, max_value, depth)
        return max_value , max_child

    else:
        min_value = float('inf')
        min_child = root

        # Cria filhos do nó:
        root.create_children()

        for child in root.children :
            value , child = min_max_agent(child, depth-1, 'player_1')
            # print(child.board, value, depth)

            if(value < min_value):
                min_value = value
                min_child = child

        # print(f'MOVE MIN: {child.id_move}')
        # print(min_child.board, min_value, depth)
        return min_value , min_child

def my_agent(agent , mask):
    x = int(input("Por favor, digite sua jogada: "))
    return x