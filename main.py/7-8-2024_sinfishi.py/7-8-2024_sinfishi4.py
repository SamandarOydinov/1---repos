import os,json
os.system("cls")

file = open("product.txt",'r')
malumot = []
for i in file.read().split("\n"):
    i = i.split(',')
    user = {

        "id": i[0],
        "kod": i[1],
        "material": i[2],
        "price": i[3],
        "Bor": i[4]

    }
    malumot.append(user)

print(json.dumps(malumot, indent = 2))


file.close()