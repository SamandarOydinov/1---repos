import os
os.system("cls")
def func(arr) -> int:
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    if len(arr) >= 3:
        for j in range(3,len(arr) + 1):
            if j % 2 == 1:
                for i in range(len(arr) - j + 1):
                    for k in range(j):
                        print(j)
                        sum += arr[k + i]
                        print(sum)

    return sum
arr = [6,9,14,5,3,8,7,12,13,1]
natija = func(arr)
print(natija)