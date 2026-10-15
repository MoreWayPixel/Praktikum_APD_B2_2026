import os 

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")
    
akun = [
    ["rizky", "admin123", "Admin"],
    ["buma", "123", "Hunter"] #akun uji coba
]

monster = [
    ["M001", "Great Izuchi", "Bird Wyvern", "Tidak ada",
     "Shrine Ruins", "Thunder, Ice", "Rendah"],

    ["M002", "Aknosom", "Bird Wyvern", "Api",
     "Shrine Ruins", "Water, Thunder", "Rendah"],

    ["M003", "Arzuros", "Fanged Beast", "Tidak ada",
     "Shrine Ruins", "Fire", "Rendah"],

    ["M004", "Tetranadon", "Amphibian", "Air",
     "Shrine Ruins", "Thunder", "Rendah"],

    ["M005", "Royal Ludroth", "Leviathan", "Air",
     "Flooded Forest", "Fire, Thunder", "Menengah"],

    ["M006", "Mizutsune", "Leviathan", "Air",
     "Shrine Ruins", "Thunder, Dragon", "Tinggi"],

    ["M007", "Rathian", "Flying Wyvern", "Api, Racun",
     "Shrine Ruins", "Dragon, Thunder", "Menengah"],

    ["M008", "Rathalos", "Flying Wyvern", "Api, Racun",
     "Shrine Ruins", "Dragon, Thunder", "Tinggi"],

    ["M009", "Pukei-Pukei", "Bird Wyvern", "Racun",
     "Flooded Forest", "Thunder, Ice", "Menengah"],

    ["M010", "Kulu-Ya-Ku", "Bird Wyvern", "Tidak ada",
     "Sandy Plains", "Water", "Rendah"],

    ["M011", "Anjanath", "Brute Wyvern", "Api",
     "Sandy Plains", "Water", "Tinggi"],

    ["M012", "Barroth", "Brute Wyvern", "Tidak ada",
     "Sandy Plains", "Fire, Ice", "Menengah"],

    ["M013", "Tobi-Kadachi", "Fanged Wyvern", "Thunder",
     "Shrine Ruins", "Water, Ice", "Menengah"],

    ["M014", "Zinogre", "Fanged Wyvern", "Thunder",
     "Shrine Ruins", "Ice", "Tinggi"],

    ["M015", "Magnamalo", "Fanged Wyvern", "Hellfireblight",
     "Shrine Ruins", "Water, Thunder", "Tinggi"]
]

