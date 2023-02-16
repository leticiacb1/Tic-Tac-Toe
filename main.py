#
# Reference: https://pettingzoo.farama.org/environments/classic/tictactoe/
#

import numpy as np
from copy import deepcopy
from utils import *

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3


class Node():
    def __init__(self,id_player, depth, board , action_mask , move):
        
        self.id = id_player                                                                         # Identifica se o nó é do player_1 ou player_2
        self.father_move = move if move != None else  play_random_agent(id_player, action_mask)    # Caso primeiro movimento                           
        
        self.board = board                                                                          # Configuração board
        self.action_mask = action_mask
        self.possible_moves = self.make_moves(action_mask)
        self.depth = depth                                                                          # Profundidade
        self.children = []

    def create_children(self):
        id = 'player_1' if self.id == 'player_2' else 'player_2'
        depth = self.depth - 1

        for move in self.possible_moves:
            mask = self.apply_action(self.action_mask, move)
            new_board = create_new_board(self.board , move)

            child = Node(id, depth, new_board, mask, self.father_move)
            self.children.append(child)

    def make_moves(self , action_mask):
        list_possible_moves = []
        for position, value in enumerate(action_mask):
            if(value):
                list_possible_moves.append(position)
        return list_possible_moves
    
    def apply_action(self, possible_actions, position):
        aux_list = deepcopy(possible_actions)
        aux_list[position] = 0
        return aux_list

def play_random_agent(agent, mask):
    x = env.action_space(agent).sample()
    while mask[x] != 1:
        x = env.action_space(agent).sample()
    return x


env = tictactoe_v3.env(render_mode='human')
env.reset()

not_finish = True

# Para o primeiro movimento:
action = None

while not_finish:
    for agent in ['player_1','player_2']:
        observation, reward, termination, truncation, info = env.last() 

        print(f'------- AGENTE : {agent}-------')
        print(observation['action_mask'])
        if termination or truncation:
            not_finish = False
        else:
            if agent == 'player_1':
                
                # Variaveis do nó
                init_depth = 2
                board = change_observation_format(observation)
                root = Node(agent, init_depth, board , observation['action_mask'], action)
                
                # Ação por mim-max
                value = min_max_agent(root) 
                print(f'------ {value} -----') 

                action = play_random_agent(agent,observation['action_mask'])     
            
            else:
                
                action = play_random_agent(agent,observation['action_mask']) 
            print(f'play: ',action)
            env.step(action)

print(env.rewards)