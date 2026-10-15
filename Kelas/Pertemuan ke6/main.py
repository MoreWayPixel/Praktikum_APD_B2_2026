# kartu = {"merah", "merah", "biru", "hijau"}

# kartu.add("hytam")\
    
# kartu.remove("hijau") #rawan eror jika data yg ingin dihapus tidak ditemukan

# kartu.discard("red") #menghindari eror saat menghapus data yg tidak ada

# print(kartu)

# set menggunakan list
# matkul = ["apd", "orsikom", "apd", "kalkulus"]

# sks = set(matkul)
# print(sks)

# angka_ganjil = {1, 3, 5, 7, 9}

# for angka in angka_ganjil:
#     print(angka)

# aslab1 = {"fina", "shasha", "risma", "attar"}
# aslab2 = {"larry", "attar", "haekal"}
# aslab3 = {"rafi", "rendi", "yoga"}

# # gabung = aslab1.union(aslab2)

# # gabungan_lengkap = gabung.union(aslab3)

# # aslab1.update(aslab2)

# # print(f"nilai aslab1 : {aslab1}")

# irisan_aslab1_aslab2 = aslab1.difference(aslab2)

# print(irisan_aslab1_aslab2)

# Matkul = {
#     "Matkul_ganjil" : "kalkulus",
#     "Matkul_genap" : "statistik"
# }
# print(Matkul.get("Matkul_ganp", "Key tidak ada"))

game = {
"pou" : "chill",
"genshin impact" : "action",
"valorant" : "fps",
"minecraft" : "sandbox",
"mobile legend" : "moba"
}

# print(len(game))

# game_copy = game.copy()

# del game_copy["valorant"]
# del game_copy["mobile legend"]

# print(game)
# print(game_copy)

# for i in game.keys():
#     print(i)

# for i in game.values():
#     print(i)

# for key, value in game.items():
#     print(key,"adalah game", value)

# game["resident evil"] = "horror"

# for key, value in game.items():
#     print(key,"adalah game", value)

# game["valorant"] = "Action"

# game.update({"minecraft" : "horror"})

# item = game.setdefault("pou","Battle Royal")
# print(item)

# for key, value in game.items():
#     print(key,"adalah game", value)

# del game["valorant"]
# print(game)

# item_dihapus = game.pop("minecraft")
# print(game)
# print(item_dihapus)

# game.clear()
# print(game)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000
# menu = dict.fromkeys(key, value)

# print(menu)

menu = {
    "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
    "nasi" : ["nasi goreng", "nasi uduk"],
    "mie" : ["mie goreng rendang", "mie goreng aceh"],
    "kuah" : ["soto", "rawon", "sop iga"]
}

print(menu.get("ayam")[2])

mahasiswa = {
    "054":{"nama":"Daniel",
           "IPK": 4.00
           },
    "056":{"nama":"Alfi",
               "IPK": 4.00
               },
    "058":{"nama":"Sartika",
               "IPK": 4.00
               },
}

print(mahasiswa["056"]["nama"])