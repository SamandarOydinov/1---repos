import os
os.system("cls")

def isprime(son: int):
    for i in range(2,son//2 + 1):
        if son % i == 0:
            return False
    return True

def func(son: int):
    if(son > 1):
        func(son - 1)
        if isprime(son):
            print(son)

func(12)