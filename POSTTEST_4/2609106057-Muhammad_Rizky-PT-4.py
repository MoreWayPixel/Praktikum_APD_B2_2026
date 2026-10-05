percobaan = 0
login_berhasil = False

while percobaan < 3:
    Nama = input("Masukan Nama Anda : ").strip().lower()
    NIM =  input("Masukan NIM Anda : ").strip()

    if Nama == "rizky":
        if NIM == "57":
            print("========================================")
            print("           LOGIN BERHASIL")
            print("========================================")
            print("        Selamat datang,", Nama)

            login_berhasil = True
            break

        else:
            print("========================================")
            print("             LOGIN GAGAL")
            print("========================================")
            print("              NIM Salah")
    else:
        if NIM == "57":
            print("========================================")
            print("             LOGIN GAGAL")
            print("========================================")
            print("             Nama Salah")
        else:
            print("========================================")
            print("             LOGIN GAGAL")
            print("========================================")
            print("          Nama dan NIM Salah")

    percobaan += 1
    print("Percobaan tersisa :", 3 - percobaan)
    print()

if login_berhasil == False:

    print("========================================")
    print("      BATAS PERCOBAAN LOGIN HABIS, ANDA DI BLOKIR!!!     ")
    print("========================================")
    print("Program dihentikan.")

else:

    while True:

        print("========================================")
        print("           Menu Distribusi")
        print("========================================")
        print("1. Paket Reguler             - 1 porsi makanan")
        print("2. Paket Anak                - 1 porsi makanan")
        print("3. Paket Keluarga            - 4 porsi makanan")
        print("4. Keluar dari program")
        print("========================================")

        pilihan = int(input("Silahkan Pilih Menu [Masukan angka dari 1-4 sesuai menu yang tersedia]: "))

        if pilihan == 1:
            nama_paket = "Paket Reguler"
            porsi_paket = 1

        elif pilihan == 2:
            nama_paket = "Paket Anak"
            porsi_paket = 1

        elif pilihan == 3:
            nama_paket = "Paket Keluarga"
            porsi_paket = 4

        elif pilihan == 4:
            print("========================================")
            print("       KELUAR DARI PROGRAM")
            print("========================================")
            break

        else:
            print("========================================")
            print("          OPSI TIDAK VALID")
            print("========================================")
            print("Silakan pilih menu dari nomor 1 sampai 4.")
            continue

        jumlah_paket = int(input("Masukkan jumlah paket yang akan dibagikan: "))

        total_porsi = 0

        for i in range(jumlah_paket):
            total_porsi = total_porsi + porsi_paket
            penerima_manfaat = total_porsi

        if total_porsi >= 20:
            bonus = "5 paket buah"

        elif total_porsi >= 10:
            bonus = "3 botol susu"

        elif total_porsi >= 5:
            bonus = "1 paket vitamin"

        else:
            bonus = "Tidak mendapat bonus"

        print("========================================")
        print("            HASIL DISTRIBUSI")
        print("========================================")
        print("Jenis Paket        :", nama_paket)
        print("Jumlah Paket       :", jumlah_paket)
        print("Total Porsi        :", total_porsi, "porsi")
        print("Penerima Manfaat   :", penerima_manfaat, "orang")
        print("Bonus              :", bonus)
        print("========================================")