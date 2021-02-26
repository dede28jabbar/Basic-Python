# Soal 1
nama = str (input("Nama kamu : "))
umur =input("Umur kamu: ")
tinggi = input("Tinggi kamu (dalam cm yaa):")
print ("Nama saya " + nama + ", umur saya " + umur + " tahun dan tinggi saya " + tinggi + " cm")

# Soal 2
jarijari = float(input("Masukkan jari-jari lingkaran : "))
luaslingkaran = float(3.14*jarijari*jarijari)
print(luaslingkaran)
print("Luas lingkaran dengan jari-jari " + str(jarijari) + " cm adalah " + str(luaslingkaran) + " cm.")

# Soal 3
# NUP = Nilai Ujian Praktek
# NUT = Nilai Ujian Teori
NUP = 2
NUT = 711
if NUP >= 75 and NUT >= 75:
    print("Selamat, anda lulus!")
elif NUP >= 75 and NUT <= 75:
    print("Anda harus mengulang ujian praktek.")
elif NUP <= 75 and NUT >= 75:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")