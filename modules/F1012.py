# Kamus
# tanggal : string
# db_consumable : variabel global dari load data / matriks consumable.csv
# db_consumable_history : variabel global dari load data / matriks consumable_history.csv
# db_gadget_borrow_history : variabel global dari load data / matriks gadget_borrow_history.csv
# db_gadget_return_history : variabel global dari load data / matriks gadget_return_history.csv
# db_user : variabel global dari load data / matriks user.csv
# minta() -> F10
# riwayatpinjam() -> F11
# riwayatkembali() -> F12

def matriks(csv):
    # I.S. mengimport file csv
    # F.S. file csv dijadikan matriks
    with open(csv, 'r') as file:
        line = [clean_line.replace('\n', '') for clean_line in file.readlines()]
        array = []
        for i in range(len(line)):
            tempArr = []
            counter = 0
            string = line[i]
            length = len(line[i])
            for j in range(length):
                if j == length - 1:
                    tempArr.append(string[counter:(j + 1)])
                elif string[j] == ';':
                    tempArr.append(string[counter:j])
                    counter = j + 1
            array.append(tempArr)
    return array

def convert(matriks, Str=False, Int=False):
    # I.S. tipe data elemen pada matriks tidak sesuai keinginan
    # F.S. tipe data elemen pada matriks berubah sesuai keinginan
    # Pilihan tipe: Str : string / Int : integer
    if Str:
        for i in matriks:
            for j in range(len(i)):
                try:
                    i[j] = str(i[j])
                except:
                    continue
    if Int:
        for i in matriks:
            for j in range(len(i)):
                try:
                    i[j] = int(i[j])
                except:
                    continue
    return matriks

def cek_tanggal(tanggal):
    # I.S. memasukkan data tanggal dengan bentuk "--/--/----"
    # F.S. mengembalikan list angka dari tanggal tersebut
    v = ""
    hasil_tanggal=[]
    raw_tanggal = tanggal + "/"
    for w in raw_tanggal:
        if (w == "/"):
            hasil_tanggal.append(int(v))
            v = ""
        else:
            v += w
    return(hasil_tanggal)

def sort_tanggal(array):
    # I.S. menerima matriks away yang diubah oleh fungsi matriks untuk
    #      file gadget borrow history dan gadget return history
    # F.S. mengeluarkan matriks yang sudah diurutkan berdasarkan tanggal
    #      menggunakan selection sort
    array_sort = array
    for i in range(1, len(array) - 1):
        Imax = i
        for j in range(i, len(array)):
            tanggal_baris_start = cek_tanggal(array_sort[i][3])
            tanggal_baris_lain = cek_tanggal(array_sort[j][3])
            if (tanggal_baris_start[2] < tanggal_baris_lain[2]):
                Imax = j
                array_simpan = array_sort[Imax]
                array[Imax] = array_sort[i]
                array_sort[i] = array_simpan
            elif (tanggal_baris_start[2] == tanggal_baris_lain[2]):
                if (tanggal_baris_start[1] < tanggal_baris_lain[1]):
                    Imax = j
                    array_simpan = array_sort[Imax]
                    array[Imax] = array_sort[i]
                    array_sort[i] = array_simpan
                elif (tanggal_baris_start[1] == tanggal_baris_lain[1]):
                    if (tanggal_baris_start[0] < tanggal_baris_lain[0]):
                        Imax = j
                        array_simpan = array_sort[Imax]
                        array[Imax] = array_sort[i]
                        array_sort[i] = array_simpan
    return (array_sort)

def sort_tanggal_2(array):
    # I.S. menerima matriks away yang diubah oleh fungsi matriks untuk
    #      file gadget borrow history dan gadget return history
    # F.S. mengeluarkan matriks yang sudah diurutkan berdasarkan tanggal
    #      menggunakan selection sort
    array_sort = array
    for i in range(1, len(array) - 1):
        Imax = i
        for j in range(i, len(array)):
            tanggal_baris_start = cek_tanggal(array_sort[i][2])
            tanggal_baris_lain = cek_tanggal(array_sort[j][2])
            if (tanggal_baris_start[2] < tanggal_baris_lain[2]):
                Imax = j
                array_simpan = array_sort[Imax]
                array[Imax] = array_sort[i]
                array_sort[i] = array_simpan
            elif (tanggal_baris_start[2] == tanggal_baris_lain[2]):
                if (tanggal_baris_start[1] < tanggal_baris_lain[1]):
                    Imax = j
                    array_simpan = array_sort[Imax]
                    array[Imax] = array_sort[i]
                    array_sort[i] = array_simpan
                elif (tanggal_baris_start[1] == tanggal_baris_lain[1]):
                    if (tanggal_baris_start[0] < tanggal_baris_lain[0]):
                        Imax = j
                        array_simpan = array_sort[Imax]
                        array[Imax] = array_sort[i]
                        array_sort[i] = array_simpan
    return (array_sort)

