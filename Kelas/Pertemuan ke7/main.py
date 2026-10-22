# def sapa():
#     print("Haloo Rizky")
    
# sapa()

# #Fungsi Tanpa Parameter
# def hitung():
#     return 5 * 3

# print(hitung())

# #Fungsi dengan Parameter
# def persegi(sisi): #parameter
#     hasil = sisi*sisi
#     return hasil

# print(persegi(5)) #argumen

# #default parameter
# def sapa(nama="Kansa"): 
#     return f"halo {nama}"

# print(sapa("Sartika"))

# def menu():
#     print("1. Create")
#     print("1. Read")
#     print("1. Update")
#     print("1. Delete")
    
#     pilihan = input("Pilih Menu: ")

# #Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"

# #Membuat variabel lokal
# def data():
#     nama = "Alfi"
#     prodi = "Kedokteran Lanjut"
    
#     print("Nama:", nama)
#     print("Prodi:", prodi)
    
# data()

# def sapa():
#     print("Haloo Rizky")

# sapa()

# #Fungsi Rekursif
# def faktorial(n):
# #Base Case: Kondisi fungsi berhenti
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * faktorial(n - 1)

# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4! {hasil_faktorial}")

#Program Menggunakan Fungsi
#Variabel global untuk menyimpan data buku
buku = []

# #Fungsi untuk menampilkan data buku
# def lihat_buku():
#     if len(buku) == 0:
#         print("Belum ada data buku")
#     else:
#         print("ID Buku | Judul Buku")
#     for indeks in range(len(buku)):
#         print(indeks, "|", buku[indeks])
        
# #Fungsi untuk menambah data
# def tambah_buku():
#     buku_baru = input("Judul Buku: ")   
#     buku.append(buku_baru)
#     print("Buku berhasil ditambahkan!")
    
# #Fungsi untuk mengedit data
# def edit_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku_baru = input("Judul baru: ")
#         buku[indeks] = buku_baru
#         print("Buku berhasil diupdate!")
        
# def hapus_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Film: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku.remove(buku[indeks])
#         print("Buku berhasil dihapus!")
        
# def tampilkan_menu():
#     print("\n")
#     print("========= MENU =========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")
#     menu = input("PILIH MENU > ")
#     print("\n")
    
#     if menu == "1":
#         lihat_buku()
#     elif menu == "2":
#         tambah_buku()
#     elif menu == "3":
#         edit_buku()
#     elif menu == "4":
#         hapus_buku()
#     elif menu == "5":
#         exit()
#     else:
#         print("Pilihan tidak valid!")