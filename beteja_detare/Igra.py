from Static_Class import StaticClass
import random
from Doska import Doska
from Ship import Ship


def f_proverka_int(tekst, x_min, x_max):
    x = input(tekst)
    while True:
        try:
            a = int(x)
            if a >= x_min and a <= x_max:
                return int(x)
            else:
                x = input(f'значение должно быть от {x_min} до {x_max} \n{tekst}')
        except ValueError as e:
            x = input(tekst)
        if not ValueError:
            break


def f_proverka_abc(tekst):
    x = input(tekst)
    while x not in ['В', 'П', 'Н', 'Л', 'З']:
        x = input(f'значение должно быть В верх, П право, Н низ, Л лево, З начать всё заново:')
    return x


def f_proverka_ship(obj, ship):
    status = True
    for i in ship.get_ship():
        if i[0] >= 0 and i[1]>=0:
            obj.set_proverka_cell(i[0], i[1])
            if obj.get_proverka_oshibka() and status:
                status = False  # если клетка за гранью доски
        else:
            status = False  # клетка за гранью доски
    return status


def f_zapisat_ship(obj, ship):
    for i in ship.get_ship():
        obj.doska[i[0]][i[1]] = ' ■ '


def f_udalit_ship(obj, ship):
    for i in ship.get_ship():
        try:
            obj.doska[i[0]][i[1]] = ' О '
        except IndexError as e:
            print()


def rand_koord(L_rand_istoria, shag, kolvo_ship):
    L = []
    #удалить занятые ячейки
    for i1, i2 in zip(L_rand_istoria, range( shag )):
        for j1, j2 in zip(i1, range( shag )):
            if j1 == ' ■ ':
                L_rand_istoria[i2].pop(j2)
    #создать список доступных координат
    for i1, i2 in zip(L_rand_istoria, range( shag )):
        for j1, j2 in zip(i1, range( shag )):
            if j1 == ' О ':
                L.append([i2, j2])
    #print('L----',len(L))
    #print(L_rand_istoria)
    if len(L):
        if kolvo_ship[3] > 0:
            dlina = 3
        elif kolvo_ship[2] > 0:
            dlina = 2
        else:
            dlina = 1

        nomer = random.randrange(0, len(L), 1)
        x = L[nomer][0]
        y = L[nomer][1]
        L_rand_istoria[x].pop(y)
        napravlenie = random.choice(['В', 'П', 'Н', 'Л'])
    else:
        dlina = -1
        x = -1
        y = -1
        napravlenie = 'З'

    #print('len(L_rand_istoria)',len(L_rand_istoria), L_rand_istoria)
    return dlina, x, y, napravlenie


def f_proverka_oblast_ship(obj, ship):
    ship.set_oblast(ship.get_ship())
    status = True
    for i in ship.get_oblast():
        obj.set_proverka_cell(i[0], i[1])
        if not obj.get_proverka_oshibka() and obj.get_proverka_cell() != ' О ' and status:
            #print('get_proverka_cell ',i,obj.get_proverka_cell())
            status = False  # за доску не вышло и ячейка занята
    return status


def f_sdelat_dosku():
    status = True
    while status:
        x = f_proverka_int('ширина доски:', 4, 20)
        doska = Doska(x)
        status = doska.oshibka
    return doska

def f_L_rand_istoria(obj):
    L_rand_istoria = []
    for i in obj.doska:
        L_temp = []
        for j in i:
            L_temp.append(j)
        L_rand_istoria.append(L_temp)
    return L_rand_istoria

def f_sdelat_korabl(kto, obj, ship, kolvo_ship):
    shag = 1
    L_rand_istoria = f_L_rand_istoria(obj)
    status = True
    while status:
        if kto == 'bot' and shag <= 1000:
            dlina, x, y, napravlenie = rand_koord(L_rand_istoria, obj.storona, kolvo_ship )
        elif kto == 'bot' and shag > 1000:
            kolvo_ship[0] = 0
            # L_rand_istoria = f_L_rand_istoria(obj)
            # napravlenie = 'З'
            # status = False
            break
        else:
            dlina = f_proverka_int('длина корабля:', 1, 3)
            x = f_proverka_int('x по вертикали:', 1, obj.storona) - 1
            y = f_proverka_int('y по горизонтали:', 1, obj.storona) - 1
            napravlenie = f_proverka_abc('введите В верх, П право, Н низ, Л лево, З начать всё заново:')
        if napravlenie == 'З':
            # kolvo_ship[0] = 0
            # status = False
            break

        ship.set_param(dlina, x, y, napravlenie)
        ship.set_ship()
        #print(f_proverka_ship(obj, ship), f_proverka_oblast_ship(obj, ship))
        if f_proverka_ship(obj, ship) and f_proverka_oblast_ship(obj, ship) and kolvo_ship[ship.dlina] > 0:
            f_zapisat_ship(obj, ship)
            kolvo_ship[ship.dlina] -= 1
            if kto != 'bot':
                print('shag', shag)
                print(obj)
            status = False
            break
        else:
            shag += 1
            if kto != 'bot':
                print('shag', shag)
                print('koord', dlina, x, y, napravlenie)
                print(f'\nкорабль неверно поставлен')
                print('доступно: ')
                print(f'3клетки:{kolvo_ship[3]}шт,')
                print(f'2клетки:{kolvo_ship[2]}шт,')
                print(f'1клетка:{kolvo_ship[1]}шт,')
                print(obj)
            #ship.del_shqip()
        if shag > 1000:
            status = False
        # if not status:
        #     break
    return kolvo_ship


