import os,random
os.system("cls")

lst = []
lstmanfiy = []
lstnol = []
for i in range(random.randint(8,10)):
    son = random.randint(-10,10)
    lst.append(son)
print(lst)
length = len(lst)
i = 0

while i < len(lst):
    if lst[i] < 0:
        x = lst[i]
        lstmanfiy.append(x)
        lst.remove(x)
        i -= 1
    if lst[i] == 0:
        y = lst[i]
        lstnol.append(y)
        lst.remove(y)
        i -= 1
    i += 1
for i in range(len(lstmanfiy)):
    lst.append(lstmanfiy[i])
for i in range(len(lst)):
    lstnol.append(lst[i])
print(lstnol)