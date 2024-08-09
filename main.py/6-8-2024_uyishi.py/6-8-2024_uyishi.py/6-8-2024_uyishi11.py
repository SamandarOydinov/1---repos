import os,math
os.system("cls")

def func(son):
    return (True if son == 1 else False)

lst = [1,0,1,0,0,1,1,1,0,0,1,0,1,0]

print(lst)
natija = list(map(func,lst))
print(natija)