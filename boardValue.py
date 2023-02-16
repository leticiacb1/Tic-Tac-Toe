def calculate_node_value(agent , board):
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

    return points