import os,math
os.system("cls")

def func(son):
    if isinstance(son,int):
        return float(son)
    if isinstance(son,float):
        return int(son)

lst = [12.3,15,23,34.6,8.6,5,24]

print(lst)
natija = list(map(func,lst))
print(natija)