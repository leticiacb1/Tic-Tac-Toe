from utils import *
from random import randint

class Node():
    def __init__(self,id_player, board , action_mask , move):
        
        self.id = id_player                                                     # Identifica se o nó é do player_1 ou player_2
        self.id_move = move if move != None else randint(0,8)                   # Posição jogada que resultou nessa configuração de tabuleiro                          
        
        self.board = board                                                      # Configuração board
        self.action_mask = action_mask
        self.possible_moves = make_moves(action_mask)                           # Profundidade
        self.children = []

    def create_children(self):
        id = 'player_1' if self.id == 'player_2' else 'player_2'

        for move in self.possible_moves:
            mask = apply_action(self.action_mask, move)
            new_board = create_new_board(self.board , move, id)

            child = Node(id, new_board, mask, move)
            self.children.append(child)