import os
# os.system("cls")

baho = 1

while baho:

    baho = int(input("bahoni kiriting : "))
    
    if baho < 40:
        if baho < 38:
            print(baho)
        else:
            print(baho + baho % 5 - 1)
        break

    if baho % 5 > 2:
        print(baho + baho % 5 - 1)
    else:
        print(baho)