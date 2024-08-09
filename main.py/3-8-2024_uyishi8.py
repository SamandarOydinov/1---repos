import os
import random
import json
os.system("cls")
def func(dct: dict):
    key = set(dct.keys())
    value = set(dct.values())
    st = (key)
    st.update(value)
    print(st)
    print(type(st))
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