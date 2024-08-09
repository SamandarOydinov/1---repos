import os
import random
import json
os.system("cls")
def func(dct: dict):
    key = list(dct.keys())
    max = key[0]
    for i in range(len(key)):
        if max < key[i]:
            max = key[i]
    print(json.dumps(dct, indent=2))
    print("max key = ",max)
dct = {

    11: 2,
    25: 12,
    32: 11,
    14: 20,
    51: 15,
    16: 14,
    37: 16,
    68: 19,
    29: 9,
    10: 17

}
func(dct)