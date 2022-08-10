import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from commands.dado.Dado import Dado
from commands.dado.utils.number_into_emote import turn_into_emote, turn_into_special_emote

def test_if_roll_dice_returns_between_1_and_choice():
    choice = 20
    rolled_number = roll_dice(choice)
    assert(rolled_number >= 1 and rolled_number <= choice)

def test_if_turn_into_emote_works():
    assert(turn_into_emote(20) == '<:doisfade:997198114421231716><:zerofade:997198636242968596>')
    assert(turn_into_emote(1) == '<:umfade:997198116304461874>')
    assert(turn_into_emote(8) == '<:oitofade:997198638893781134>')
    assert(turn_into_emote(136) == '<:umfade:997198116304461874><:tresfade:997198646779072593><:seisfade:997198642953846784>')
    assert(turn_into_emote(45) == '<:quatrofade:997198644400902236><:cincofade:997198641263558707>')
    assert(turn_into_emote(97) == '<:novefade:997198637681619034><:setefade:997198640261124197>')

def test_if_turn_into_special_emote_works():
    assert(turn_into_special_emote(20) == '<a:doisbonito:997148113951273062><a:zerobonito:997148111816380558>')
    assert(turn_into_special_emote(1) == '<a:umbonito:997148137338712084>')
    assert(turn_into_special_emote(8) == '<a:oitobonito:997148119852646430>')
    assert(turn_into_special_emote(136) == '<a:umbonito:997148137338712084><a:tresbonito:997148135065407548><a:seisbonito:997148125183623178>')
    assert(turn_into_special_emote(45) == '<a:quatrobonito:997148132469112872><a:cincobonito:997148129772183603>')
    assert(turn_into_special_emote(97) == '<a:novebonito:997148116887277568><a:setebonito:997148122042089522>')

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