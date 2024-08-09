import os 
os.system("cls")

dct = {
    'I': 1,
    'V': 5,
    'X': 10
}

rimraqam = input("Rim raqamini kiriting : ")

sum = 0
i = 0

while i < (len(rimraqam)):
    if i < len(rimraqam) and dct[rimraqam[i]] < dct[rimraqam[i + 1]]:
        sum += dct[rimraqam[i + 1]] - dct[rimraqam[i]]
        i += 2
    else:
        sum += dct[rimraqam[i]]
        i += 1
print(sum)