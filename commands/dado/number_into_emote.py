from .emotes_and_gifs_settings import number_emotes, critical_sucess_number_emotes

def turn_into_emote(numbers):
    phrase = ''
    for number in str(numbers):
        phrase += number_emotes[number]
    return phrase

def turn_into_special_emote(numbers):
    phrase = ''
    for number in str(numbers):
        phrase += critical_sucess_number_emotes[number]
    return phrase

