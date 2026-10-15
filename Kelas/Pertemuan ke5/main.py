formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]

for index, elemen in enumerate (formula1, start=1):
    print(index, elemen)

sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"] #list
print(sirkuit)

sirkuit.append("Daniel")
print(sirkuit)

sirkuit.append("Nando") #menambah 1 elemen baru
print(sirkuit)

sirkuit.extend(["Larry", "Rendy"]) #menambah banyak elemen baru sekaligus
print(sirkuit)

sirkuit.insert(2, "Alfi") #menambah elemen ke index tertentu
print(sirkuit)

sirkuit[3] = "Apip" #merubah elemen melalui index langsung
print(sirkuit)

# sirkuit[0:1] = ["Rizky", "Naufal"] #merubah banyak element sekaligus
# print(sirkuit)

# nama_list[start:stop:step]
sirkuit[0:5:2] = ["Naufal", "Rizky", "Rahman"]
print(sirkuit)

del sirkuit[4]
print(sirkuit)

sirkuit.remove ("Apip")
print(sirkuit)

nama_dihapus = sirkuit.pop(5)
print(sirkuit)
print(nama_dihapus)

print(sirkuit[0:4:2])

matkul_1 = ["kalkulus", "logma", "apd"]
matkul_2 = ["basis data", "apl", "pbo"]

matkul_gabungan = matkul_1 + matkul_2
print(matkul_gabungan)

angka1= [1,2,3]
angka2= [4,5,6]

angka_gabungan = angka1 + angka2
print(angka_gabungan)

matkul_1 = matkul_1 * 5
print(matkul_1)

line_up = [
["Ferrari", "Leclerc", 16],
["Mercedes", "Hamilton", 44],
["Red Bull", "Verstappen", 1],
["McLaren", "Norris", 4]
]

print(line_up[2][1])

for i in line_up:
    for j in i:
        print(j)

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
listchara = list(chara)

print(type(listchara))

listchara.append("naruto")
print(listchara)

del listchara[6]

listchara.remove("Yukari")

print (f"tuple listchara setelah di del: {listchara}")

chara = ("Yukari", "Yukino", "Odette", "Senku", "yagami", "Naruto")
(Persona, Oregairu, Genshin, DrStone, *Anime) = chara

print(Persona)
print(Oregairu)
print(Anime)

