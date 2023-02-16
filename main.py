#
# Reference: https://pettingzoo.farama.org/environments/classic/tictactoe/
#

import numpy as np

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3


class Node():
    def __init__(self,id_player, depth,obs):
        
        self.id = id_player                           # Identifica se o nó é do player_1 ou player_2
        self.board = obs['observation']               # Configuração board
        self.possible_actions = obs['action_mask']
        self.depth = depth                            # Profundidade

    def create_children(self, actual_state):
        ...
        
def calculate_static_value(agent , obs):
    '''
    Retorna pontos adquiridos na atual configuração do tabuleiro
    '''

    # ---- PONTUAÇÕES ----
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
    
    # Casos 'me' ou 'adversary' na linha
    board = change_observation_format(obs)   # [ [ [] .. ] , [ [] .. ] , [ [] ..] ]
    
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
        
def play_min_max_agent(agent, obs):
    # TODO you must implement your code here
    ...

def play_random_agent(agent, obs):
    x = env.action_space(agent).sample()
    while obs['action_mask'][x] != 1:
        x = env.action_space(agent).sample()
    return x

env = tictactoe_v3.env(render_mode='human')
env.reset()

not_finish = True
while not_finish:
    for agent in ['player_1','player_2']:
        observation, reward, termination, truncation, info = env.last() 

        print(f'------- AGENTE : {agent}-------')

        if termination or truncation:
            not_finish = False
        else:
            if agent == 'player_1':
                calculate_static_value(agent,observation)
                action = play_random_agent(agent,observation)  # this is where you would insert your policy/algorithm
                
            else:
                calculate_static_value(agent,observation)
                action = play_random_agent(agent,observation) # TODO change
            #print(f'play: ',action)
            env.step(action)

print(env.rewards)
