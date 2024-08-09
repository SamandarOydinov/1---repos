import os
import random
os.system("cls")

def sortlash(lst: list):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lst = []
n = int(input("nechta element : "))

for i in range(n):
    son = random.randint(10,100)
    lst.append(son)

natija = sortlash(lst)

print(natija)