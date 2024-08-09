import os,random
os.system("cls")

lst = []

for i in range(random.randint(4,8)):
    son = random.randint(1,10)
    lst.append(son)
max = lst[0]
print(lst)
for i in range(len(lst)):
    if max < lst[i]:
        max = lst[i]
for i in range(len(lst)):
    lst[i] = max
print(lst)