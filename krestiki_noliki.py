
def f_fut(x, l):
    o2 = False
    while not o2:
        try:
            x = int(x)
            if x >= 1 and x <= 9:
                x = int(x)
                o2 = True
            else:
                o2 = False
                x = input(f'игрок {l}:')
        except:
            o2 = False
            x = input(f'игрок {l}:')
    return o2, x

def f_shablon ():
    p = [0,0,0,0,0,0,0,0,0,0]
    return p

def f_shfaq_fushen (p):
    fush1 = []
    fush2 = [' ⁰ ', ' ¹ ', ' ² ', ' ³ ', ' ⁴ ', ' ⁵ ', ' ⁶ ', ' ⁷ ', ' ⁸ ', ' ⁹ ']
    j = 0
    for i in p:
        if i == 4:
            fush1.append(' Ｏ ')
        elif i == 1:
            fush1.append(' Ｘ ')
        else:
            n = fush2[j]
            fush1.append(n)
        j += 1

    fusha = f"-------------\n¦{fush1[1]}¦{fush1[2]}¦{fush1[3]}¦\n-------------\n¦{fush1[4]}¦{fush1[5]}¦{fush1[6]}¦\n-------------\n¦{fush1[7]}¦{fush1[8]}¦{fush1[9]}¦\n-------------"
    return fusha

def bej_hap(p, x, l):
    o = False
    while not o:
        if l == 1:
            m = 1
        else:
            m = 4
        if not p[x]:
            p[x] = m
            fusha = f_shfaq_fushen(p)
            print(fusha)
            o = True
        else:
            print('ячейка занята')
            fusha = f_shfaq_fushen(p)
            print(fusha)
            x = input(f'игрок {l}:')
            o2, x = f_fut(x, l)
            o = False
    return o, p

def f_fitorja (p):
    z = False
    if sum(p[1:4]) == 3 or sum(p[4:7]) == 3:
        z = True
    elif sum(p[1:4]) == 12 or sum(p[4:7]) == 12:
        z = True
    elif p[1] + p[5] + p[9] == 3 or p[3] + p[5] + p[7] == 3:
        z = True
    elif p[1] + p[5] + p[9] == 12 or p[3] + p[5] + p[7] == 12:
        z = True
    for j in range(1,4):
        x = 0
        for i in range(0, 9, 3):
            x += p[j + i]
        if x ==3 or x == 12:
            z = True
    return z

def lojra():
    p = f_shablon ()
    fusha = f_shfaq_fushen(p)
    print(fusha)
    print('введите числа от 1 до 9:')
    z = f_fitorja(p)
    shag = 1
    l = 1
    while True and not z and shag < 10:
        x = input(f'игрок {l}:')
        o2, x = f_fut(x, l)
        o, p = (bej_hap(p, x, l))
        z = f_fitorja(p)
        if z:
            fusha = f_shfaq_fushen(p)
            print(fusha)
            print('победа')
            break
        z = f_fitorja(p)
        if l ==1:
            l = 2
        else:
            l = 1
        shag += 1
        if shag == 10 and not z:
            print(fusha)
            print('ничья')

lojra()

