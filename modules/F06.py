# Program Menghapus Item

# I.S. Menerima input ID barang yang akan dibuang (diperiksa apakah barang itu ada)
# F.S. Item dibuang dari database / pesan error jika input ID tidak ada / tidak ada yang terjadi bila proses di cancel


# KAMUS 
# databaseG : list of list
# databaseC : list of list
"""Ganti berdasarkan datatype"""
# ID : string


# FUNGSI DAN PROSEDUR

def searchDatabase(ID, database):
# Fungsi yang memeriksa apakah sebuah Id ada di dalam database

# KAMUS LOKAL
# found : boolean

# ALGORITMA
    found = False   # Variable yang menyimpan apakah ID ada di database

    for i in database:

        if i[0] == ID:
            found = True
            break

    return found


def getIndex(ID, database):
# Fungsi mendapatkan index suatu item di database berdasarkan ID (asumsi ID memang ada di database)

# KAMUS LOKAL

# ALGORITMA
    for i in range(len(database)):
        if database[i][0] == ID:
            return i


def removeDatabase(ID, database):
# Prosedur yang dijalankan program setelah validasi (asumsi ID memang ada di database)

# KAMUS LOKAL
# index : integer

# confirmation : string
# temp: list of list
    """Ganti datatype"""
# ALGORITMA
    index = getIndex(ID, database)  # Index dari item

    while True:     # Proses konfirmasi penghapusan
        confirmation = input("Apakah anda yakin ingin menghapus " + database[index][1] + " (Y/N)? ")
        
        if (confirmation == "N"):   # Jika user tidak jadi menghapus
            print("\nPenghapusan dibatalkan.")
            break

        elif (confirmation == "Y"): # Jika user jadi menghapus

            # Kode penghapusan dengan index 
            temp = database[:index] 
            for i in database[(index + 1):]:
                temp.append(i)
            database = temp

            print("\nItem telah berhasil dihapus dari database")
            break
        
        else:   # Inpput tidak valid. Pesan error dan input diulang
            print("\nInput tidak valid. Masukkan lagi!")
    
    return database


# PROGRAM UTAMA
def hapusItem(databaseG, databaseC):

    # Input ID
    ID = input("Masukan ID: ")
    
    # Pengecekan ID ada di database
    if not(searchDatabase(ID, databaseG)) and not(searchDatabase(ID, databaseC)):    # Bila ID tidak ada di kedua database
        print("\nTidak ada item dengan ID tersebut")

    else:
        if ID[0] == "G":    # Jika item gadget
            databaseG = removeDatabase(ID, databaseG)

        else:               # Jika item consumable
            databaseC = removeDatabase(ID, databaseC)

    return (databaseG, databaseC)