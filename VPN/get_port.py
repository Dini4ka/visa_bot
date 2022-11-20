import random


def get_port():
    switch = random.randint(0, 2)
    result = dict(login='iharmikhailovich1341', password='e8c14a')
    with open('../settings/ports.txt') as f:
        ip_and_port = f.readlines(0)[switch].split('@')[1].split(':')
        ip = ip_and_port[0]
        port = ip_and_port[1][:-1]
        result.update({('ip', ip), ('port', port)})
        f.close()
    return result


def get_all_ports():
    result = []
    with open('../settings/ports.txt') as f:
        for line in f:
            a = dict(login='iharmikhailovich1341', password='e8c14a')
            ip_and_port = line.split('@')[1].split(':')
            ip = ip_and_port[0]
            port = ip_and_port[1][:-1]
            a.update({('ip', ip), ('port', port)})
            result.append(a)
        f.close()
    return result


