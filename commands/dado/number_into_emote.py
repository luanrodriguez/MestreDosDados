special_emotes_dic = {
    '0': '<a:zerobonito:997148111816380558>',
    '1': '<a:umbonito:997148137338712084>',
    '2': '<a:doisbonito:997148113951273062>',
    '3': '<a:tresbonito:997148135065407548>',
    '4': '<a:quatrobonito:997148132469112872>',
    '5': '<a:cincobonito:997148129772183603>',
    '6': '<a:seisbonito:997148125183623178>',
    '7': '<a:setebonito:997148122042089522>',
    '8': '<a:oitobonito:997148119852646430>',
    '9': '<a:novebonito:997148116887277568>'
}

emotes_dic = {
    '0': '<:zerofade:997198636242968596>',
    '1': '<:umfade:997198116304461874>',
    '2': '<:doisfade:997198114421231716>',
    '3': '<:tresfade:997198646779072593>',
    '4': '<:quatrofade:997198644400902236>',
    '5': '<:cincofade:997198641263558707>',
    '6': '<:seisfade:997198642953846784>',
    '7': '<:setefade:997198640261124197>',
    '8': '<:oitofade:997198638893781134>',
    '9': '<:novefade:997198637681619034>'
}


def turn_into_emote(numbers):
    phrase = ''
    for number in str(numbers):
        phrase += emotes_dic[number]
    return phrase

def turn_into_special_emote(numbers):
    phrase = ''
    for number in str(numbers):
        phrase += special_emotes_dic[number]
    return phrase

