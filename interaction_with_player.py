"""
module that contains functions to interact with user
""" 
import random

def start_intro():
    '''
    Prints out the intro of the game.
    '''
    print("Today u r having very important test , Let's start.")

def user_num():
    user_number = -1
    while user_number <=0 and isinstance(user_number,int):
        try:
            user_number = int(input())
            if user_number<=0:
                print("Enter positive number:")
        except ValueError:
            print("This number is not int type, Please input correct number")
        
    return user_number

def form_num(grid):
    number_types = ['ulam', 'prime', 'happy']
    num_type = random.choice(number_types)
    print(f'Please, choose the {num_type} number from the following:\n{grid}')
    return num_type
