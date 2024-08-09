import os
import json
import random
os.system("cls")

def list(lst: list):
    max = -1
    for i in range(len(lst)):
        if not lst[i] % 2:
            if lst[i] > max:
                max = lst[i]
    print("max juft son : ",max)

lst = []
n = int(input("n = "))
for i in range(n):
    son = random.randint(10,100)
    lst.append(son)
print(lst)
list(lst)