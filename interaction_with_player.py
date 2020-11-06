"""
module that contains functions to interact with user
""" 

from random import sample, choice

def start_intro():
    '''
    Prints out the intro of the game.
    '''
    print("Today u r having very important test , Let's start.")

def lvl_of_difficuly():
    '''
    '''
    lvl = input("Choose the level of difficuly :\nEazy Medium Hard\n")
    if lvl == 'Eazy':
        return (0,20)
    elif lvl == 'Medium':
        return (21,50)
    elif lvl == 'Hard':
        return (51,100)
    else:
        print("Please , input correct level of difficulty:")
        lvl_of_difficuly()
 
def generate_grid(from_num: int, to_num: int) -> list:
    grid = sample([i for i in range(1, 100)], 10)

    return grid
def game_round():
    number_types = ['ulam', 'prime', 'happy']
    num_type = random.choice(number_types)
    spectrum = lvl_of_difficuly()
    grid = generate_grid(spectrum[0],spectrum[1])
    print(f'Please, choose the {num_type} number from the following:\n{grid}')

    



#game_round()
