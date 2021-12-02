# Program Pencarian Gadget Berdasarkan Tahun Ditemukan

# Mencari gadget berdasarkan tahun ditemukan
# I.S. Menerima database gadget, input tahun, dan kategori pencarian (asumsi input valid)
# F.S. Mencetak hasil pencarian


# KAMUS 
# database : list of list
# tahun    : integer
# kategori : string
# found    : boolean 
# panjang  : integer


# FUNGSI DAN PROSEDUR

def cetakSearch(Id, database):
# Prosedur mencetak info gadget berdasarkan Id

# KAMUS LOKAL

# ALGORITMA
    print("Nama: ", database[Id][1])
    print("Deskripsi: ", database[Id][2]    )
    print("Jumlah: ", database[Id][3])
    print("Rarirty: ", database[Id][4])
    print("Tahun Ditemukan: ", database[Id][5])
    print("")


# PROGRAM UTAMA
def cariTahun(database):
    database = database[1:]     # Menghilangkan bagian awal list yang berisi [id, nama, ...]
    
    # Meminta input user
    tahun    = int(input("\nMasukkan tahun: "))
    kategori = input("Masukkan kategori: ")
    found    = False
    panjang  = len(database)

    print("\nHasil Pencarian :\n")

    # Pengeceakan dan pencetakan hasil pencarian
    if (kategori == "="):
        for i in range(panjang):
            if int(database[i][5]) == tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == ">"):
        for i in range(panjang):
            if int(database[i][5]) > tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == "<"):
        for i in range(panjang):
            if int(database[i][5]) < tahun:
                found = True
                cetakSearch(i, database)

    elif (kategori == ">="):
        for i in range(panjang):
            if int(database[i][5]) >= tahun:
                found = True
                cetakSearch(i, database)

    else: # kategori == "<="
        for i in range(panjang):
            if int(database[i][5]) <= tahun:
                found = True
                cetakSearch(i, database)
    
    # Hasil cetak bila tidak ditemukan gadget sesuai dengan kategori pencarian
    if not(found):
        print("Tidak ada gadget yang ditemukan")