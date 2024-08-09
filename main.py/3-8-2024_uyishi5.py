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

    min = index[0]
    minindex = 0
    for i in range(len(index)):
        if index[i] < min:
            min = index[i]
            minindex = i

    for i in range(len(element)):
        print(element[i]," - > ",index[i]," marta")
    print("eng kam takrorlangan son : ",element[minindex])
lst = [1,2,2,3,1,3,3,1,5,5,5]
print(lst)
func(lst)