def f_postavit_vse_korabli(kto, obj):
    #[1 установка кораблей 0 заново всё упереустановить,4 одинарных,2 двойных,1 тройной]
    kolvo_ship = [1, 4, 2, 1]
    while True:
        ship1 = Ship()
        kolvo_ship = f_sdelat_korabl(kto, obj, ship1, kolvo_ship)
        ship2 = Ship()
        kolvo_ship = f_sdelat_korabl(kto, obj, ship2, kolvo_ship)
        ship3 = Ship()
        kolvo_ship = f_sdelat_korabl(kto, obj, ship3, kolvo_ship)
        ship4 = Ship()
        kolvo_ship = f_sdelat_korabl(kto, obj, ship4, kolvo_ship)
        ship5 = Ship()
        kolvo_ship = f_sdelat_korabl(kto, obj, ship5, kolvo_ship)
        ship6 = Ship()
        kolvo_ship = f_sdelat_korabl(kto, obj, ship6, kolvo_ship)
        ship7 = Ship()
        kolvo_ship = f_sdelat_korabl(kto, obj, ship7, kolvo_ship)
        #print('kolvo_ship', kolvo_ship)
        #print(obj)
        #print('---------')
        if kolvo_ship == [1, 0, 0, 0]:
            status = 0
            return status
            break
        else:
            f_udalit_ship(obj, ship1)
            f_udalit_ship(obj, ship2)
            f_udalit_ship(obj, ship3)
            f_udalit_ship(obj, ship4)
            f_udalit_ship(obj, ship5)
            f_udalit_ship(obj, ship6)
            f_udalit_ship(obj, ship7)
            kolvo_ship = [1, 4, 2, 1]

    status = kolvo_ship[0]
    return status

#kto = ['bot', 'igrok']
def f_rasstanovka ():
    status = 1
    while status:
        pl1 = f_sdelat_dosku()
        print(pl1)
        status = f_postavit_vse_korabli('igrok', pl1)
        print('-----------')
        print(pl1)

    status = 1
    while status:
        pl2 = Doska(pl1.storona)
        print(pl2)
        status = f_postavit_vse_korabli('bot', pl2)
        print('-----------')
        print(pl2)


f_rasstanovka ()

# obj = f_sdelat_dosku()
# print(obj)
# print('1------------')
# kto = 'bot'
# kolvo_ship = [1, 4, 2, 1]
# ship1 = Ship()
# kolvo_ship = f_sdelat_korabl(kto, obj, ship1, kolvo_ship)
# print(obj)
# print('2------------')
# ship2 = Ship()
# kolvo_ship = f_sdelat_korabl(kto, obj, ship2, kolvo_ship)
# print(obj)
# print('3------------')
# ship3 = Ship()
# kolvo_ship = f_sdelat_korabl(kto, obj, ship3, kolvo_ship)
# print(obj)
# print('4------------')
# ship4 = Ship()
# kolvo_ship = f_sdelat_korabl(kto, obj, ship4, kolvo_ship)
# print(obj)
# print('5------------')
# ship5 = Ship()
# kolvo_ship = f_sdelat_korabl(kto, obj, ship5, kolvo_ship)
# print(obj)
# print('6------------')
# ship6 = Ship()
# kolvo_ship = f_sdelat_korabl(kto, obj, ship6, kolvo_ship)
# print(obj)
# print('7------------')
# ship7 = Ship()
# kolvo_ship = f_sdelat_korabl(kto, obj, ship7, kolvo_ship)
# print(obj)
# print('------------')

# pl1 = f_sdelat_dosku()
# print(pl1)
# f_postavit_vse_korabli(pl1)






#dlina, x, y, napravlenie, error = f_sdelat_korabl(pl1)
#print(dlina, x, y, napravlenie, error)
# print('----------------------')
#print(pl1)


# ship = Ship(3, 3, 1, 'В')
# ship.set_ship()
# pl1.set_proverka_cell(ship.get_ship())
# print( pl1.get_proverka_cell() )

# b.set_oblast(b.get_ship())
# print(b.get_oblast())


#--------------------------------------------------------------------
#pl1 = Doska(6)
#print(pl1)
#print(pl1.oshibka)
#print('--------------')

# b = Ship(3, 3, 1, 'В')
# b.set_ship()
# pl1.set_proverka_cell(b.get_ship())
# print( pl1.get_proverka_cell() )

#  | 1 | 2 | 3 | 4 | 5 | 6 |
# 1| О | О | О | ■ | О | ■ |
# 2| О | ■ | О | О | О | О |
# 3| О | ■ | О | ■ | О | ■ |
# 4| О | ■ | О | О | О | О |
# 5| О | О | О | О | О | О |
# 6| ■ | ■ | О | ■ | ■ | О |


