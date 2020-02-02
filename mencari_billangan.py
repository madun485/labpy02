##Mencari Bilangan.
#Tugas Latihan Py02

print("Program Mencari Bilangan Terbesar")
print()
bil_1 = int(input("Masukkan Bilangan Ke-1: "))
bil_2 = int(input("Masukkan Bilangan Ke-2: "))
bil_3 = int(input("Masukkan Bilangan Ke-3: "))

if bil_1 > bil_2 and bil_1 > bil_3:
    if bil_2 > bil_3:
        print(bil_1, "Terbesar dan", bil_3, "Terkecil")
    else:
        print(bil_1, "Terbesar dan", bil_2, "Terkecil")
elif bil_2 > bil_1 and bil_2 > bil_3:
    if bil_1 > bil_3:
        print(bil_2, "Terbesar dan", bil_3, "Terkecil")
    else:
        print(bil_2, "Terbesar dan", bil_1, "Terkecil")
else:
    if bil_1 > bil_2:
        print(bil_3, "Terbesar dan", bil_2, "Terkecil")
    else:
        print(bil_3, "Terbesar dan", bil_1, "Terkecil")