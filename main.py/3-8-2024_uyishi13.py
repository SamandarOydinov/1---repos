import os
import json
import random
os.system("cls")

def set(st: set):
    lst = list(st)
    min = lst[0]
    for i in range(len(lst)):
        if min > lst[i]:
            min = lst[i]
    st.clear()
    st.update(lst)
    print(st)
    print(min)

st = {36, 44, 42, 35, 70, 20, 50, 83, 30, 70, 30, 99}
set(st)