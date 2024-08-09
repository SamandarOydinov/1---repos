import os
os.system("cls")

lst = [100,210,30210,2501,12001]

for i in range(len(lst)):
    count = 0
    count1 = 0
    x = lst[i]
    while x:
        if x % 10 == 0:
            count1 += 1
        x //= 10
    if count1 >= 2:
        print(lst[i])