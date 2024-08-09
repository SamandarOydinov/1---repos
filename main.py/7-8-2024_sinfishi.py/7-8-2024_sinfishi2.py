from os import system
from json import dumps
system("cls")

file = open('languages.txt',"r",encoding='UTF8')
towns = []
town = file.read().split('\n')
for shahar in town:
    shahar = shahar.split(',')
    MALUMOT = {
        "name": shahar[0],
        "population": int(shahar[1]),
        "millat": shahar[2]
    }
    towns.append(MALUMOT)


for i in towns:
    if i['population'] > 1000000:
        print(dumps(i, indent = 2))

# print(dumps(towns, indent = 2))

file.close()