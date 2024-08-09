import os,math,random
os.system("cls")
# n = int(input("n = "))

def func(son):
    return isinstance(son,str)

lst = ["Salom Samandar",12.3,15,23,"assalomu alaykum ",34.6,"ALLA",8.6,"IT mutahasis",5,24]
print(">>>>>>LIST elemenrlari")
print(lst)

natija = list(filter(func,lst))
print(">>>>>>LIST string elemenrlari")
print(natija)