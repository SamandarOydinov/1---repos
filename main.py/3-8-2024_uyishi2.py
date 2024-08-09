import os
import random
os.system("cls")

def func(lst: list):
    lst.sort()
    min2 = lst[1]

    print(lst)
    print("2 - minimal son : ",min2)

lst = []
n = int(input("nechta element : "))

for i in range(n):
    son = random.randint(10,100)
    lst.append(son)

func(lst)