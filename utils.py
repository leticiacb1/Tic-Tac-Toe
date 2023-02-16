from copy import deepcopy
import numpy as np

def create_new_board(board , move):
        
        new_board = deepcopy(board)
        
        if(move in [0,3,6]):
            new_board[0][move // 3] = [1,0]
        elif(move in [1,4,7]):
            new_board[1][move // 3] = [1,0]
        else:
            new_board[2][move //3] = [1,0]
        
        return new_board

def calculate_static_value(agent , board):
    '''
    Retorna pontos adquiridos na atual configuração do tabuleiro
    '''

    #             -------- PONTUAÇÕES --------
    # 100 pontos:
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
        factor = 1
    else:
        factor = -1

    me = [1,0]
    adversary = [0,1]
    points = 0
     
    for board_line in board:
        event_me = board_line.count(me)
        event_adversary = board_line.count(adversary)

        if(event_adversary == 3):
            points += factor*(-1)*100             
        elif(event_adversary == 2):
            if(event_me == 0):
                points += factor*(-1)*10           
            else:
                points += factor*(-1)             
        elif(event_adversary == 1):
            points += factor*(-1)                     
        
        elif(event_me == 3):
            points += factor*100              
        elif(event_me == 2):
            if(event_adversary == 0):
                points += factor*10     
            else:
                points += factor

        elif(event_me == 1):
            points += factor                  

    
    # Casos 'me' ou 'adversary' na coluna
    column_format = [[board[0][0] , board[1][0] , board[2][0]] , 
                    [board[0][1] , board[1][1] , board[2][1]] ,
                    [board[0][2] , board[1][2] , board[2][2]] ,]

    for board_column in board:
        event_me = board_column.count(me)
        event_adversary = board_column.count(adversary)

        if(event_adversary == 3):
            points += factor*(-1)*100           
        elif(event_adversary == 2):           
            if(event_me == 0):                
                points += factor*(-1)*10
            else:
                points += factor*(-1)
        elif(event_adversary == 1):
            points += factor*(-1)              
                                              
        elif(event_me == 3):                  
            points += factor*100             
        elif(event_me == 2):                  
            if (event_adversary == 0):        
                points += factor*10           
            else:
                points += factor
        
        elif(event_me == 1):                  
            points += factor                  
                                                      
    # Casos 'me' ou 'adversary' na diagonal
    diagonal_format = [ [board[0][0] , board[1][1] , board[2][2]] , [board[0][2] , board[1][1] , board[2][0]]]

    for diagonal in diagonal_format:
        event_me = diagonal.count(me)
        event_adversary = diagonal.count(adversary)

        if(event_adversary == 3):
            points += factor*(-1)*100         
        elif(event_adversary == 2):           
            if(event_me == 0):                
                points += factor*(-1)*10          
            else:
                points += factor*(-1)                
        elif(event_adversary == 1):
            points += factor*(-1)             
                                              
        elif(event_me == 3):                  
            points += factor*100             
        elif(event_me == 2):                  
            if(event_adversary == 0):
                points += factor*10
            else:                          
                points += factor
        elif(event_me == 1):                 
            points += factor    
    
    print(f'\n >> PONTOS: {points}\n ')

    return points  

def change_observation_format(obs):
    new_format = []
    for i in range(0,3):
        aux = []
        for position in obs['observation'][i]:
            aux.append(position.tolist())
        
        new_format.append(aux)
    
    return new_format
        
def min_max_agent(root):
    '''
    Maximizar ou minimizar lucro
    '''

    if(root.depth == 0):
        return calculate_static_value(root.id, root.board)

    # Cria filhos do nó:
    root.create_children()

    if(root.id == 'player_1'):
        max_value = np.NINF
        print(f"acoes = {root.possible_moves}")
        print(f"--- FILHOS  : {len(root.children)}---")
        for child in root.children :

            print("---- BOARD:")
            print(child.board)

            value = min_max_agent(child)
            max_value = max(max_value, value)
        
        return max_value
    
    else:
        min_value = np.Inf
        print("--- FILHOS  ---")
        for child in root.children :
            print(child.board)

            value = min_max_agent(child)
            min_value = min(min_value, value)
    
        return min_value