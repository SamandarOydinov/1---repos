import os
os.system("cls")

matn = ("salom mening ismim Eshmat dunyo noutbuk ustiga qurilmagan")
print(matn)
matn = matn.lower()
lst = matn.split()
taqiq = ["salom","eshmat","toshmat","dunyo","noutbuk"]

for i in range(len(lst)):
    for j in range(len(taqiq)):
        if lst[i] == taqiq[j]:
            lst[i] = '*****'
for i in range(len(lst)):
    print(lst[i],end = " ")