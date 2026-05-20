import json 
import os

FILE_DATA = "data_buku.json"

def load_data():
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)

def tampilkan_buku(data):
    if len(data) == 0:
        print("Data buku kosong")
    else: 
        for i, buku in enumerate(data, start=1):
            print(f"{i}. {buku['judul']}")


def tambah_buku(data):
    judul = input("Judul Buku : ")
    penulis = input("Penulis : ")
    tahun = input("Tahun : ")

    buku = {
        "judul": judul, 
        "penulis": penulis, 
        "tahun" : tahun
    }

    data.append(buku)
    save_data(data)

def main():
    data = load_data()
    while True: 
        print("1. Tampilkan Buku")
        print("2. Tambah Buku")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_buku(data)

        elif pilihan == "2":
            tambah_buku(data)

        elif pilihan == "3":
            break

if __name__ == "__main__":
   main()