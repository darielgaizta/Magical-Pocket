# Modul berisi spesifikasi dan realisasi F01, F02, dan F03

# KAMUS
# db_user   = matriks user.csv
# db_gadget = matriks gadget.csv
# F01 : register
# F02 : login
# F03 : carirarity
# F16 : Help (tambahan)

def kapitalisasi(kata):
    # I.S. string yang dimasukkan berhuruf kecil
    # F.S. mengkapitalisasi setiap huruf awal
    idx = []
    listKata = list(kata)
    for i in range(len(listKata)):
        if listKata[i] == ' ':
            idx.append(i)
    for i in range(len(listKata)):
        if i in idx:
            kata = kata[0].capitalize() + kata[1:i+1] + kata[i+1].capitalize() + kata[i+2:]
    return kata

def convert(matriks,Str=False,Int=False):
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

def adding(csv,new_data):
    # I.S. diberikan data baru berupa list
    # F.S. data baru dimasukkan ke file csv dalam bentuk string
    with open(csv,'w') as file:
        for i in new_data:
            file.write(";".join(i)+"\n")

def register(path,db_user):
    # I.S. admin me-register-kan user baru
    # F.S. mengembalikan data user baru berupa list
    terdaftar = False
    nama = input("Masukkan nama: ")
    uname = input("Masukkan username: ")
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    nama = kapitalisasi(nama)
    for i in range(len(db_user)):
        if uname == db_user[i][1]:
            print("User {} sudah terdaftar, silakan login.".format(uname))
            terdaftar = True
            break
    if terdaftar == False:
        print("User {} telah berhasil register ke dalam Kantong Ajaib".format(uname))
        new_user = [id(uname),uname,nama,alamat,password,'User']
        db_user.append(new_user)
        adding(path,convert(db_user,Str=True))

def login(db_user):
    # I.S. input uname dan password
    # F.S. mengembalikan list yang mengandung logged_in
    logged_in = False
    uname = input("Masukkan username: ")
    password = input("Masukkan password: ")
    for i in range(len(db_user)):
        if db_user[i][1] == uname and db_user[i][4] == password:
            print("Halo {}, selamat datang di Kantong Ajaib!".format(uname))
            logged_in = True
            user = db_user[i]
            break
    if logged_in:
        # user = [id,uname,nama,alamat,password,role]
        return user
    else:
        print("Maaf, username dan password salah atau tidak ditemukan.")
        # logged_in = False
        return logged_in
 
def carirarity(db_gadget):
    # I.S. pengguna memasukkan rarity dari suatu gadget
    # F.S. menampilkan semua gadget sesuai rarity yang di-input
    rarity = input("Masukkan rarity: ")
    print('\n'+'='*10)
    print("Hasil pencarian:")
    for i in db_gadget:
        if i[4] == rarity:
            print("\nNama\t\t\t:",i[1])
            print("Deskripsi\t\t:",i[2])
            print("Jumlah\t\t\t:",int(i[3]))
            print("Rarity\t\t\t:",i[4],)
            print("Tahun ditemukan\t\t:",i[5])
    print('='*10)

def Help():
    print("\n=== COMMAND ===")
    print("register - mendaftarkan akun pengguna baru")
    print("login - melakukan log-in ke dalam sistem")
    print("carirarity - mengeluarkan gadget berdasarkan rarity")
    print("caritahun - mengeluarkan gadget berdasarkan tahun ditemukan")
    print("tambahitem - melakukan penambahan item")
    print("hapusitem - menghapus item")
    print("ubahjumlah - mengubah jumlah item yang ada")
    print("pinjam - meminjam gadget")
    print("kembalikan - mengembalikan gadget")
    print("minta - meminta consumable")
    print("riwayatpinjam - meilihat riwayat peminjaman gadget")
    print("riwayatkembali - melihat riwayat pengembalian gadget")
    print("riwayatambil - melihat riwayat pengambilan consumable")
    print("save - menyimpan perubahan data")
    print("exit - keluar dari program")

# db_user = matriks('user.csv') -> buat jaga-jaga
# db_gadget = matriks('gadget.csv') -> buat jaga-jaga