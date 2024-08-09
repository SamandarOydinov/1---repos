import os 
os .system("cls")

son = input("son kiriting : ")

length = len(son)
son = int(son)
natija = []
i = 1
while son != 0:
    if son % 10 == 1:
        natija.append('bir')
    if son % 10 == 2:
        natija.append('ikki')
    if son % 10 == 3:
        natija.append('uch')
    if son % 10 == 4:
        natija.append("to'rt")
    if son % 10 == 5:
        natija.append('besh')
    if son % 10 == 6:
        natija.append('olti')
    if son % 10 == 7:
        natija.append('yetti')
    if son % 10 == 8:
        natija.append('sakkiz')
    if son % 10 == 9:
        natija.append("to'qqiz")
    son //= 10
    i += 1
    if son and i == 2:
        if son % 10 == 1:
            natija.append("o'n")
        if son % 10 == 2:
            natija.append('yigirma')
        if son % 10 == 3:
            natija.append("o'ttiz")
        if son % 10 == 4:
            natija.append("qirq")
        if son % 10 == 5:
            natija.append('ellik')
        if son % 10 == 6:
            natija.append('oltmish')
        if son % 10 == 7:
            natija.append('yetmish')
        if son % 10 == 8:
            natija.append('sakson')
        if son % 10 == 9:
            natija.append("to'qson")
        son //= 10
    if i == 3:
        natija.append("yuz")
    if i == 4:
        natija.append("ming")
    if i == 5:
        if son:
            if son % 10 == 1:
                natija.append("o'n")
            if son % 10 == 2:
                natija.append('yigirma')
            if son % 10 == 3:
                natija.append("o'ttiz")
            if son % 10 == 4:
                natija.append("qirq")
            if son % 10 == 5:
                natija.append('ellik')
            if son % 10 == 6:
                natija.append('oltmish')
            if son % 10 == 7:
                natija.append('yetmish')
            if son % 10 == 8:
                natija.append('sakson')
            if son % 10 == 9:
                natija.append("to'qson")
            son //= 10
        natija.append("ming")
print(natija)
a = []
for i in range(length - 2):
    a.append(natija[length - 2 * i:length - 2 * (i - 1)])
a.append(natija[1:2])
a.append(natija[:1])
print(a)