def minta(db_consumable, db_consumable_history, user):
    # I.S. pengguna memasukkan ID item, jumlah item, dan tanggal item diambil
    # F.S. menampilkan apakah item berhasil diambil, mengembalikan list item baru, mencatat
    #      pengambilan item tersebut
    id_snack = str(input("Masukan ID Item: "))
    jumlah = int(input("Jumlah: "))
    tanggal = str(input("Tanggal permintaan: "))
    permintaan = []
    ubah_tanggal = cek_tanggal(tanggal)
    v = ""
    baris_snack = int
    # melakukan pengecekan tanggal untuk memastikan tanggal yang dimasukkan valid
    if (ubah_tanggal[0] <= 31 and ubah_tanggal[1] == 1) or (
            ubah_tanggal[0] <= 28 and ubah_tanggal[1] == 2) or (
            ubah_tanggal[0] <= 29 and ubah_tanggal[1] == 2 and (
            ubah_tanggal[2] % 400 == 0 or (
            ubah_tanggal[2] % 4 == 0 and ubah_tanggal[2] % 100 != 0))) or (
            ubah_tanggal[0] <= 31 and ubah_tanggal[1] == 3) or (
            ubah_tanggal[0] <= 30 and ubah_tanggal[1] == 4) or (
            ubah_tanggal[0] <= 31 and ubah_tanggal[1] == 5) or (
            ubah_tanggal[0] <= 30 and ubah_tanggal[1] == 6) or (
            ubah_tanggal[0] <= 31 and ubah_tanggal[1] == 7) or (
            ubah_tanggal[0] <= 31 and ubah_tanggal[1] == 8) or (
            ubah_tanggal[0] <= 30 and ubah_tanggal[1] == 9) or (
            ubah_tanggal[0] <= 31 and ubah_tanggal[1] == 10) or (
            ubah_tanggal[0] <= 30 and ubah_tanggal[1] == 11) or (
            ubah_tanggal[0] <= 31 and ubah_tanggal[1] == 12):
        # permintaan digunakan untuk menyimpan input data pengguna dan menambahkan id peminjaman
        # ID dibuat berdasarkan banyak baris di file csv
        permintaan = ["CH" + str(len(db_consumable_history) + 1), user[1], id_snack, tanggal, jumlah]
        for i in range(1, len(db_consumable)):
            if (id_snack == db_consumable[i][0]):
                baris_snack = i
        if (baris_snack == int):
            print("item tidak ditemukan")
        elif (int(db_consumable[baris_snack][3]) >= jumlah):
            total_baru = int(db_consumable[baris_snack][3])
            total_baru -= jumlah
            db_consumable[baris_snack][3] = total_baru
            print("item " + str(db_consumable[baris_snack][1] + " (x" + str(jumlah) + ") telah berhasil diambil!"))
            consumable_finale = convert(db_consumable, Str=True)

            chbaru = [["" for i in range(5)] for j in range(0, (len(db_consumable_history)) + 1)]
            for i in range(0, len(db_consumable_history)):
                for j in range(0, 5):
                    chbaru[i][j] = db_consumable_history[i][j]

            for i in range(0, 5):
                chbaru[len(db_consumable_history)][i] = permintaan[i]
            consumehistory_final = convert(chbaru, Str=True)
            return (consumable_finale, consumehistory_final)

        elif (db_consumable[baris_snack][3] == 0):
            print("item sudah habis")
        elif (int(db_consumable[baris_snack][3]) < jumlah):
            print("item tidak cukup")

    else:
        print("tanggal tidak valid")


