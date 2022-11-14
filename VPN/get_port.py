import random


def get_port():
    switch = random.randint(1, 3)
    result = dict(login='iharmikhailovich1341', password='e8c14a')
    with open('ports.txt') as f:
        ip = f.readlines(switch)[0].split('@')[1].split(':')[0]
        port = f.readlines(switch)[0].split('@')[1].split(':')[1][:-1]
        result.update({('ip', ip), ('port', port)})
        f.close()
    return result
