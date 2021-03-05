# Soal 3
# NUP = Nilai Ujian Praktek
# NUT = Nilai Ujian Teori
NUP = 90
NUT = 80
if NUP >= 75 and NUT >= 75:
    print("Selamat, anda lulus!")
elif NUP >= 75 and NUT <= 75:
    print("Anda harus mengulang ujian praktek.")
elif NUP <= 75 and NUT >= 75:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")