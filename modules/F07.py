#F07

#Kamus
# db_gadget = matriks dari gadget.csv
# db_consumable = matriks dari consumables.csv

def modify_data(matriks, idx, col, value):
# I.S. : Matriks, indeks, kolom, serta nilai akhir dari data yang ingin diubah
# F.S  : Data pada matriks telah diubah 
    matriks[idx][col] = value

def input_perubahan(jumlah):
# I.S. : jumlah awal dari barang
# F.S. : membuat variabel baru jumlah perubahan dan apakah valid
    jumlah_ubah = int(input("Masukkan Jumlah: "))
    if int(jumlah) + jumlah_ubah >= 0:
        jumlah_tidak_valid = False
    else:
        jumlah_tidak_valid = True
    return jumlah_ubah, jumlah_tidak_valid

def proses_perubahan(matriks, id_barang):
# I.S. : matriks yang ingin diubah dan id barang 
# F.S. : mengeluarkan kevalidan id dan mencetak pernyataan jumlah barang telah diubah atau tidak 
    idx_barang = ""
    for i in range(len(matriks)):
        if id_barang == matriks[i][0]:
            jumlah_barang = matriks[i][3]
            idx_barang  = i
    id_tidak_valid = True      #digunakan untuk mengecek kevalidan masukan id
    if idx_barang != "":
        id_tidak_valid = False
    
    if (id_tidak_valid == False): #jika id valid program ini akan dilanjutkan
        jumlah_ubah, jumlah_tidak_valid = input_perubahan(jumlah_barang)
        for i in matriks:
            if i[0] == id_barang:
                nama_barang = i[1]
        if jumlah_tidak_valid == True:
            print("\n" + str(abs(jumlah_ubah)) + " " + nama_barang + "gagal dibuang karena stok kurang. Stok sekarang: " + str(jumlah_barang) + "(<" + str(abs(jumlah_ubah))+ ")")
        else:
            jumlah_barang = int(jumlah_barang) + jumlah_ubah
            modify_data(matriks, idx_barang, 3, jumlah_barang)
            if jumlah_ubah >= 0:
                print("\n" + str(abs(jumlah_ubah)) + " " + nama_barang + " berhasil ditambahkan. Stok sekarang: " + str(jumlah_barang))
            else:
                print("\n" + str(abs(jumlah_ubah)) + " " + nama_barang + " berhasil dibuang. Stok sekarang: " + str(jumlah_barang))
    return id_tidak_valid

def ubah_jumlah(full_data_gadget, full_data_consum):
# I.S. : matriks gadget dan consumables
# F.S. : matriks telah diubah
    id_barang = input("Masukkan ID item: ")
    if id_barang[0] == "G":
        id_tidak_valid = proses_perubahan(full_data_gadget, id_barang)
    elif id_barang[0] == "C":
        id_tidak_valid = proses_perubahan(full_data_consum, id_barang)
    else:
        id_tidak_valid = True
    if id_tidak_valid != False:
        print("Tidak ada item dengan id tersebut")