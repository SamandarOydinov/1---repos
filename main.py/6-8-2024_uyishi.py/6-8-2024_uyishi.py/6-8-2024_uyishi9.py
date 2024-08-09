import os,math,random
os.system("cls")
# n = int(input("n = "))

def func(son):
    return son > 0

lst = []
for i in range(random.randint(5,10)):
    son = random.randint(-100,100)
    lst.append(son)
print(lst)

natija = list(filter(func,lst))
print(">>>>>>LIST MUSBAT elemenrlari")
print(natija)