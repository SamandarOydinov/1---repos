import os,math,random
os.system("cls")

def func(son):
    if son > 0:
        return -son
    else:
        return son * 2

lst = []
for i in range(random.randint(5,10)):
    son = random.randint(-20,20)
    lst.append(son)
print(lst)
lst = list(map(func,lst))
print(lst)