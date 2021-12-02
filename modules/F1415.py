# F14 : load data
# F15 : save data

import time
import argparse
import os

def matriks(csv):
    # I.S. mengimport file csv
    # F.S. file csv dijadikan matriks
    with open(csv,'r') as file:
        line = [clean_line.replace('\n','') for clean_line in file.readlines()]
        array = []
        for i in range(len(line)):
            tempArr = []
            counter = 0
            string = line[i]
            length = len(line[i])
            for j in range(length):
                if j == length-1:
                    tempArr.append(string[counter:(j+1)])
                elif string[j] == ';':
                    tempArr.append(string[counter:j])
                    counter = j + 1
            array.append(tempArr)
    return array

def get_db():
	# F.S. mengembalikan list berisi matriks tiap csv
	list_db = []
	for (root,dirs,files) in os.walk(args.folder):
		for i in files:
			list_db.append(matriks(f"{args.folder}\\{i}"))
	return list_db

def get_files():
	# F.S. mengembalikan nama file (csv) dalam bentuk list
	for (root,dirs,files) in os.walk(args.folder):
		return files

def get_path(file_name):
	# I.S. memerlukan nama file csv sebagai argumen
	# F.S. mengembalikan nilai berupa lokasi file
	return f"{args.folder}\\{file_name}"

def save(files,db,directory):
	# I.S. diberikan matriks tiap database dalam list
	# F.S. setiap data disimpan dalam csv yang sesuai
	# db : matriks db dalam list
	# files : database / nama file (list)
	counter = 0
	for file in files:
		with open(f"{directory}\\{file}",'w') as f:
			for i in db[counter]:
				f.write(";".join(i)+"\n")
		counter += 1
	print('\nSaving',end='')
	for i in range(3):
		time.sleep(1)
		print('.',end='')
	print('\nDATA SAVED!\n')

def get_directory(directory):
	# I.S. pengguna memasukkan nama folder
	# F.S. mengembalikan nama folder (string)
	os.mkdir(directory)
	return directory

def check_directory(directory):
	# I.S. diberikan nama directory
	# F.S. akan dicek apakah directory sudah ada
	for i in os.listdir():
		if directory == i:
			return True
	return False

parser = argparse.ArgumentParser(description='nama folder')
parser.add_argument('folder', type=str, help='definisikan folder')
args = parser.parse_args()

if args.folder == "KantongAjaib":
	print("\nSelamat datang di Kantong Ajaib!")
else:
	print("Error: Folder not found.")
	exit()