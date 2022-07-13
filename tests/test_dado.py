import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from commands.dado.main import roll_dice

def test_if_dado_returns_a_number_between_1_and_choice():
    rolled_number = roll_dice(20)
    assert(rolled_number > 0 and rolled_number <= 20)

def test_if_dado_returns_an_error_message_when_sides_are_1_or_below():
    rolled_number_one = roll_dice(1)
    rolled_number_below_one = roll_dice(0)
    assert(rolled_number_below_one == 'O número precisa ser maior que 1 e menor que 10001')
    assert(rolled_number_one == 'O número precisa ser maior que 1 e menor que 10001')

def test_if_dado_returns_an_error_message_when_sides_are_above_10000():
    rolled_number = roll_dice(10001)
    assert(rolled_number == 'O número precisa ser maior que 1 e menor que 10001')

def test_if_dado_returns_an_error_message_when_no_parameter_is_given():
    rolled_number = roll_dice()
    assert(rolled_number == 'Somente números são aceitos')

def test_if_dado_returns_an_error_message_when_sides_are_not_numbers():
    rolled_number = roll_dice('foo')
    assert(rolled_number == 'Somente números são aceitos')