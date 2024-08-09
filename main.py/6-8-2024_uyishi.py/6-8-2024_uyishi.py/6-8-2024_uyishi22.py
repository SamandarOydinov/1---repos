import os
os.system("cls")

lst = [[9,2,3],[3,10,16],[6,8,1]]
print(lst)
max = lst[0][0]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if max < lst[i][j]:
            max = lst[i][j]

print(max)