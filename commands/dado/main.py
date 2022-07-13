from random import randint

def check_sides(sides):
    response = {
    'is_ok': False,
    'error': ''
    }

    if(sides <= 1 or sides > 10000):
        response['error'] = 'O número precisa ser maior que 1 e menor que 10001'
    else:
        response['is_ok'] = True
    return response

def format_message(rolled_number):
    if(rolled_number)

def roll_dice(message = None):
    try:
        sides = int(message)
        check = check_sides(sides)
        if(check['is_ok']):
            return randint(1, sides)
        return check['error']
    except:
        return 'Somente números são aceitos'
