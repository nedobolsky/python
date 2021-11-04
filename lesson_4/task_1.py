from sys import argv


def wage():
    try:
        hours, rate, prize = map(float, argv[1:])
        print(hours * rate + prize)
    except ValueError:
        print('Вы забыли передать 3 аргумента, выработка в часах, ставка в час, премия')


wage()
