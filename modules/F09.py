def mencari_data_gadget(id,full_data_gadget):
# I.S. : id gadget dan matriks gadget
# F.S. : array data yang berisi nama gadget tersebut
    data = []
    for i in full_data_gadget:
        if (id == i[0]):
            data.append(i[1])
            return data #[nama barang]

def data_dan_tampilan_awal(id_user,full_data_borrow,full_data_gadget):
# I.S. : id user, matriks peminjaman,, dan matriks gadget
# F.S. : menampilkan barang yang dipinjam dan data setiap barang tersebut
    nomor = 1
    data_pinjam = []
    for i in range(len(full_data_borrow)):
        if full_data_borrow[i][5] == "False" and id_user == full_data_borrow[i][1]:
            gadget = mencari_data_gadget(full_data_borrow[i][2], full_data_gadget)
            if gadget != None:
                gadget.append(full_data_borrow[i][4])
                gadget.append(full_data_borrow[i][0])
                gadget.append(full_data_borrow[i][2])
                data_pinjam.append(gadget)
                print(str(nomor) + ". " + gadget[0])
                nomor += 1
    if nomor == 1:
        is_ada_pinjaman = False
    else:
        is_ada_pinjaman = True
    return data_pinjam, is_ada_pinjaman

def input_tanggal_valid():
# I.S. : menerima masukan tanggal
# F.S. : tanggal yang sudah divalidasi
    tgl_tidak_valid = True
    while(tgl_tidak_valid):
        idx = 0
        tgl_pinjam  = input("Tanggal peminjaman: ")
        raw_tgl = ["" for i in range(3)]
        for i in tgl_pinjam:
            if i != "/" :
                raw_tgl[idx] += i
            else:
                idx += 1
                continue
        if idx == 2:
            raw_tgl = [int(i) for i in raw_tgl]
            if (raw_tgl[2] % 400 == 0) or ((raw_tgl[2] % 100 != 0) and (raw_tgl[2] % 4 == 0)):
                if (raw_tgl[1] == 1) or (raw_tgl[1] == 3) or (raw_tgl[1] == 5) or (raw_tgl[1] == 7) or (raw_tgl[1] == 8) or (raw_tgl[1] == 9) or (raw_tgl[1] == 11):
                    if (1 <= raw_tgl[0] <= 31):
                        tgl_tidak_valid = False
                elif raw_tgl[1] == 2 :
                    if (1 <= raw_tgl[0] <= 29):
                        tgl_tidak_valid = False
                else:
                    if (1 <= raw_tgl[0] <= 30):
                        tgl_tidak_valid = False
            else:
                if (raw_tgl[1] == 1) or (raw_tgl[1] == 3) or (raw_tgl[1] == 5) or (raw_tgl[1] == 7) or (raw_tgl[1] == 8) or (raw_tgl[1] == 9) or (raw_tgl[1] == 11):
                    if (1 <= raw_tgl[0] <= 31):
                        tgl_tidak_valid = False
                elif raw_tgl[1] == 2 :
                    if (1 <= raw_tgl[0] <= 28):
                        tgl_tidak_valid = False
                else:
                    if (1 <= raw_tgl[0] <= 30):
                        tgl_tidak_valid = False
            
            if (tgl_tidak_valid == True ):
                print("Tanggal tidak valid! Ulangi")
        else:
            print("Tanggal berbentuk dd/mm/yyyy")
    return tgl_pinjam

def masukan_nomor_pinjam(data_pinjam):
# I.S : data nama gadget dan menerima input masukan pilihan
# F.S : nomor pilihan yang valid dari peminjaman
    input_nomor_tidak_valid = True
    while(input_nomor_tidak_valid):
        nomor_pinjam = int(input("Masukkan nomor peminjaman: "))
        if (0 < nomor_pinjam < len(data_pinjam)+1):
            input_nomor_tidak_valid = False
        else:
            print("Input tidak valid. Ulangi!")
    return nomor_pinjam

def jumlah_pengembalian(full_data_borrow, full_data_return,id_user, data_pinjam, nomor_pinjam):
# I.S. : matriks peminjaman, matriks pengembalian, id user, data pinjam dan nomor pinjam yang dipilih
# F.S. : jumlah pengembalian yang telah divalidasi
    notValid = True
    while(notValid):
        jumlahPinjam = 0
        for i in full_data_borrow:
            if (i[1] == id_user and i[2] == data_pinjam[nomor_pinjam-1][3]):
                jumlahPinjam += int(i[4])

        telahKembali = 0
        for i in full_data_return:
            if (i[3] == id_user and i[4] == data_pinjam[nomor_pinjam-1][3]):
                telahKembali += int(i[5])
        
        sisaPinjam = jumlahPinjam-telahKembali

        jumlah_kembali = int(input("Masukkan jumlah pengembalian: "))
        if jumlah_kembali <= sisaPinjam:
            sisaPinjam -= jumlah_kembali
            notValid = False
        else:
            print("Jumlah pengembalian tidak sesuai.")
    return jumlah_kembali, sisaPinjam


def mengembalikan_gadget(id_user, full_data_borrow, full_data_gadget, full_data_return):
# I.S. : id user, matriks peminjaman, matriks gadget, dan matriks pengembalian
# F.S. : menambahkan array baru di matriks peminjaman
    data_pinjam, is_ada_pinjaman = data_dan_tampilan_awal(id_user,full_data_borrow,full_data_gadget)
    if (is_ada_pinjaman):
        nomor_pinjam = masukan_nomor_pinjam(data_pinjam)
        tgl_kembali = input_tanggal_valid()
        jumlah_kembali, sisaPinjam = jumlah_pengembalian(full_data_borrow, full_data_return, id_user, data_pinjam, nomor_pinjam)

        print("\n" + "Item " + data_pinjam[nomor_pinjam-1][0] + " (x" + str(jumlah_kembali) + ") telah dikembalikan.")

        for i in range(1, len(full_data_gadget)):
            if full_data_gadget[i][1] == data_pinjam[nomor_pinjam-1][0]:
                full_data_gadget[i][3] = int(full_data_gadget[i][3]) + jumlah_kembali
        if(sisaPinjam == 0):
            for i in full_data_borrow:
                if i[0] == data_pinjam[nomor_pinjam-1][2]:
                    i[5] = "True"

        new_return = ["R" + str(len(full_data_return)), data_pinjam[nomor_pinjam-1][2], tgl_kembali, str(id_user), data_pinjam[nomor_pinjam-1][3], jumlah_kembali]
        full_data_return.append(new_return)
    else:
        print("\n Anda tidak memiliki pinjaman barang.")

"""Untuk keperluan bonus ditambahkan field baru di gadget_return_history.csv, 
   yaitu jumlah_pengembalian, id_gadget, dan id_user. id_gadget dan id_user ditambahkan
   untuk keperluan validasi jumlah pengembalian dan keterangan isReturned di gadget_borrow_history."""