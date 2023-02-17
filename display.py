import os

def init_game_screen():

    print("\n     ------------------------------------")
    print("     -------- TIC TAC TOE GAME ----------")
    print("     ------------------------------------\n")    

    print("                |       |       ")
    print("            O   |   X   |   -   ")
    print("          ______|_______|_______")
    print("                |       |       ")
    print("            -   |   X   |   -   ")
    print("          ______|_______|_______")
    print("                |       |       ")
    print("            -   |   O   |   O   ")
    print("                |       |       \n")

    print(" \n    > Choose a game option :  \n")
    print("    1 - Smart Machine (X)  vs  Random Machine (O)\n")
    print("    2 - Smart Machine (X)  vs  Human (O)\n")


    option = int(input("    > [1 or 2] ? \t"))
    os.system('clear')

    return option

def start_game():
    print("\n     ------------------------------------")
    print("     --------- STARTING THE GAME --------")
    print("     ------------------------------------\n") 

    print(" \n    > Board positionsn :  \n")

    print("             |   |   ")
    print("           0 | 3 | 6 ")
    print("          ___|___|___")
    print("             |   |   ")
    print("           1 | 4 | 7 ")
    print("          ___|___|___")
    print("             |   |   ")
    print("           2 | 5 | 8 ")
    print("             |   |   ")
   
def player_move(name , position):

    print("\n     ------------------------------------")
    print(f"             {name} TURN ")
    print("     ------------------------------------\n") 

    
    print(f" \n    > Choose position :  {position}\n")

def end_screen(name , situacao):
    
    print("\n     ------------------------------------")
    print(f"               {name} : {situacao} ")
    print("     ------------------------------------\n") 
    
    print("\n                  THE END !             ")
