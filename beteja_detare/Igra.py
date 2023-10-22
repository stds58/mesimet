

from Doska import Doska

class Igra:
    def __init__(self):
        self.imja = self.proces

    def proverka_int(self, tekst, x_min, x_max):
        x = input(tekst)
        while True:
            try:
                a = int(x)
                if a >= x_min and a <= x_max:
                    return int(x)
                else:
                    x = input(f'значение должно быть от {x_min} до {x_max} \n{tekst}:')
            except ValueError as e:
                x = input(tekst)
            if not ValueError:
                break


    def proces(self):
        self.imja = input('введите ваше имя:')
        storona = self.proverka_int('введите ширину доски:', 6, 20)
        pl1 = Doska(storona)
        pl1.igrok_rasstanovka()
        #pl1.auto_rasstanovka()
        print(pl1)
        print(pl1.status)
        print('-------------')
        auto = True
        pl2 = Doska(storona, auto)
        pl2.auto_rasstanovka()
        #print(pl2)
        print(pl2.status)
        print('-------------')

        while len(pl1.spisok_ship) and len(pl2.spisok_ship):
            #print(pl2)
            print(f'ходит {self.imja}')
            print(f'доска {self.imja}\n{pl1}')
            print(f'доска противника\n{pl2}')
            if len(pl1.spisok_ship) and len(pl2.spisok_ship):
                pl2.hod()
            else:
                print(f'победил {self.imja}') if not len(pl2.spisok_ship) else print(f'победил комп')
                break

            if len(pl1.spisok_ship) and len(pl2.spisok_ship):
                #print(pl1)
                print(f'ходит комп')
                auto = True
                pl1.hod(auto)
            else:
                print(f'победил {self.imja}') if not len(pl2.spisok_ship) else print(f'победил комп')
                break
        # print(pl1)
        # print('----------')
        # print(pl2)

igra = Igra()
igra.proces()