def riwayatpinjam(db_gadget_borrow_history, db_user, db_gadget, user):
    # I.S. mengecek jika akun pengguna adalah admin
    # F.S. menampilkan sejarah gadget yang dipinjam semua pengguna, mulai dari yang paling baru
    #      (menampilkan 5 data pertama, jika diminta dapat menampilkan lebih banyak)
    if user[5]=="Admin":
        borrow_hist_sort=sort_tanggal(db_gadget_borrow_history)

        # mencari nama orang dari id peminjam
        for i in range(1, len(db_gadget_borrow_history)):
            for j in range(1, len(db_user)):
                if (borrow_hist_sort[i][1] == db_user[j][0]):
                    borrow_hist_sort[i][1] = db_user[j][2]
        # mencari nama gadget dari id gadget
        for i in range(1, len(db_gadget_borrow_history)):
            for j in range(1, len(db_gadget)):
                if (borrow_hist_sort[i][2] == db_gadget[j][0]):
                    borrow_hist_sort[i][2] = db_gadget[j][1]

        barishistory = len(db_gadget_borrow_history) - 1
        barisawal = 1
        v = 1
        w = 1

        # mencetak hasil permintaan riwayatpinjam
        while (v < 2):
            if (barishistory > 5):
                while (w <= 5 and barisawal <= barishistory):
                    print("ID Peminjaman: " + str(borrow_hist_sort[barisawal][0]))
                    print("Nama Pengambil: " + str(borrow_hist_sort[barisawal][1]))
                    print("Nama Gadget: " + str(borrow_hist_sort[barisawal][2]))
                    print("Tanggal Peminjaman: " + str(borrow_hist_sort[barisawal][3]))
                    print("Jumlah: " + str(borrow_hist_sort[barisawal][4]))
                    print("")
                    barisawal += 1
                    w += 1
                if (barishistory >= barisawal):
                    mengulang = str(input("Apakah anda ingin melihat data selanjutnya (Y/N): "))
                    if (mengulang == "Y") or (mengulang == "y"):
                        w = 1
                    else:
                        v = 2
                else:
                    v = 2
            elif (0 < barishistory and barishistory <= 5):
                for i in range(1, barishistory+1):
                    print("ID Peminjaman: " + str(borrow_hist_sort[i][0]))
                    print("Nama Pengambil: " + str(borrow_hist_sort[i][1]))
                    print("Nama Gadget: " + str(borrow_hist_sort[i][2]))
                    print("Tanggal Peminjaman: " + str(borrow_hist_sort[i][3]))
                    print("Jumlah: " + str(borrow_hist_sort[i][4]))
                    print("")
                v = 2
            elif (barishistory == 0):
                print("Belum ada barang yang dipinjam")
                v = 2
    else:
        print("Anda tidak dapat mengakses riwayat pinjam")

def riwayatkembali(db_gadget_return_history, db_user, db_gadget, user):
    # I.S. mengecek jika akun pengguna adalah admin
    # F.S. menampilkan sejarah gadget yang dikembalikan semua pengguna, mulai dari yang paling baru
    #      (menampilkan 5 data pertama, jika diminta dapat menampilkan lebih banyak)

    # mengecek jika user adalah admin
    if user[5] == "Admin":
        return_hist_sort=sort_tanggal_2(db_gadget_return_history)
        # catatan digunakan untuk menyimpan data nama pengambil dan nama gadget

        # mencari nama orang dari id peminjam
        for i in range(1, len(db_gadget_return_history)):
            for j in range(1, len(db_user)):
                if (return_hist_sort[i][3] == db_user[j][0]):
                    return_hist_sort[i][3] = db_user[j][2]
        # mencari nama gadget dari id gadget
        for i in range(1, len(db_gadget_return_history)):
            for j in range(1, len(db_gadget)):
                if (return_hist_sort[i][4] == db_gadget[j][0]):
                    return_hist_sort[i][4] = db_gadget[j][1]

        barishistory = len(db_gadget_return_history) - 1
        barisawal = 1
        v = 1
        w = 1

        # mencetak hasil permintaan riwayatkembali
        while (v < 2):
            if (barishistory > 5):
                while (w <= 5 and barisawal <= barishistory):
                    print("ID pengembalian: " + str(return_hist_sort[barisawal][1]))
                    print("Nama pengambil: " + str(return_hist_sort[barisawal][3]))
                    print("Nama Gadget: " + str(return_hist_sort[barisawal][4]))
                    print("Tanggal pengambilan: " + str(return_hist_sort[barisawal][2]))
                    print("Jumlah: " + str(return_hist_sort[barisawal][5]))
                    print("")
                    barisawal += 1
                    w += 1
                if (barishistory >= barisawal):
                    mengulang = str(input("Apakah anda ingin melihat data selanjutnya (Y/N): "))
                    if (mengulang == "Y") or (mengulang == "y"):
                        w = 1
                    else:
                        v = 2
                else:
                    v = 2

            elif (0 < barishistory and barishistory <= 5):
                for barisawal in range(1, barishistory + 1):
                    print("ID pengembalian: " + str(return_hist_sort[barisawal][1]))
                    print("Nama pengambil: " + str(return_hist_sort[barisawal][3]))
                    print("Nama Gadget: " + str(return_hist_sort[barisawal][4]))
                    print("Tanggal pengambilan: " + str(return_hist_sort[barisawal][2]))
                    print("Jumlah: " + str(return_hist_sort[barisawal][5]))
                    print("")
                v = 2
            elif (barishistory == 0):
                print("Belum ada barang yang dikembalikan")
                v = 2
    else:
        print("Anda tidak dapat mengakses riwayat pengembalian")