class UstKolvo:
    #kolvo = None
    def __init__(self, kolvo = None):
        self.kolvo = kolvo

    def set_kolvo(self, kolvo):
        if kolvo >= 1 and kolvo <= 10 and isinstance(kolvo, int):
            self.kolvo = kolvo
        else:
            self.kolvo = 1

    def get_kolvo(self):
        return self.kolvo

if __name__ == "__main__":
    k = UstKolvo()
    k.set_kolvo(-4)
    kk = k.get_kolvo()
    print(kk)
