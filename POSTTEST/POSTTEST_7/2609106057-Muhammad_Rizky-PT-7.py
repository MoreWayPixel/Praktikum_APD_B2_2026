import os 
    
akun = {
    "rizky": {
        "password": "admin123",
        "role": "Admin"
    },
    "buma": {
        "password": "123",
        "role": "Hunter"
    }
}

monster = {
    "M001": {
        "nama": "Great Izuchi",
        "jenis": "Bird Wyvern",
        "elemen": "Tidak ada",
        "habitat": "Shrine Ruins",
        "kelemahan": "Thunder, Ice",
        "ancaman": "Rendah"
    },
    "M002": {
        "nama": "Aknosom",
        "jenis": "Bird Wyvern",
        "elemen": "Api",
        "habitat": "Shrine Ruins",
        "kelemahan": "Water, Thunder",
        "ancaman": "Rendah"
    },
    "M003": {
        "nama": "Arzuros",
        "jenis": "Fanged Beast",
        "elemen": "Tidak ada",
        "habitat": "Shrine Ruins",
        "kelemahan": "Fire",
        "ancaman": "Rendah"
    },
    "M004": {
        "nama": "Tetranadon",
        "jenis": "Amphibian",
        "elemen": "Air",
        "habitat": "Shrine Ruins",
        "kelemahan": "Thunder",
        "ancaman": "Rendah"
    },
    "M005": {
        "nama": "Royal Ludroth",
        "jenis": "Leviathan",
        "elemen": "Air",
        "habitat": "Flooded Forest",
        "kelemahan": "Fire, Thunder",
        "ancaman": "Menengah"
    }
}

pengguna_aktif = ""
role_aktif = ""
jumlah_login_gagal = 0

def cari_monster(id_monster):
    if id_monster in monster:
        return monster[id_monster]
    else:
        return None

def validasi_ancaman(ancaman):
    if ancaman in ["Rendah", "Menengah", "Tinggi"]:
        return True
    else:
        return False

def hitung_monster():
    return len(monster)

def input_id_monster():
    id_masukan = input("Masukkan ID Monster: ").strip().upper()
    return id_masukan

def tampilkan_daftar_monster():
    print("================ DAFTAR MONSTER ================")
    daftar_id = list(monster.keys())
    tampilkan_monster_rekursif(daftar_id)
    print("Jumlah monster:", hitung_monster())

def tampilkan_detail_monster(id_monster):
    data_monster = cari_monster(id_monster)

    if data_monster is not None:
        print("ID Monster       :", id_monster)
        print("Nama Monster     :", data_monster["nama"])
        print("Jenis Monster    :", data_monster["jenis"])
        print("Elemen/Status    :", data_monster["elemen"])
        print("Habitat          :", data_monster["habitat"])
        print("Kelemahan        :", data_monster["kelemahan"])
        print("Tingkat Ancaman  :", data_monster["ancaman"])
    else:
        print("Monster tidak ditemukan!")

def tampilkan_monster_rekursif(daftar_id, indeks=0):
    if indeks >= len(daftar_id):
        return

    id_data = daftar_id[indeks]
    print(id_data, "-", monster[id_data]["nama"])
    tampilkan_monster_rekursif(daftar_id, indeks + 1)


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=========================================================")
    print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡠⣤⣴⣾⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣶⣠⣤⡤⠤⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀
