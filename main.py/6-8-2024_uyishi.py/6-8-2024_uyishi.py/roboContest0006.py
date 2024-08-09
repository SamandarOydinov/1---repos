import os
# os.system("cls")
yil = 1
while yil:
    yil = int(input("yilni kiriting : "))

    if not (yil % 400 and not yil % 100 or yil % 4):
        print(f"12/09/{yil}")
    else:
        print(f"13/09/{yil}")