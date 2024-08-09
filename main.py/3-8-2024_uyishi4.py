import os
import random
os.system("cls")
def func(lst: list):
    element = []
    index = []
    for i in range(len(lst)):
        natija = lst.count(lst[i])
        if lst[i] not in element:
            element.append(lst[i])
            index.append(natija)

    max = index[0]
    maxindex = 0
    for i in range(len(index)):
        if index[i] > max:
            max = index[i]
            maxindex = i

    for i in range(len(element)):
        print(element[i]," - > ",index[i]," marta")
    print("eng kop takrorlangan son : ",element[maxindex])

lst = []
n = int(input("nechta element : "))

for i in range(n):
    son = random.randint(10,100)
    lst.append(son)
print(lst)

func(lst)