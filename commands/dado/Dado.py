from random import randint
from .utils.number_into_emote import turn_into_emote, turn_into_special_emote
from .utils.emotes_and_gifs_settings import critical_error_number, dice_gif

class Dado:
    def __init__(self, context, sides_received):
        self.name = context.author.display_name
        self.sides = sides_received
        self.rolled_number = None
        self.error = None

    def roll(self):
        try:
            self.sides = int(self.sides)
            between_one_and_ten_thousand = self._check_sides()
            if(between_one_and_ten_thousand):
                self.rolled_number = self._get_random_number()
            else:
                self.error = 'Somente números inteiros entre 1 e 10001 são aceitos'   
        except:
            self.error = 'Somente números inteiros são aceitos'

        finally:
            return self._handle_response()

    def _handle_response(self):
        if self.error:
            response_message = self.error

        elif self.rolled_number == self.sides:
            response_message = turn_into_special_emote(self.rolled_number)

        elif self.rolled_number == 1:
            response_message = critical_error_number
        
        else:
            response_message = turn_into_emote(self.rolled_number)

        return f'{self.name}: {response_message} {dice_gif}'

    def _check_sides(self):
        if(self.sides <= 1 or self.sides > 10000):
            return False
        return True

    def _get_random_number(self):  
        return randint(1, self.sides)
        
