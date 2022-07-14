from random import randint

def dice_handler(sides):
     

def check_sides(sides):
    if(sides <= 1 or sides > 10000):
        return Falses
    return True

def roll_dice(message = None):
    sides = int(message)
    check = check_sides(sides)
    if(check):
        return randint(1, sides)
    return 'O número precisa ser maior que 1 e menor que 10001'
