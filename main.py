#
# Reference: https://pettingzoo.farama.org/environments/classic/tictactoe/
#

import numpy as np
from copy import deepcopy
from utils import *
from random import randint

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3


def make_moves(action_mask):
    list_possible_moves = []
    for position, value in enumerate(action_mask):
        if(value):
            list_possible_moves.append(position)
    return list_possible_moves

def apply_action(possible_actions, position):
    aux_list = deepcopy(possible_actions)
    aux_list[position] = 0
    return aux_list

class Node():
    def __init__(self,id_player, board , action_mask , move):
        
        self.id = id_player                                                                         # Identifica se o nó é do player_1 ou player_2
        self.id_move = move if move != None else randint(0,8)                                       # Posição jogada que resultou nessa configuração de tabuleiro                          
        
        self.board = board                                                                          # Configuração board
        self.action_mask = action_mask
        self.possible_moves = make_moves(action_mask)                                               # Profundidade
        self.children = []

    def create_children(self):
        id = 'player_1' if self.id == 'player_2' else 'player_2'

        for move in self.possible_moves:
            mask = apply_action(self.action_mask, move)
            new_board = create_new_board(self.board , move, id)

            child = Node(id, new_board, mask, move)
            self.children.append(child)

            #print(f"ID DAS CRIANÇAS : {move}")

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
        if termination or truncation:
            not_finish = False 
        else:
            if agent == 'player_1':
                # Variaveis do nó
                depth = 1
                board = change_observation_format(observation)
                root = Node(agent, board , observation['action_mask'], action)
                
                # Ação por mim-max
                value , child = min_max_agent(root, depth, agent)
                action = child.id_move

            else:
                action = play_random_agent(agent,observation['action_mask']) 
            
            print(f'play: ',action)
            env.step(action)

print(env.rewards)