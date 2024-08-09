import os
import random
import json
os.system("cls")
def func(dct: dict):
    value = list(dct.values())
    max = value[0]
    for i in range(len(value)):
        if max < value[i]:
            max = value[i]
    print(json.dumps(dct, indent=2))
    print("max value = ",max)
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