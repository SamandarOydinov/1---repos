import os,math,random
os.system("cls")
# n = int(input("n = "))

def func(son):
    return isinstance(son,int)

lst = ["Salom Samandar",12.3,15,23,34.6,8.6,5,24]
print(">>>>>>LIST elemenrlari")
print(lst)

natija = list(filter(func,lst))
print(">>>>>>LIST BUTUN elemenrlari")
print(natija)