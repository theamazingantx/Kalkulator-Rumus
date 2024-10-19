# Header/Judul
print("Selamat datang di program untuk menghitung rumus sederhana")
print("----------------------------------------------------------")
print("Pilih menu\n1. Keliling segitiga\n2. Luas segitiga\n3. Keliling persegi\n4. Luas persegi\n5. Keliling lingkaran\n6. Luas Lingkaran")

# Input User untuk memilih menu
menu = int(input("Pilih menu: "))

# variabel yang paling sering digunakan
phi = 3.14159

# if statment bro

# Jika yg diketik 1, maka akan menjalankan program dibawah ini
if menu == 1:
    print("Anda memilih rumus keliling segitiga!!\n")
    a = int(input("Masukan sisi pertama: "))
    b = int(input("Masukan sisi kedua: "))
    c = int(input("Masukan sisi ketiga: "))

    d = a + b + c

    print("Hasil: ", d)

# JIka yg diketik 2, maka akan menjalankan program dibawah ini
elif menu == 2:
    print("Anda memilih rumus luas segitiga!!\n")
    a = int(input("Masukan alas: "))
    b = int(input("Masukan Tinggi: "))

    c = 1/2 * a * b

    print("Hasil: ", c)


# Jika yg diketik 3, maka akan menjalankan program dibawah ini
elif menu == 3:
    print("Anda memilih rumus keliling persegi!!\n")
    a = int(input("Masukan sisi: "))

    b = 4 * a

    print("Hasil :", b)

# Jika yg diketik 4, maka akan menjalankan program dibawah ini
elif menu == 4:
    print("Anda memilih rumus luas persegi!!\n")
    a = int(input("Masukan sisi: "))

    b = a * a

    print("Hasil :", b)

# Jika yg diketik 5, maka akan menjalankan program dibawah ini
elif menu == 5:
    print("Anda memilih rumus keliling lingkaran!!\n")
    subMenu = int(input("Pilih sub menu: \n1. Pakai jari jari\n2. Pakai diameter\nPilih menu: "))

    if subMenu == 1:
        a = int(input("Masukan jari jari: "))

        b = 2 * phi * a

        print("Hasil: ", b)

    elif subMenu == 2:
        a = int(input("Masukan diameter: "))
        b = phi * a

        print("Hasil: ", b)

    else: print("Liat atas, kira kira ada gak menu", subMenu, "Diatas??")

# Jika yg diketik 6, maka akan menjalankan program dibawah ini
elif menu == 6:
    print("Anda memilih rumus luas lingkaran!!\n")
    subMenu = int(input("Pilih sub menu: \n1. Pakai jari jari\n2. Pakai diameter\nPilih menu: "))

    if subMenu == 1:
        a = int(input("Masukan jari jari: "))

        b = phi * a * a

        print("Hasil: ", b)

    elif subMenu == 2:
        a = int(input("Masukan diameter: "))

        b = (phi * a ** 2) / 4

        print("Hasil: ", b)

    else: print("Liat atas, kira kira ada gak menu", subMenu, "Diatas??")

# Selain angka yang ditentukan, maka akan menjalankan program dibawah ini
else: print("Menu tidak tersedia")