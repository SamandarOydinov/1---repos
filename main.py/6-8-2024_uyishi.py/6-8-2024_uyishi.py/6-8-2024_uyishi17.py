import os
os.system("cls")

dct = {
    1: 'b',
    2: 'a',
    3: 'c',
    4: 'd',
    6: 'e',
    5: 'f',
    7: 'g',
    8: 'h',
    9: 'i'
}
key = list(dct.keys())
value = list(dct.values())

for i in range(len(value)):
    for j in range(i + 1,len(value)):
        if value[i] < value[j]:
            value[i], value[j] = value[j], value[i]

print(value)