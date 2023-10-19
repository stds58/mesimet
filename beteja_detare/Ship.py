
class Ship:
    dlina_min = 1
    dlina_max = 3
    def __init__(self, dlina = None, koordX = None, koordY = None, napravlenie = None, oshibka = False):
        self.dlina = dlina
        self.koordX = koordX
        self.koordY = koordY
        self.napravlenie = napravlenie
        self.oshibka = oshibka
        self.korabl = []
        self.oblast = []

    def set_param(self, dlina, koordX, koordY, napravlenie):
        self.dlina = dlina
        self.koordX = koordX
        self.koordY = koordY
        self.napravlenie = napravlenie

    def get_ship(self):
        return self.korabl

    def set_ship(self):
        self.korabl = []
        if self.dlina < self.dlina_min or self.dlina > self.dlina_max:
            self.oshibka = f'допустимая длина от {self.dlina_min} до {self.dlina_max}'

        if self.napravlenie not in ['В', 'П', 'Н', 'Л']:
            self.oshibka = f'допустимое направление {self.napravlenie}'

        for i in range(self.dlina):
            L = []
            if self.napravlenie == 'В':
                L.append(self.koordX - i)
                L.append(self.koordY)
                self.korabl.append(L)
            elif self.napravlenie == 'П':
                L.append(self.koordX)
                L.append(self.koordY + i)
                self.korabl.append(L)
            elif self.napravlenie == 'Н':
                L.append(self.koordX + i)
                L.append(self.koordY)
                self.korabl.append(L)
            elif self.napravlenie == 'Л':
                L.append(self.koordX)
                L.append(self.koordY - i)
                self.korabl.append(L)

    def set_oblast(self, L):
        self.oblast = []
        L_shablon = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        #self.oblast = []
        for i in L:
            for j in L_shablon:
                a = i[0] + j[0]
                b = i[1] + j[1]
                if [a, b] not in self.oblast and a >= 0 and b >= 0:
                    self.oblast.append([a, b])

    def get_oblast(self):
        return self.oblast

    # def del_shqip(self):
    #     self.korabl = []

# from Doska import Doska
# pl1 = Doska(6)
# print(pl1)
# #print(pl1.doska)
# #print('--------------')
# #print(pl1.storona)
# b = Ship()
# b.set_param(3, 0, 4, 'В')
# b.set_ship()
# print(b.get_ship())
# for i in b.get_ship():
#     pl1.doska[i[0]][i[1]] = ' ■ '
#
# b.set_oblast(b.get_ship())
# #print(b.get_oblast())
#
# test = Doska(6)
# for i in b.get_oblast():
#     try:
#         test.doska[i[0]][i[1]] = ' ■ '
#     except IndexError as e:
#         zaglushka = True
# #----------
# b = Ship()
# b.set_param(3, 5, 5, 'В')
# b.set_ship()
# for i in b.get_ship():
#     pl1.doska[i[0]][i[1]] = ' ■ '
# b.set_oblast(b.get_ship())
# for i in b.get_oblast():
#     try:
#         test.doska[i[0]][i[1]] = ' ■ '
#     except IndexError as e:
#         zaglushka = True
# #---------
# #print(pl1.doska)
# print(pl1)
# print('------------')
# print(test.doska)
# print(test)
#print(b.oshibka)
# pl1.set_proverka_cell(5, 5)
# print(pl1.get_proverka_cell())
# print(pl1.get_proverka_oshibka())
# # print(pl1.get_proverka_cell())
# print(pl1)

