
import random

class Ship:
    def __init__(self, dlina, koordX, koordY, napravlenie):
        self.dlina = dlina
        self.koordX = koordX - 1
        self.koordY = koordY - 1
        self.napravlenie = napravlenie
        self.korabl = self.set_ship


    @property
    def set_ship(self):
        self.korabl = []
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
        return self.korabl


    # случайные координаты одной клетки
    def rand_ship(self, obj_doska, obj_doska_dublazh, kolvo_ship):
        self.len_doska = len(obj_doska)
        L = []
        # создать список доступных координат
        for i1, i2 in zip(obj_doska_dublazh, range(self.len_doska)):
            for j1, j2 in zip(i1, range(self.len_doska)):
                if j1 == ' О ':
                    L.append([i2, j2])
        #print('L',L)
        if len(L):
            if kolvo_ship[3] > 0:
                self.dlina = 3
            elif kolvo_ship[2] > 0:
                self.dlina = 2
            else:
                self.dlina = 1

            nomer = random.randrange(0, len(L), 1)
            self.koordX = L[nomer][0]
            self.koordY = L[nomer][1]
            obj_doska_dublazh[self.koordX].pop(self.koordY)
            self.napravlenie = random.choice(['В', 'П', 'Н', 'Л'])
        self.koord = [self.dlina, self.koordX, self.koordY, self.napravlenie]
        return self.koord

