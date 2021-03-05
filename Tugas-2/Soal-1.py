while True:
    print("Selamat Datang!")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        read = open("Kontak.txt","r")
        data = read.readlines()
        for i in range(0,len(data),2):
            print("Nama : {} No. Telepon : {}".format(data[i],data[i+1]))
        read.close()
    elif pilihan == 2:
        create = open("Kontak.txt","a")
        Nama = input("Nama kamu: ")
        NoTelp = input("Nomor Telepon kamu: ")
        create.write(Nama+"\n")
        create.write(NoTelp+"\n")
        create.close()
    elif pilihan == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")