# Program Inventarisasi Barang-Barang Doremonangis

# KAMUS
# files = list nama file (csv)
# db = matriks dari tiap isi file (csv)
# command, action, path = string
# save_last_changes = character

from modules import *

files = get_files()
db = get_db()

# index db dan files:
# [0] consumable.csv
# [1] consumable_history.csv
# [2] gadget.csv
# [3] gadget_borrow_history.csv
# [4] gadget_return_history.csv
# [5] user.csv

db_consumable = convert(db[0], Int=True)
db_consumable_history = convert(db[1], Int=True)
db_gadget = convert(db[2], Int=True)
db_gadget_borrow_history = convert(db[3], Int=True)
db_gadget_return_history = convert(db[4], Int=True)
db_user = convert(db[5], Int=True)

# PROGRAM UTAMA

while 1:
	command = input('>>> ')
	if command == 'login':								# F02
		user = login(db_user)
		while user != False:
			action = input('>>> ')
			if action == 'register' and user[5] == 'Admin':			# F01 (Admin only)
				path = get_path('user.csv')
				register(path,db_user)
			elif action == 'carirarity':					# F03
				carirarity(db_gadget)
			elif action == 'caritahun':					# F04
				cariTahun(db_gadget)
			elif action == 'tambahitem' and user[5] == "Admin":		# F05 (Admin only)
				db_gadget, db_consumable = tambahItem(db_gadget, db_consumable)
			elif action == 'hapusitem' and user[5] == "Admin":		# F06 (Admin only)
				db_gadget, db_consumable = hapusItem(db_gadget, db_consumable)
			elif action == 'ubahjumlah' and user[5] == "Admin":		# F07 (Admin only)
				ubah_jumlah(db_gadget, db_consumable)
			elif action == 'pinjam' and user[5] == "User":			# F08 (User only)
				meminjam_gadget(user[0],db_gadget_borrow_history, db_gadget)
			elif action == 'kembalikan' and user[5] == "User":		# F09 (User only)
				mengembalikan_gadget(user[0], db_gadget_borrow_history, db_gadget, db_gadget_return_history)
			elif action == 'minta' and user[5] == "User":			# F10 (User only)
				hasil_minta = minta(db_consumable, db_consumable_history, user)
				if hasil_minta:
					db_consumable_history = hasil_minta[1]
			elif action == 'riwayatpinjam' and user[5] == "Admin":		# F11 (Admin only)
				riwayatpinjam(db_gadget_borrow_history, db_user, db_gadget, user)
			elif action == 'riwayatkembali' and user[5] == "Admin":		# F12 (Admin only)
				riwayatkembali(db_gadget_return_history, db_user, db_gadget, user)
			elif action == 'riwayatambil' and user [5] == "Admin":		# F13 (Admin only)
				riwayatambil(db_consumable_history,db_user, db_consumable, user)
			elif action == 'save':						# F15
				db[0] = convert(db_consumable,Str=True)
				db[1] = convert(db_consumable_history,Str=True)
				db[2] = convert(db_gadget,Str=True)
				db[3] = convert(db_gadget_borrow_history,Str=True)
				db[4] = convert(db_gadget_return_history,Str=True)
				db[5] = convert(db_user,Str=True)
				directory = input("Masukkan nama folder penyimpanan: ")
				if check_directory(directory):
					save(files,db,directory)
				else:
					save(files,db,get_directory(directory))
			elif action == 'Help':						# F16
				Help()
			elif action == 'exit':						# F17
				while 1:
					save_last_changes = input("Ingin menyimpan perubahan (Y/N): ")
					save_last_changes = save_last_changes.capitalize()
					if save_last_changes == 'Y':
						db[0] = convert(db_consumable,Str=True)
						db[1] = convert(db_consumable_history,Str=True)
						db[2] = convert(db_gadget,Str=True)
						db[3] = convert(db_gadget_borrow_history,Str=True)
						db[4] = convert(db_gadget_return_history,Str=True)
						db[5] = convert(db_user,Str=True)
						directory = input("Masukkan nama folder penyimpanan: ")
						if check_directory(directory):
							save(files,db,directory)
						else:
							save(files,db,get_directory(directory))
						break
					elif save_last_changes == 'N':
						break
					else:
						print("Error: Wrong input.")
				exit()
			else:
				print("Error: Command not found.")
	elif command == 'Help':
		Help()
		print('\nSilakan ketik "login" untuk memulai.')
	elif command == 'exit':
		exit()
	else:
		print("Error: Command not found.")
		print('\nKetik "Help" untuk melihat command yang tersedia! ')