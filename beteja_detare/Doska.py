
from random import randint
from Ship import Ship

class Doska():
    def __init__(self, storona, auto = False):
        self.storona = storona
        self.doska = self.set_doska
        self.status = self.ustanovit_korabl
        self.kolvo_ship = [1, 4, 2, 1]
        self.spisok_ship = []
        self.spisok_obvodka = []
        self.auto = auto


    #сделать доску
    @property
    def set_doska(self):
        d = range(1, self.storona + 1)
        self.doska = [[' О ' for i in d] for j in d]
        return self.doska


    def set_doska_dublazh(self, obj_doska):
        self.doska_dublazh = []  # дубляж доски из которой убираем занятые клетки и клетки которые уже перебрали для расстановки
        for i in obj_doska:
            L_temp = []
            for j in i:
                L_temp.append(j)
            self.doska_dublazh.append(L_temp)
        self.len_doska = len(obj_doska)
        # удалить занятые ячейки
        for i1, i2 in zip(self.doska_dublazh, range(self.len_doska)):
            for j1, j2 in zip(i1, range(self.len_doska)):
                if j1 == ' ■ ':
                    self.doska_dublazh[i2].pop(j2)
        return self.doska_dublazh

    #показать доску в удобном виде
    def __str__(self):
        doska_tuman = []
        for i1, i2 in zip(self.doska, range(self.storona)):
            L2 = []
            for j1, j2 in zip(i1, range(self.storona)):
                if j1 == ' ■ ':
                    L2.append(' О ')
                else:
                    L2.append(j1)
            doska_tuman.append(L2)
        if self.auto:
            stroka = '  |' + '|'.join([f'{i:02} ' for i in range(1, self.storona + 1)]) + '|\n'
            self.stroka = stroka + '\n'.join(
                [f"{ii:02}|{'|'.join(i)}|" for i, ii in zip(doska_tuman, range(1, self.storona + 1))])
        else:
            stroka = '  |' + '|'.join([f'{i:02} ' for i in range(1, self.storona + 1)]) + '|\n'
            self.stroka = stroka + '\n'.join(
                [f"{ii:02}|{'|'.join(i)}|" for i, ii in zip(self.doska, range(1, self.storona + 1))])
        return self.stroka


    # обводка подбитого корабля
    def obvodka_korabla(self):
        # установить область вокруг кораблей
        self.spisok_obvodka = []
        L_shablon = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        for obj_ship in self.spisok_ship:
            L = []
            for i in obj_ship.korabl:
                for j in L_shablon:
                    a = i[0] + j[0]
                    b = i[1] + j[1]
                    if [a, b] not in L and a >= 0 and b >= 0 and a < self.storona and b < self.storona:
                        L.append([a, b])
            # добавить обводку
            for j in obj_ship.korabl:
                for i in L:
                    if i == j:
                        L.remove(j)
            self.spisok_obvodka.append(L)


    #проверка корабля
    def ustanovit_korabl(self, obj_ship):
        #obj_ship = b.korabl [[4, 2], [3, 2], [2, 2]]
        self.status = False
        # проверить корабль
        while not self.status:
            for i in obj_ship:
                if i[0] < 0 or i[0] >= self.storona or i[1] < 0 or i[1] >= self.storona:
                    self.status = "клетка за гранью доски"
            break
        # установить область вокруг корабля
        self.oblast = []
        L_shablon = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in obj_ship:
            for j in L_shablon:
                a = i[0] + j[0]
                b = i[1] + j[1]
                if [a, b] not in self.oblast and a >= 0 and b >= 0 and a < self.storona and b < self.storona:
                    self.oblast.append([a, b])
        # проверить область корабля
        for i in self.oblast:
            if self.doska[i[0]][i[1]] == ' ■ ':
                self.status = 'клетка занята'
                break
        # проверить количество кораблей
        if not self.status:
            dlina = len(obj_ship)
            if not self.kolvo_ship[dlina]:
                self.status = 'корабль такой длины  больше уже нельзя поставить'
        # запись допустимого корабля
        if not self.status:
            for i in obj_ship:
                self.doska[i[0]][i[1]] = ' ■ '
            self.kolvo_ship[dlina] -= 1
        # подсчёт кораблей
        if not self.status:
            sum = 0
            for i in range(1, len(self.kolvo_ship)):
                sum = sum + self.kolvo_ship[i]
                # print(sum)
            if not sum:
                self.kolvo_ship[0] = 0
                self.status = 'все корабли расставлены'
        return self.status


    def proverka_int(self, tekst, x_min, x_max):
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

    def proverka_abc(self, tekst):
        x = input(tekst)
        while x not in ['В', 'П', 'Н', 'Л', 'З']:
            x = input(f'значение должно быть В верх, П право, Н низ, Л лево, З начать всё заново:')
        return x

    def vvod_klaviatura(self):
        # ввести координаты
        dlina = self.proverka_int('длина корабля:', 1, 3)
        x = self.proverka_int('x по вертикали:', 1, self.storona)
        y = self.proverka_int('y по горизонтали:', 1, self.storona)
        napravlenie = self.proverka_abc('введите В верх, П право, Н низ, Л лево, З начать всё заново:')
        return dlina, x, y, napravlenie

    def igrok_rasstanovka(self):
        while True:
            x = self.vvod_klaviatura()
            if x[3] in ['В', 'П', 'Н', 'Л']:
                b = Ship(x[0],x[1],x[2],x[3])
                self.ustanovit_korabl(b.korabl)
                print(self.__str__())
                if self.status:
                    print(self.status)
                if self.status:
                    print('self.kolvo_ship', self.kolvo_ship)
                    print(self.__str__())
                if self.status == 'все корабли расставлены':
                    break


    def auto_rasstanovka(self):
        self.status = 'начало'
        doska_dubl = self.set_doska_dublazh(self.doska)
        i = 1
        while self.status:
            b = Ship(0, 0, 0, '')
            self.x = b.rand_ship(self.doska, doska_dubl, self.kolvo_ship)
            b = Ship(self.x[0], self.x[1], self.x[2], self.x[3])
            self.ustanovit_korabl(b.korabl)
            if not self.status:
                self.spisok_ship.append(b)
            if self.status == 'все корабли расставлены':
                self.spisok_ship.append(b)
                self.obvodka_korabla()
                break
            i += 1
            if i > self.storona**2 and self.kolvo_ship[0] == 1:
                self.spisok_ship = []
                self.kolvo_ship = [1, 4, 2, 1]
                self.doska = self.set_doska
                doska_dubl = self.set_doska_dublazh(self.doska)
                self.status = 'начало'
                i = 1
            elif i <= self.storona**2 and self.kolvo_ship[0] == 1:
                self.status = 'начало'

    # ход одного игрока
    def hod(self, auto = False):
        while len(self.spisok_ship):
            if auto:
                x, y = self.autohod()
            else:
                print('буквой X помечаются подбитые корабли, буквой T — промахи')
                x = self.proverka_int('введите координаты клетки.х по вертикали:', 1, self.storona) - 1
                y = self.proverka_int('введите координаты клетки.у по горизонтали:', 1, self.storona) - 1
            if self.doska[x][y] == ' ■ ':
                self.doska[x][y] = ' X '
                l = self.spisok_ship
                for i, j in zip(l, range(len(l))):  # взять корабль из списка [[2, 2], [2, 3], [2, 4]]
                    l_ship = self.spisok_ship[j].korabl
                    for ii, jj in zip(l_ship, range(len(l_ship))):  # взять координаты корабля [2, 2]
                        if [x, y] == ii:
                            self.spisok_ship[j].korabl.pop(jj)
                            if not self.spisok_ship[j].korabl:
                                self.spisok_ship.pop(j)
                                for i in self.spisok_obvodka[j]: #обвести подбитый корабль
                                    self.doska[ i[0] ][ i[1] ] = ' T '
                                self.spisok_obvodka.pop(j)
                                print(self.__str__())
                                print('подбит')
                            else:
                                print(self.__str__())
                                print('ранен')
            elif self.doska[x][y] == ' T ' or self.doska[x][y] == ' X ':
                print(self.__str__())
                print('сюда уже стреляли. повторите заново\n')
            else:
                self.doska[x][y] = ' T '
                print('промах\n')
                break
            #print(obj)
            #print('-------------')
            # print(pl2.spisok_ship[0].korabl)
            # print(pl2.spisok_ship[1].korabl)
            # print(pl2.spisok_ship[2].korabl)
            # print(pl2.spisok_ship[3].korabl)
            # print(pl2.spisok_ship[4].korabl)
            # print(pl2.spisok_ship[5].korabl)
            # print(pl2.spisok_ship[6].korabl)

    # ход компа
    def autohod(self):
        L = []
        # создать список доступных координат
        for i1, i2 in zip(self.doska, range(self.storona)):
            for j1, j2 in zip(i1, range(self.storona)):
                if j1 == ' О ' or j1 == ' ■ ':
                    L.append([i2, j2])
        i = randint(0, len(L)-1)
        x = L[i][0]
        y = L[i][1]
        return x, y
