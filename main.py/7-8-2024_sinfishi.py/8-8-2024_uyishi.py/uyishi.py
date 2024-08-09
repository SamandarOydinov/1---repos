from os import system
from json import dumps

system("cls")
def MENU():
    print("""
    Quyidgailardan birini tanlang : 
    1 : pulim yetadigan bilet narxlari
    2 : kiritilgan davlat bo'yicha barcha avia reyslar
    3 : US ga boruvchi 21:00 dan oldingi barcha avia reyslar
    0 : CHIQISH

    """)

def bilet_narxlari(air):
    qiymat = int(input("pulingiz miqdorini kiriting : "))
    for i in air:
        print(i)


file = open("booking_data.",'r')

natija = file.read().split('\n')

air = []

for i in natija:
    i = i.split(",")
    data = {
        "ID": i[0],
        'departure': i[1],
        'd_time': i[2],
        'arrive': i[3],
        'a_time': i[4],
        'cost': i[5]
    }
    
    air.append(data)

MENU()
choose = int(input("idlardan birini tanlang : "))
while choose != 0:
    if choose == 1:
        bilet_narxlari(air)
    a = int(input("MENU ga qaytish uchun 1 ni kiriting : "))
    if a == 1:
        MENU()
        choose = int(input("idlardan birini tanlang : "))
    else:
        choose = 0
file.close()