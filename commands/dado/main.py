from random import randint, choice
from .number_into_emote import turn_into_emote, turn_into_special_emote
from .emotes_and_gifs_settings import critical_success_gifs, critical_error_gifs, critical_error_number

def dice_handler(message = None):
    try:
        sides = int(message)
        between_one_and_ten_thousand = check_sides(sides)
        if(between_one_and_ten_thousand):
            response = []
            rolled_number = roll_dice(sides)
            if(rolled_number == sides):
                response.append(turn_into_special_emote(rolled_number))
                response.append(choice(critical_success_gifs))
            elif(rolled_number == 1):
                response.append(critical_error_number)
                response.append(choice(critical_error_gifs))
            else:
                response.append(turn_into_emote(rolled_number))
            
            return response
        return ['Somente números inteiros entre 1 e 10001']
    except:
        return ['Somente números inteiros são aceitos']

def check_sides(sides):
    if(sides <= 1 or sides > 10000):
        return False
    return True

def roll_dice(sides):  
    return randint(1, sides)
    
