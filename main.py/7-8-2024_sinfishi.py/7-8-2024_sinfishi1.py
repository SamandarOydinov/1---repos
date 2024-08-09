from os import system
from json import dumps
system("cls")

file = open('dars.txt',"r")

user = file.read().split("\n")
users = []
for odam in user:
    odam = odam.split(",")
    # print(odam)
    odamlar = {
        'name': odam[0],
        'surname': odam[1],
        'country': odam[len(odam) - 1]
    }
    users.append(odamlar)
print(dumps(users, indent = 2))
file.close()