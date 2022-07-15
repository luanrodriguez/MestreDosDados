from random import randint, choice
from .dice_gifs import critical_success, critical_error
from .number_into_emote import turn_into_emote, turn_into_special_emote

def dice_handler(message = None):
    try:
        sides = int(message)
        between_one_and_ten_thousand = check_sides(sides)
        if(between_one_and_ten_thousand):
            response = []
            rolled_number = roll_dice(sides)
            if(rolled_number == sides):
                response.append(turn_into_special_emote(rolled_number))
                response.append(choice(critical_success))
            elif(rolled_number == 1):
                response.append('<:blobum:997205585256796260>')
                response.append(choice(critical_error))
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
    
