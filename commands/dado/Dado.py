from random import randint, choice
from .utils.number_into_emote import turn_into_emote, turn_into_special_emote
from .utils.emotes_and_gifs_settings import critical_error_number, dice_gif, critical_success_gifs, critical_error_gifs

class Dado:
    def __init__(self, context, sides):
        self._name = context.author.display_name
        self._sides = sides
        self._rolled_number = None
        self._error = None
        self.gif = None

    def roll(self):
        try:
            self._sides = int(self._sides)
            between_one_and_ten_thousand = self._check_sides()
            if(between_one_and_ten_thousand):
                self._rolled_number = self._get_random_number()
            else:
                self._error = 'Somente números inteiros entre 1 e 10001 são aceitos'   
        except:
            self._error = 'Somente números inteiros são aceitos'

        finally:
            return self._handle_response()

    def _handle_response(self):
        if self._error:
            response_message = self._error

        elif self._rolled_number == self._sides:
            response_message = turn_into_special_emote(self._rolled_number)
            self.gif = choice(critical_success_gifs)

        elif self._rolled_number == 1:
            response_message = critical_error_number
            self.gif = choice(critical_error_gifs)
        
        else:
            response_message = turn_into_emote(self._rolled_number)

        return f'{self._name}: {response_message} {dice_gif}'

    def _check_sides(self):
        if(self._sides <= 1 or self._sides > 10000):
            return False
        return True

    def _get_random_number(self):  
        return randint(1, self._sides)
        
