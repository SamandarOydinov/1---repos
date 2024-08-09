import os
os.system("cls")

while 1:
    a = int(input("to'g'ri to'rtburchakning 1 - tomonini kiriting : "))
    b = int(input("to'g'ri to'rtburchakning 2 - tomonini kiriting : "))
    if a >= 1 and b > 1000:
        break
    else:
        print("iltimos 1 <= (1 - tomon) va (1000 < (2 - tomon)) ko'rinishida kiriting")

P = 2 * (a + b)
S = a * b

if P > S:
    print(f"Perimetri yuzasidan katta Uning perimetri : {P}")
else:
    print(f"Yuzasi perimetridan katta Uning Yuzasi : {S}")