while True:
    bersihkan_layar()
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
        bersihkan_layar()
        print("=== LOGIN ===")
        username = input("Username: ").strip().lower()
        password = input("Password: ").strip()

        login_berhasil = False
        role = ""

        for data in akun:
            if data[0] == username and data[1] == password:
                login_berhasil = True
                role = data[2]
                break

        
        if login_berhasil:
            print("Login berhasil!")
            print("Selamat datang,", username)
            print("Role:", role)

            if role == "Hunter":
                while True:
                    bersihkan_layar()
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
                        bersihkan_layar()
                        print("================ DAFTAR MONSTER ================")

                        for data in monster:
                            print(data[0], "-", data[1]) 

                    elif menu_hunter == "2":
                        bersihkan_layar()
                        print("================ DETAIL MONSTER ================")
                        id_monster = input("Masukkan ID Monster: ").strip().upper()

                        monster_ditemukan = False

                        for data in monster:
                            if data[0] == id_monster:
                                monster_ditemukan = True
                                print("ID Monster       :", data[0])
                                print("Nama Monster     :", data[1])
                                print("Jenis Monster    :", data[2])
                                print("Elemen/Status    :", data[3])
                                print("Habitat          :", data[4])
                                print("Kelemahan        :", data[5])
                                print("Tingkat Ancaman  :", data[6])
                                break

                        if not monster_ditemukan:
                                print("Monster tidak ditemukan!")
                        
                    elif menu_hunter == "3":
                        bersihkan_layar()
                        print("Logout berhasil!")
                        break

                    else:
                        bersihkan_layar()
                        print("Pilihan tidak valid! Silahkan pilih menu 1-3!")
                        
                    input("Tekan Enter untuk kembali ke menu...") 

            else:
                role == "Admin"
                while True:
                    bersihkan_layar()
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
                        bersihkan_layar()
                        print("================ DAFTAR MONSTER ================")

                        for data in monster:
                            print(data[0], "-", data[1])

                    elif menu_admin == "2":
                        bersihkan_layar()
                        print("================ DETAIL MONSTER ================")
                        id_monster = input("Masukkan ID Monster: ").strip().upper()

                        monster_ditemukan = False

                        for data in monster:
                            if data[0] == id_monster:
                                monster_ditemukan = True
                                print("ID Monster      :", data[0])
                                print("Nama Monster    :", data[1]) 
                                print("Jenis Monster   :", data[2])
                                print("Elemen/Status   :", data[3])
                                print("Habitat         :", data[4])
                                print("Kelemahan       :", data[5])
                                print("Tingkat Ancaman :", data[6])
                                break

                        if not monster_ditemukan:
                            print("Monster tidak ditemukan!")
                            
                    elif menu_admin == "3":
                        bersihkan_layar()
                        print("================ TAMBAH MONSTER ================")

                        id_monster = input("Masukkan ID Monster: ").strip().upper()

                        id_tersedia = True

                        for data in monster:
                            if data[0] == id_monster:
                                id_tersedia = False
                                break

                        if id_monster == "":
                            print("ID Monster tidak boleh kosong!")

                        elif not id_tersedia:
                            print("ID Monster sudah digunakan!")

                        else:
                            nama = input("Nama Monster: ").strip()
                            jenis = input("Jenis Monster: ").strip()
                            elemen = input("Elemen/Status: ").strip()
                            habitat = input("Habitat: ").strip()
                            kelemahan = input("Kelemahan: ").strip()
                            ancaman = input("Tingkat Ancaman: ").strip().capitalize()

                            if nama == "" or jenis == "" or elemen == "" or habitat == "" or kelemahan == "" or ancaman == "":
                                print("Semua data monster harus diisi!")

                            elif ancaman not in ["Rendah", "Menengah", "Tinggi"]:
                                print("Tingkat ancaman harus Rendah, Menengah, atau Tinggi!")

                            else:
                                monster.append([
                                    id_monster, nama, jenis, elemen,
                                    habitat, kelemahan, ancaman
                                ])

                                print("Monster berhasil ditambahkan!")

                    elif menu_admin == "4":
                        bersihkan_layar()
                        print("================ UBAH DATA MONSTER ================")

                        id_monster = input("Masukkan ID Monster yang ingin diubah: ").strip().upper()

                        monster_ditemukan = False

                        for data in monster:
                            if data[0] == id_monster:
                                monster_ditemukan = True

                                print("Data Monster Saat Ini:")
                                print("1. Nama Monster    :", data[1])
                                print("2. Jenis Monster   :", data[2])
                                print("3. Elemen/Status   :", data[3])
                                print("4. Habitat         :", data[4])
                                print("5. Kelemahan       :", data[5])
                                print("6. Tingkat Ancaman :", data[6])

                                pilihan_ubah = input("Pilih data yang ingin diubah (1-6): ")

                                if pilihan_ubah == "1":
                                    data_baru = input("Masukkan nama baru: ").strip()
                                    if data_baru != "":
                                        data[1] = data_baru
                                        print("Nama monster berhasil diubah!")
                                    else:
                                        print("Nama tidak boleh kosong!")

                                elif pilihan_ubah == "2":
                                    data_baru = input("Masukkan jenis baru: ").strip()
                                    if data_baru != "":
                                        data[2] = data_baru
                                        print("Jenis monster berhasil diubah!")
                                    else:
                                        print("Jenis tidak boleh kosong!")

                                elif pilihan_ubah == "3":
                                    data_baru = input("Masukkan elemen/status baru: ").strip()
                                    if data_baru != "":
                                        data[3] = data_baru
                                        print("Elemen/status berhasil diubah!")
                                    else:
                                        print("Elemen/status tidak boleh kosong!")

                                elif pilihan_ubah == "4":
                                    data_baru = input("Masukkan habitat baru: ").strip()
                                    if data_baru != "":
                                        data[4] = data_baru
                                        print("Habitat berhasil diubah!")
                                    else:
                                        print("Habitat tidak boleh kosong!")

                                elif pilihan_ubah == "5":
                                    data_baru = input("Masukkan kelemahan baru: ").strip()
                                    if data_baru != "":
                                        data[5] = data_baru
                                        print("Kelemahan berhasil diubah!")
                                    else:
                                        print("Kelemahan tidak boleh kosong!")

                                elif pilihan_ubah == "6":
                                    data_baru = input("Masukkan tingkat ancaman baru: ").strip().capitalize()

                                    if data_baru in ["Rendah", "Menengah", "Tinggi"]:
                                        data[6] = data_baru
                                        print("Tingkat ancaman berhasil diubah!")
                                    else:
                                        print("Tingkat ancaman harus Rendah, Menengah, atau Tinggi!")

                                else:
                                    print("Pilihan tidak valid!")

                                break

                        if not monster_ditemukan:
                            print("Monster tidak ditemukan!")

                    elif menu_admin == "5":
                        bersihkan_layar()
                        print("================ HAPUS MONSTER ================")

                        id_monster = input("Masukkan ID Monster yang ingin dihapus: ").strip().upper()

                        monster_ditemukan = False

                        for data in monster:
                            if data[0] == id_monster:
                                monster_ditemukan = True

                                print("ID Monster   :", data[0])
                                print("Nama Monster :", data[1])

                                konfirmasi = input("Yakin ingin menghapus monster ini? (y/n): ").strip().lower()

                                if konfirmasi == "y":
                                    monster.remove(data)
                                    print("Monster berhasil dihapus!")

                                elif konfirmasi == "n":
                                    print("Penghapusan dibatalkan!")

                                else:
                                    print("Pilihan tidak valid. Penghapusan dibatalkan!")

                                break

                        if not monster_ditemukan:
                            print("Monster tidak ditemukan!")

                    elif menu_admin == "6":
                        bersihkan_layar()
                        print("Logout berhasil!")
                        break

                    else:
                        bersihkan_layar()
                        print("Pilihan tidak valid! Silahkan pilih menu 1-6!")
                        
                    input("Tekan Enter untuk kembali ke menu...") 

        else:
            print("Username atau password salah!")
            print("Silakan Register terlebih dahulu jika belum memiliki akun.")

    elif pilihan == "2":
        bersihkan_layar()
        print("=== REGISTER ===")
        username = input("Buat username: ")
        password = input("Buat password: ")

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong!")

        else:
            username_tersedia = True

            for data in akun:
                if data[0] == username:
                    username_tersedia = False
                    break

            if username_tersedia:
                akun.append([username, password, "Hunter"])
                print("Registrasi berhasil!")
                print("Silakan Login menggunakan akun yang telah dibuat.")
            else:
                print("Username sudah digunakan!")

    elif pilihan == "3":
        bersihkan_layar()
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
        bersihkan_layar()
        
        print("Pilihan tidak valid! Silahkan pilih menu 1-3!")
    
    input("Tekan Enter untuk kembali ke menu...") 