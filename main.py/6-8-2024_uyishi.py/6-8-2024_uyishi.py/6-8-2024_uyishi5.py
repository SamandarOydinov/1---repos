import os,math,random
os.system("cls")
n = int(input("n = "))

def func(son):
    return son > pow(n,3)

def func1(son):
    return son <= pow(n,3)

lst = []
for i in range(random.randint(5,10)):
    son = random.randint(100,1000)
    lst.append(son)
print(lst)
natija = list(filter(func,lst))
natija1 = list(filter(func1,lst))
print(f">>>> listdagi {n} ning kubidan kattalar")
print(natija)
print(f">>>> listdagi {n} ning kubidan kichiklar")
print(natija1)