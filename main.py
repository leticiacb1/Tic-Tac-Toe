from utils import *
from minMax import min_max_agent
from node import Node

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3

def main(env):

    not_finish = True
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
                    action = play_random_agent(env,agent,observation['action_mask']) 
                
                print(f'play: ',action)
                env.step(action)

    print(env.rewards)

if __name__ == '__main__': 

    # Cria ambiente:
    env = tictactoe_v3.env(render_mode='human')
    env.reset()

    # Função principal
    main(env)
