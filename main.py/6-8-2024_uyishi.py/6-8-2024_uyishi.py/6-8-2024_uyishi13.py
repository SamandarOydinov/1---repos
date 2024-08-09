import os
os.system("cls")

matn = list("salom Samandar nima gap tinchmi")
matn1 = []
for i in range(len(matn) - 1):
    matn[i] = matn[i].lower()
    if matn[i].isalpha():
        matn1.append(matn[i])

for i in range(len(matn1)):
    for j in range(i + 1,len(matn1) - 1):
        if matn1[i] < matn1[j]:
            matn1[i],matn1[j] = matn1[j],matn1[i]
print(matn1)