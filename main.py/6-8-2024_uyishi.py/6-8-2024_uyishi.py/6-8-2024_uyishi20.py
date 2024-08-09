import os
os.system("cls")

matn = input("gapni kiriting : ")

lst = matn.split()

sozlar = []
count = []

for i in range(len(lst)):
    sozlar.append(lst[i])
    count.append(lst.count(lst[i]))

max = count[0]
maxindex = 0

for i in range(len(count)):
    if max < count[i]:
        max = count[i]
        maxindex = i
print(f"eng ko'p takrorlangan so'z -> \"{sozlar[maxindex]}\" <- {max} marta")