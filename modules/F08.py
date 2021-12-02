# F08

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

def input_item(id_user, full_data_gadget, full_data_borrow):
# I.S. : id user dan matriks gadget serta riwayat peminjaman
# F.S. : data dari barang yang dipinjam
    id_tidak_valid = True
    data_pinjam = []
    while(id_tidak_valid):
        id_kembar = False
        id_barang = input("Masukkan ID item: ")
        if len(full_data_borrow) == 1 :
            for i in full_data_borrow:
                if ((id_barang == i[2]) and (id_user == i[1]) and i[5] == "False"):
                    print("Barang sedang dipinjam. Pinjam barang lainnya.")
                    id_tidak_valid = True
                    id_kembar = True
        if id_kembar == False :
            for i in range(len(full_data_gadget)):
                if id_barang == full_data_gadget[i][0]:
                    data_pinjam.append(id_barang)
                    data_pinjam.append(full_data_gadget[i][1])
                    data_pinjam.append(full_data_gadget[i][3])
                    data_pinjam.append(i)
                    id_tidak_valid = False
        if (id_tidak_valid and id_kembar == False):
            print("ID tidak valid! Ulangi masukan!")
    return data_pinjam #[id barang, nama barang, jumlah barang, index]

def input_jumlah_peminjaman(data_pinjam,full_data_gadget):
# I.S. : data dari barang yang dipinjam dan matriks gadget
# F.S. : jumlah peminjaman yang valid
    jumlah_tidak_valid = True
    while(jumlah_tidak_valid):
        jumlah_pinjam = int(input("Jumlah peminjaman: "))
        if data_pinjam[2] >= jumlah_pinjam:
            data_pinjam[2] -= jumlah_pinjam
            full_data_gadget[data_pinjam[3]][3] = data_pinjam[2]
            jumlah_tidak_valid = False
        else:
            print("Jumlah barang yang anda masukkan tidak sesuai. Ulangi!")
    return jumlah_pinjam

def meminjam_gadget(id_user, full_data_borrow, full_data_gadget):
# I.S. id user, matriks peminjaman, dan matriks gadget
# F.S. menambahkan array baru ke matriks peminjaman
    data_pinjam = input_item(id_user, full_data_gadget,full_data_borrow)
    tgl_pinjam = input_tanggal_valid()
    jumlah_pinjam = input_jumlah_peminjaman(data_pinjam, full_data_gadget)

    print("\n"+"Item " + data_pinjam[1] + " (x" + str(jumlah_pinjam) +") berhasil dipinjam!")
    new_borrow  = ["B" + str(len(full_data_borrow)), id_user, data_pinjam[0], tgl_pinjam, jumlah_pinjam, "False"]
    full_data_borrow.append(new_borrow)