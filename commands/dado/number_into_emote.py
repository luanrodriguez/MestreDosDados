emotes_dic = {
    '0': ':zero:',
    '1': ':one:',
    '2': ':two:',
    '3': ':three:',
    '4': ':four:',
    '5': ':five:',
    '6': ':six:',
    '7': ':seven:',
    '8': ':eight:',
    '9': ':nine:'
}


def turn_into_emote(numbers):
    phrase = ''
    for number in str(numbers):
        phrase += emotes_dic[number]
    return phrase
