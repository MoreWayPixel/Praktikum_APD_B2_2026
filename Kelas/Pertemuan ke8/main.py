# #abs() - Nilai absolut
# angka = -20
# angka_absolute = abs(angka)
# print(angka_absolute)

# #divmod() - Mengembalikan tuple (hasil_bagi, sisa_bagi)
# bilangan = divmod(10,3)
# print(bilangan)

# #max() - menampilkan nilai tertinggi
# #min() - menampilkan nilai terendah

# #pow() - Pangkat (dengan opsi modulus)
# bilangan = pow(2,4)
# print(bilangan)

# #round() - pembulatan angka
# #sum() - Penjumlahan iterable

# #enumerate() – Memberi indeks pada iterable
# for index, value in enumerate(["a","b","c","d","e"], start=1):
#     print(f"{index}. {value}")

# #reversed() – Membalik urutan iterable
# data = [12,34,13,67,90,100]
# data_reversed = list(reversed(data))
# print(data_reversed)\

# #sorted() – Mengurutkan iterable
# data_sorted = list(sorted(data))
# print(data_sorted)

# #Fungsi Lingkungan (Environment)
# #globals() dan locals()
# a= "dua puluh"
# def fungsi_sembarang():
#     a = 10
#     b = "Rizky"
#     c = True
    
#     print(globals()['a'])
#     print(locals()['a'])
#     print(locals())
    
# fungsi_sembarang()

# #replace() – Mengganti substring dengan substring lain
# kalimat = "Apip suka belajar python"

# kalimat_diubah = kalimat.replace("python","kalkulus")
# print(kalimat_diubah)

# #find() – Menemukan posisi pertama substring (-1 jika tidak ada)
# print(kalimat.find('belajar'))

# #startswith() – Mengecek apakah string diawali substring tertentu
# print(kalimat.startswith('A'))

# #endswith() – Mengecek apakah string diakhiri substring tertentu
# print(kalimat.endswith('n'))

##Built-in Library
# import math

# print(math.sqrt(144))

##cara lain
# from math import sqrt

# print(sqrt(144))

# #datetime
# from datetime import datetime
# print(datetime.now())

# #calendar
# import calendar as kalender
# print(kalender.calendar(2026))

# #random
# import random

# print(random.randint(1,100))

# buah = ["pisang", "rambutan", "manggis"]
# print(random.choice(buah))

# kartu = ["As Wajik", "3 Hati", "7 Sekop"]
# random.shuffle(kartu)
# print(kartu)

#web untuk mencari library - pypi.org