⠀⢀⣠⣼⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠈⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣄⣀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠾⢧⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⣀⣤⣯⣧⠀⠀⣀⡀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡿⠿⠟⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⢰⣿⠃⢿⣯⣵⡿⠿⠿⠆⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡭⡄⠀⠀⠀⠀
⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠸⣿⣧⢸⣿⡹⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⣄⡀⠀⠘⣿⣗⢿⣿⣿⡀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣴⣿⣿⣾⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠀⠀⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⡍⠉⠛⠿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⣤⣀⠀⠀⠀⠀⠀⢁⣴⣿⣿⣿⣿⣿⣟⡿⣿⣿⣿⠄⠀⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠠⣤⣬⣿⣷⠛⠛⠻⣶⣿⣿⢟⣽⣿⣿⣿⣏⠀⢠⣿⣿⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⠿⠿⠿⣻⣿⠉⠉⠀⠀⠈⢿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠒⠯⠿⠖⠀⠀⠀⠀⠘⠛⠙⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("==========================================================")
    print("⚔️  Selamat Datang di Monster Hunter Monster List(MHML)⚔️")
    print("==========================================================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        username = input("Username: ").strip().lower()
        password = input("Password: ").strip()
        
        if username in akun and akun[username]["password"] == password:
            pengguna_aktif = username
            role_aktif = akun[username]["role"]
            role = role_aktif

            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")

            if role == "Hunter":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(r"""                       
                       /\
                      /  \
                      ||||
                      ||||
                      ||||
                     /||||\
                    /______\
                       ||
                       ||
                    """)
                    print("==================================================")
                    print("             ⚔️ MHML - HUNTER MENU ⚔️")
                    print("==================================================")
                    print("Selamat datang", role, username)
                    print("==================================================")
                    print("1. Daftar Monster")
                    print("2. Detail Monster")
                    print("3. Logout")
                    print("==================================================")

                    menu_hunter = input("Pilih menu: ")

                    if menu_hunter == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        tampilkan_daftar_monster()

                    elif menu_hunter == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        tampilkan_daftar_monster()
                        print("================ DETAIL MONSTER ================")
                        id_monster = input_id_monster()
                        tampilkan_detail_monster(id_monster)
                        
                    elif menu_hunter == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Logout berhasil!")
                        break

                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Pilihan tidak valid! Silahkan pilih menu 1-3!")
                        
                    input("Tekan Enter untuk kembali ke menu...") 

            elif role == "Admin":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(r"""
                      /\_/\
                     /_____\
                    /| o o |\
                   ( |  ^  | )
                    \|_____/
                     /|___|\
                    / |___| \
                    """)
                    print("==================================================")
                    print("              🛡️ MHML - ADMIN MENU 🛡️")
                    print("==================================================")
                    print("Selamat datang", role, username)
                    print("==================================================")
                    print("1. Daftar Monster")
                    print("2. Detail Monster")
                    print("3. Tambah Monster")
                    print("4. Ubah Data Monster")
                    print("5. Hapus Monster")
                    print("6. Logout")
                    print("==================================================")

                    menu_admin = input("Pilih menu: ")

                    if menu_admin == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        tampilkan_daftar_monster()

                    elif menu_admin == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        tampilkan_daftar_monster()
                        print("================ DETAIL MONSTER ================")
                        id_monster = input_id_monster()
                        tampilkan_detail_monster(id_monster)

                    elif menu_admin == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("================ TAMBAH MONSTER ================")

                        id_monster = input("Masukkan ID Monster: ").strip().upper()

                        if id_monster == "":
                            print("ID Monster tidak boleh kosong!")

                        elif id_monster in monster:
                            print("ID Monster sudah digunakan!")

                        else:
                            nama = input("Nama Monster: ").strip()
                            jenis = input("Jenis Monster: ").strip()
                            elemen = input("Elemen/Status: ").strip()
                            habitat = input("Habitat: ").strip()
                            kelemahan = input("Kelemahan: ").strip()
                            ancaman = input("Tingkat Ancaman (Rendah/Menengah/Tinggi): ").strip().capitalize()

                            if (
                                nama == "" or jenis == "" or elemen == ""
                                or habitat == "" or kelemahan == ""
                                or ancaman == ""
                            ):  
                                print("Semua data monster harus diisi!")

                            elif not validasi_ancaman(ancaman):
                                print("Tingkat ancaman harus Rendah, Menengah, atau TInggi!")

                            else:
                                monster[id_monster] = {
                                    "nama": nama,
                                    "jenis": jenis,
                                    "elemen": elemen,
                                    "habitat": habitat,
                                    "kelemahan": kelemahan,
                                    "ancaman": ancaman
                                }

                                print("Monster berhasil ditambahkan!")

                    elif menu_admin == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("================ UBAH DATA MONSTER ================")

                        id_monster = input("Masukkan ID Monster yang ingin diubah: ").strip().upper()

                        if id_monster in monster:
                            data = monster[id_monster]

                            print("1. Nama Monster")
                            print("2. Jenis Monster")
                            print("3. Elemen/Status")
                            print("4. Habitat")
                            print("5. Kelemahan")
                            print("6. Tingkat Ancaman")

                            pilihan_ubah = input(
                                "Pilih data yang ingin diubah (1-6): "
                            )

                            kolom = {
                                "1": "nama",
                                "2": "jenis",
                                "3": "elemen",
                                "4": "habitat",
                                "5": "kelemahan",
                                "6": "ancaman"
                            }

                            if pilihan_ubah in kolom:
                                kunci = kolom[pilihan_ubah]
                                data_baru = input(
                                    "Masukkan data baru: "
                                ).strip()

                                if pilihan_ubah == "6":
                                    data_baru = data_baru.capitalize()

                                if data_baru == "":
                                    print("Data tidak boleh kosong!")

                                elif pilihan_ubah == "6" and not validasi_ancaman(data_baru):
                                    print("Tingkat ancaman tidak valid!")

                                else:
                                    data[kunci] = data_baru
                                    print("Data monster berhasil diubah!")

                            else:
                                print("Pilihan tidak valid!")

                        else:
                            print("Monster tidak ditemukan!")

                    elif menu_admin == "5":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("================ HAPUS MONSTER ================")

                        id_monster = input("Masukkan ID Monster yang ingin dihapus: ").strip().upper()

                        if id_monster in monster:
                            print("Nama Monster:", monster[id_monster]["nama"])

                            konfirmasi = input(
                                "Yakin ingin menghapus? (y/n): "
                            ).strip().lower()

                            if konfirmasi == "y":
                                del monster[id_monster]
                                print("Monster berhasil dihapus!")

                            elif konfirmasi == "n":
                                print("Penghapusan dibatalkan!")

                            else:
                                print("Pilihan tidak valid!")
                                print("Penghapusan dibatalkan!")

                        else:
                            print("Monster tidak ditemukan!")

                    elif menu_admin == "6":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Logout berhasil!")
                        break

                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Pilihan tidak valid! Silahkan pilih menu 1-6!")
                        
                    input("Tekan Enter untuk kembali ke menu...") 

        else:
            print("Username atau password salah!")
            print("Silakan Register terlebih dahulu jika belum memiliki akun.")

    elif pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER ===")
        username = input("Buat username: ").strip().lower()
        password = input("Buat password: ").strip()

        try:
            if username == "" or password == "":
                raise ValueError("Username dan password tidak boleh kosong!")
            elif len(username) < 3:
                raise ValueError("Username minimal 3 karakter!")
            elif username in akun:
                raise ValueError("Username sudah digunakan!")
        except ValueError as kesalahan:
            print("Registrasi gagal:", kesalahan)
        else:
            akun[username] = {
                "password": password,
                "role": "Hunter"
            }
            print("Registrasi berhasil!")
            print("Silakan Login menggunakan akun baru.")
        finally:
            print("Proses register selesai.")

    elif pilihan == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("""
        ⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜
        ⬜⬜⬛🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫⬛⬜⬜
        ⬜⬜⬛🟫🟫⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛🟫🟫⬛⬜⬜
        ⬜⬜⬛🟫🟫🟫⬛⬛🏽🏽🏽🟫🏽🏽🏽⬛⬛🟫🟫🟫⬛⬜⬜
        ⬜⬜⬛🟫🟫⬛🏽🏽🏽🏽🟫🟫🟫🏽🏽🏽🏽⬛🟫🟫⬛⬜⬜
        ⬜⬜⬛🟫⬛🏽🏽🏽🏽🟫🟫🟫🟫🟫🏽🏽🏽🏽⬛🟫⬛⬜⬜
        ⬜⬜⬜⬛🏽🏽⬛⬛🟫🟫🟫🟫🟫🟫🟫⬛⬛🏽🏽⬛⬜⬜⬜
        ⬜⬜⬜⬛🏽⬛⬜⬜⬛🟫🟫🟫🟫🟫⬛⬜⬜⬛🏽⬛⬜⬜⬜
        ⬜⬜⬛🏽⬛⬜⬛⬛⬜⬛🟫🟫🟫⬛⬜⬛⬛⬜⬛🏽⬛⬜⬜
        ⬛⬛⬛🏽⬛⬜⬛⬛⬜⬛🟫⬛🟫⬛⬜⬛⬛⬜⬛🏽⬛⬛⬛
        ⬜⬜⬛🏽🏽⬛⬜⬜⬛🟫⬛⬛⬛🟫⬛⬜⬜⬛🏽🏽⬛⬜⬜
        ⬛⬛⬛🏽🏽🏽⬛⬛🟫⬛⬛🟪⬛⬛🟫⬛⬛🟫⬛🏽⬛⬛⬛
        ⬜⬜⬛🏽🏽🟫🟫🟫🟫🟫🟫⬛🟫🟫🟫⬛🏽⬛🏽🏽⬛⬜⬜
        ⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🏽⬛⬛⬛⬛⬛⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬛⬛🏽🏽🟫🏽🏽⬛⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬛🏽⬛🏽🟫🏽🟫🏽⬛⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛🏽⬛⬛🏽🏽🟫🏽🏽⬛⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛🟫⬛⬜⬛🏽🏽🏽🏽🏽⬛⬜⬜⬜⬜⬛⬛⬜⬜
        ⬜⬜⬜⬜⬛⬛⬜⬜⬛🟫🟫🟫🟫🟫⬛⬛⬜⬜⬛🟫⬛⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛🏽🏽🏽🏽🏽⬛🏽⬛⬛🟫⬛⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛🏽🏽⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛🏽⬛⬜⬛🏽⬛⬜⬛⬛⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫⬛⬜⬛🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
        """)
        print("Selamat Tinggal dan Sampai Jumpa")
        break

    else:
        os.system("cls" if os.name == "nt" else "clear")
        
        print("Pilihan tidak valid! Silahkan pilih menu 1-3!")
    
    input("Tekan Enter untuk kembali ke menu...") 