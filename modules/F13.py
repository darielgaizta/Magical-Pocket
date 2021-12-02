# KAMUS

# tanggal : string
# db_consumable : variabel global dari load data / matriks consumable.csv
# db_consumable_history : variabel global dari load data / matriks consumable_history.csv
# db_user : variabel global dari load data / matriks user.csv
# riwayatambil() -> F13

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

def riwayatambil(db_consumable_history, db_user, db_consumable, user):
    # I.S. mengecek jika akun pengguna adalah admin
    # F.S. menampilkan sejarah consumable yang diambil semua pengguna, mulai dari yang paling baru
    #      (menampilkan 5 data pertama, jika diminta dapat menampilkan lebih banyak)
    if user[5]=="Admin":
        take_hist_sort=sort_tanggal(db_consumable_history)

        # mencari nama orang dari id peminjam
        for i in range(1, len(db_consumable_history)):
            for j in range(1, len(db_user)):
                if (take_hist_sort[i][1] == db_user[j][0]):
                    take_hist_sort[i][1] = db_user[j][2]
        # mencari nama consumbale dari id consumable
        for i in range(1, len(db_consumable_history)):
            for j in range(1, len(db_consumable)):
                if (take_hist_sort[i][2] == db_consumable[j][0]):
                    take_hist_sort[i][2] = db_consumable[j][1]

        barishistory = len(db_consumable_history) - 1
        barisawal = 1
        v = 1
        w = 1

        # mencetak hasil permintaan riwayatambil
        while (v < 2):
            if (barishistory > 5):
                while (w <= 5 and barisawal <= barishistory):
                    print("ID Peminjaman: " + str(take_hist_sort[barisawal][0]))
                    print("Nama Pengambil: " + str(take_hist_sort[barisawal][1]))
                    print("Nama Consumable: " + str(take_hist_sort[barisawal][2]))
                    print("Tanggal Peminjaman: " + str(take_hist_sort[barisawal][3]))
                    print("Jumlah: " + str(take_hist_sort[barisawal][4]))
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
                    print("ID Peminjaman: " + str(take_hist_sort[i][0]))
                    print("Nama Pengambil: " + str(take_hist_sort[i][1]))
                    print("Nama Consumable: " + str(take_hist_sort[i][2]))
                    print("Tanggal Peminjaman: " + str(take_hist_sort[i][3]))
                    print("Jumlah: " + str(take_hist_sort[i][4]))
                    print("")
                v = 2
            elif (barishistory == 0):
                print("Belum ada consumable yang diambil")
                v = 2
    else:
        print("Anda tidak dapat mengakses riwayat pengambilan")