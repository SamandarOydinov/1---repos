import os
os.system("cls")

son1 = int(input("1 - son: "))
son2 = int(input("2 - son: "))
son3 = int(input("3 - son: "))

katta = lambda son1,son2,son3 : son1 if son1 >= son2 and son1 >= son3 else son2 if son2 >= son1 and son2 >= son3 else son3
natija = katta(son1,son2,son3)
print(natija)