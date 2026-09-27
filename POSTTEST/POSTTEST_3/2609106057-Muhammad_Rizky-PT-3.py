Nama = input("Masukan Nama Anda : ").strip()
NIM =  input("Masukan NIM Anda : ").strip()

if Nama == "Rizky":
    if NIM == "057":
        print("========================================")
        print("           LOGIN BERHASIL")
        print("========================================")
        print("        Selamat datang,", Nama)

        reward_dasar = 1000
        
        print("========================================")
        print("           PILIHAN MISI")
        print("========================================")
        print("1. Misi Standar              - Bonus 2%")
        print("2. Misi Sulit                - Bonus 5%")
        print("3. Misi Kritis               - Bonus 8%")
        print("4. Misi Penyelamatan Bumi    - Bonus 12%")

        pilihan = int(input("Silahkan Pilih Misi [Masukan angka dari 1-4 sesuai misi yg tersedia]: "))

        if pilihan == 1:
            nama_misi = "Misi Standar"
            persentase_bonus = 0.02

        elif pilihan == 2:
            nama_misi = "Misi Sulit"
            persentase_bonus = 0.05

        elif pilihan == 3:
            nama_misi = "Misi Kritis"
            persentase_bonus = 0.08

        elif pilihan == 4:
            nama_misi = "Misi Penyelamatan Bumi"
            persentase_bonus = 0.12

        else:
            print("\n========================================")
            print("       PILIHAN MISI TIDAK TERSEDIA")
            print("========================================")
            print("Silakan pilih misi dari nomor 1 sampai 4.")

        # ============== PERHITUNGAN ==============
        if pilihan >= 1 and pilihan <= 4:
            reward_bonus = int(reward_dasar * persentase_bonus)
            reward_akhir = int(reward_dasar + reward_bonus)

            print("\n========================================")
            print("            HASIL MISI")
            print("========================================")
            print("Nama Misi       :", nama_misi)
            print("Reward Dasar    :", reward_dasar, "poin")
            print("Bonus           :", reward_bonus, "poin")
            print("Reward Akhir    :", reward_akhir, "poin")
            print("========================================")
    else:
        print("========================================")
        print("             LOGIN GAGAL")
        print("========================================")
        print("              NIM Salah")
else:
    if NIM =="057":
        print("========================================")
        print("             LOGIN GAGAL")
        print("========================================")
        print("             Nama Salah")
    else:
        print("========================================")
        print("             LOGIN GAGAL")
        print("========================================")
        print("          Nama dan NIM Salah")