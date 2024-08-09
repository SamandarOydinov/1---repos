import os
import random
os.system("cls")
def func(lst: list):
    lst.sort()
    max2 = lst[len(lst) - 2]

    print(lst)
    print("2 - maximal son : ",max2)
lst = []
n = int(input("nechta element : "))

for i in range(n):
    son = random.randint(10,100)
    lst.append(son)
max = lst[0]

func(lst)