import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from commands.dado.main import roll_dice, dice_handler
from commands.dado.number_into_emote import turn_into_emote

def test_if_roll_dice_returns_between_1_and_choice():
    choice = 20
    rolled_number = roll_dice(choice)
    assert(rolled_number >= 1 and rolled_number <= choice)

def test_if_turn_into_emote_works():
    assert(turn_into_emote(20) == ':two::zero:')
    assert(turn_into_emote(1) == ':one:')
    assert(turn_into_emote(8) == ':eight:')
    assert(turn_into_emote(118) == ':one::one::eight:')

def test_if_dado_returns_an_error_message_when_sides_are_1_or_below():
    rolled_number_one = dice_handler(1)
    rolled_number_below_one = dice_handler(0)
    assert(rolled_number_below_one == ['Somente números inteiros entre 1 e 10001'])
    assert(rolled_number_one == ['Somente números inteiros entre 1 e 10001'])

def test_if_dado_returns_an_error_message_when_sides_are_above_10000():
    rolled_number = dice_handler(10001)
    assert(rolled_number == ['Somente números inteiros entre 1 e 10001'])

def test_if_dado_returns_an_error_message_when_no_parameter_is_given():
    rolled_number = dice_handler()
    assert(rolled_number == ['Somente números inteiros são aceitos'])

def test_if_dado_returns_an_error_message_when_sides_are_not_numbers():
    rolled_number = dice_handler('foo')
    assert(rolled_number == ['Somente números inteiros são aceitos'])