from utils import *
from minMax import min_max_agent
from node import Node
from display import *

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3

def main(env, option):

    not_finish = True
    action = None

    # Variáveis para loops de jogadas
    n_rounds = 50
    count_rounds = 0
    dic = {'wins': 0 , 'tied': 0 , 'lose': 0}
    
    # Conição de parada:
    stop = False

    while not stop:

        # Loop principal
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

                        print(f"Jogou 1 : {action}\n")

                        # Display:
                        if(option != 3 and option != 4):
                            player_move('SMART MACHINE' , action)

                    else:

                        if(option == 1):
                            action = play_random_agent(env,agent,observation['action_mask']) 
                            player_move('RANDOM MACHINE', action)
                        elif(option == 2):
                            action = my_agent(agent,observation['action_mask']) 
                        else:
                            # Loop de jogadas
                            if(option == 3):   # Random
                                action = play_random_agent(env,agent,observation['action_mask'])
                            elif(option == 4): # Smart
                                # Variaveis do nó
                                depth = 1
                                board = change_observation_format(observation)
                                root = Node(agent, board , observation['action_mask'], action)
                                
                                # Ação por mim-max
                                value , child = min_max_agent(root, depth, agent)
                                action = child.id_move


                                print(f"Jogou 2 : {action}\n")

                    env.step(action)
        
        # Jogando apenas 1 vez:
        if (option == 1 or option == 2): 

            if(env.rewards['player_1'] > env.rewards['player_2']):
                end_screen('SMART MACHINE', 'WIN')
            elif(env.rewards['player_1'] == env.rewards['player_2']):
                end_screen('TIED', 'GAME')
            else:
                print(" A maquina não perde, nem vou escrever essa possibilidade :)")

            stop= True
            break

        else:
            # Jogando 20 vezes:
            count_rounds+=1

            # Somatorio de vitorias, empates e derrotas
            if(env.rewards['player_1'] > env.rewards['player_2']):
                dic['wins']+=1
            elif(env.rewards['player_1'] == env.rewards['player_2']):
                dic['tied']+=1
            else:
                dic['lose']+=1
        
            if(count_rounds < n_rounds):
                not_finish = True
                action = None

                # Cria ambiente:
                env = tictactoe_v3.env()
                env.reset()

            else:
                stop= True
                show_scores(dic)

                break

if __name__ == '__main__': 

    # Função principal
    option  = init_game_screen()
    
    # Cria ambiente:
    if(option == 1  or option == 2):
        
        start_game()
        infos_board()

        env = tictactoe_v3.env(render_mode='human')
        env.reset()
    else:
        env = tictactoe_v3.env()
        env.reset()

    main(env , option)
