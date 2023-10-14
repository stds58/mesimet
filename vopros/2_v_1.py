
class SdelatPole():
    #pole = None
    def __init__(self, kolvo = None, pole= {}):
        self.kolvo = kolvo
        self.pole = pole

    def set_kolvo(self, kolvo):
        if kolvo >= 1 and kolvo <= 10 and isinstance(kolvo, int):
            self.kolvo = kolvo
        else:
            self.kolvo = 1
    def get_kolvo(self):
        return self.kolvo

    def set_pole(self, kolvo):
        if kolvo >= 1 and kolvo <= 10 and isinstance(kolvo, int):
            storona = range(1, kolvo + 1)
        else:
            storona = range(1, 2)
        pole = {str(i) + str(j): ' О ' for j in storona for i in storona}
        self.pole = pole
    def get_pole(self):
        return self.pole

if __name__ == "__main__":
   k=SdelatPole()
   k.set_kolvo(-4)
   g = k.get_kolvo()
   k.set_pole(g)
   kk = k.get_pole()
   print( kk )
   print(g)
