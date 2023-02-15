#
# Reference: https://pettingzoo.farama.org/environments/classic/tictactoe/
#

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3

def play_random_agent(agent, obs):
    x = env.action_space(agent).sample()

    print(f'------- AGENTE : {agent}-------')
    print(x)

    while obs['action_mask'][x] != 1:
        x = env.action_space(agent).sample()
    return x

def play_min_max_agent(agent, obs):
    # TODO you must implement your code here
    pass

env = tictactoe_v3.env(render_mode='human')
env.reset()

not_finish = True
while not_finish:
    for agent in ['player_1','player_2']:
        observation, reward, termination, truncation, info = env.last() 
        print("----- OBSERVATION -----")
        print(observation)

        print("----- REWARD -----")
        print(reward)

        print("----- TERMINATION -----")
        print(termination)

        print("----- TRUNCATION -----")
        print(truncation)

        print("----- INFO ------")
        print(info)

        if termination or truncation:
            not_finish = False
        else:
            if agent == 'player_1':
                action = play_random_agent(agent,observation)  # this is where you would insert your policy/algorithm
            else:
                action = play_random_agent(agent,observation) # TODO change
            print(f'play: ',action)
            env.step(action)

print(env.rewards)
