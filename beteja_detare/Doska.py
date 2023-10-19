
class Doska:
    storona_min = 4
    storona_max = 20
    def __init__(self, storona = None, oshibka_proverka = False):
        self.storona = storona
        self.doska = self.set_doska
        self.oshibka = self.get_oshibka
        self.cell = self.get_proverka_cell
        self.oshibka_proverka = oshibka_proverka

    #обработка ошибок
    @property
    def get_oshibka(self):
        if not isinstance(self.storona, int):
            self.oshibka = f'ошибка: сторона должна быть целым числом от {self.storona_min} до {self.storona_max}'
        else:
            if self.storona < self.storona_min or self.storona > self.storona_max:
                self.oshibka = f'ошибка: сторона должна быть от {self.storona_min} до {self.storona_max}'
            else:
                self.oshibka = False
        return self.oshibka

    #сделать доску
    @property
    def set_doska(self):
        if not self.get_oshibka:
            d = range(1, self.storona + 1)
            self.doska = [[' О ' for i in d] for j in d]
        else:
            self.doska = []
        return self.doska

    #показать доску в удобном виде
    def __str__(self):
        if not self.get_oshibka:
            stroka = ' |'+'|'.join([f' {i} ' for i in range(1,self.storona+1)])+'|\n'
            stroka = stroka + '\n'.join([f"{ii}|{'|'.join(i)}|" for i,ii in zip(self.doska,range(1,self.storona+1))])
            #return '\n'.join([f"{ii}|{'|'.join(i)}|" for i,ii in zip(self.doska,range(1,self.storona+1))])
            return stroka
        else:
            return self.get_oshibka

    #проверить входит ли значение в диапазон доски и получить значение клетки
    def set_proverka_cell(self, x, y):
        try:
            self.cell = self.doska[x][y]
        except IndexError as e:
            self.oshibka_proverka = True  #'либо доска пустая либо координаты за гранью доски'
        else:
            self.oshibka_proverka = False

    def get_proverka_cell(self):
        return self.cell

    def get_proverka_oshibka(self):
        return self.oshibka_proverka



#IndexError

# pl1 = Doska(6)
# print(pl1.doska[1][3])
# pl1.set_proverka_cell([[3,4],[1,4],[2,4]])
# print( pl1.get_proverka_cell() )
# #x = input('ввести значение:')
# x = 5
# y = 2
# if x-1 >= 0 and x-1 < pl1.storona and y-1 >= 0 and y-1 < pl1.storona:
#     pl1.doska[x-1][y-1] = ' ■ '
# print(pl1)
# print('--------------')
#print(pl1.storona)




