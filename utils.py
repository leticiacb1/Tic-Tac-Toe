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

def change_observation_format(obs):
    new_format = []
    for i in range(3):
        aux = []
        for column in obs['observation']:
            aux.append(column[i].tolist())

        new_format.append(aux)

    return new_format

def play_random_agent(env, agent, mask):
    x = env.action_space(agent).sample()
    while mask[x] != 1:
        x = env.action_space(agent).sample()
    return x

def my_agent(agent , mask):

    print("\n     ------------------------------------")
    print(f"             YOUR TURN ")
    print("     ------------------------------------\n") 
    
    x = int(input(" \n    > Choose position :  "))
    
    return x