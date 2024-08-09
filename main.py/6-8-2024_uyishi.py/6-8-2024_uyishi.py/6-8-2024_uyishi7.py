import os,math,random
os.system("cls")
# n = int(input("n = "))

def func(son):
    for i in range(2,son // 2 + 1):
        if son % i == 0:
            return False
    return True

lst = []
for i in range(random.randint(5,10)):
    son = random.randint(100,1000)
    lst.append(son)
print(lst)

natija = list(filter(func,lst))
print(">>>>>>LIST TUB elemenrlari")
print(natija)