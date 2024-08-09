import os
import json
os.system("cls")
def func(dct: dict):
    key = list(dct.keys())
    value = list(dct.values())
    # dct1 = {}
    print(json.dumps(dct,indent=2))
    dct.clear()
    for i in range(len(key)):
        dct[value[i]] = key[i]
    print("  ***KEYIN***")
    print(json.dumps(dct, indent=2))   
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