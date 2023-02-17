from utils import *
from minMax import min_max_agent
from node import Node
from display import *

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3

def main(env, option):

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

                    # Display:
                    player_move('SMART MACHINE' , action)

                else:

                    if(option == 1):
                        action = play_random_agent(env,agent,observation['action_mask']) 
                        player_move('RANDOM MACHINE', action)
                    else:
                        action = my_agent(agent,observation['action_mask']) 

                env.step(action)
    
    if(env.rewards['player_1'] > env.rewards['player_2']):
        end_screen('SMART MACHINE', 'WIN')
    elif(env.rewards['player_1'] == env.rewards['player_2']):
        end_screen('TIED', 'GAME')
    else:
        print(" A maquina não perde, nem vou escrever essa possibilidade :)")

if __name__ == '__main__': 

    # Cria ambiente:
    env = tictactoe_v3.env(render_mode='human')
    env.reset()

    # Função principal
    option  = init_game_screen()
    start_game()
    main(env , option)
