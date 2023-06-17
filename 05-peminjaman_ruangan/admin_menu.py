import csv
import modul_pengguna
import pandas as pd
from tabulate import tabulate

def admin_menu():
    print("=== MENU ADMIN ===")
    print("1. Menghapus jadwal")
    print("2. Mengganti jadwal")
    print("0. Keluar")

    choice = input("Masukkan pilihan: ")
    if choice == "1":
        hapus_jadwal()
    elif choice == "2":
        ganti_jadwal()
    elif choice == "0":
        print("PROGRAM BERAKHIR")
    else:
        print("Pilihan tidak valid.")
        admin_menu()


def hapus_jadwal():
    print("=== HAPUS JADWAL ===")
    #menampilkan data pemesanan
    data = pd.read_csv('data_pemesanan.csv')
    print('=== DATA PEMESANAN ===')

    if len(data)== 0:
        print('[Data tidak tersedia]')
    else: 
        print()
        print(tabulate(data, headers =['Kode Pesanan', 'Nama', 'NIM', 'Sesi Kelas', 'Tanggal', 'Sesi Jam'],tablefmt='grid'))

    jadwal = input("Masukkan kode pemesanan jadwal yang akan dihapus: ")
    if modul_pengguna.cek_pemesanan_ada(jadwal):
    # kode untuk menghapus jadwal
        modul_pengguna.hapus_pesanan(jadwal)
        
    else: 
        print("KODE PESANAN TIDAK VALID")
        hapus_jadwal()


    

def ganti_jadwal():
    global jam
    print("=== GANTI JADWAL ===")
    #menampilkan data pemesanan
    print('=== DATA PEMESANAN ===')
    data = pd.read_csv('data_pemesanan.csv')
    if len(data)== 0:
        print('[Data tidak tersedia]')
    else: 
        print()
        print(tabulate(data, headers =['Kode Pesanan', 'Nama', 'NIM', 'Sesi Kelas', 'Tanggal', 'Sesi Jam'],tablefmt='grid'))

    jadwal_lama = input("Masukkan kodepesanan jadwal yang ingin diganti: ")
    if modul_pengguna.cek_pemesanan_ada(jadwal_lama):
        while(True):
            print("==Masukkan Jadwal Baru==")
            print("Daftar kelas: ")
            list_kelas = ["1303", "1304", "1209", "5401", "5402"]
            print("1. ", list_kelas[0])
            print("2. ", list_kelas[1])
            print("3. ", list_kelas[2])
            print("4. ", list_kelas[3])
            print("5. ", list_kelas[4])
            kelass=input("Pilih Kelas: ")
            if kelass not in ['1', '2', '3','4', '5']:
                print("Kelas tidak valid, mohon inputkan antara 1-5")
                continue
            else:    
                while True:
                    print(" ")
                    tanggal = input("Tanggal pemesanan (hh/bb/tttt): ")
                    print(" ")
                    try:
                        tanggal_split = tanggal.split("/")
                        if len(tanggal_split) != 3:
                            raise ValueError
                        hari = int(tanggal_split[0])
                        bulan = int(tanggal_split[1])
                        tahun = int(tanggal_split[2])
                        if len(tanggal_split[0]) != 2 or len(tanggal_split[1]) != 2 or len(tanggal_split[2]) != 4:
                            raise ValueError
                        tanggal_valid = True
                    except (ValueError, IndexError):
                                
                        print("\n=== Format tanggal tidak sesuai. Harap gunakan format dd/mm/tttt. ===\n")
                              
                        tanggal_valid = False

                    if tanggal_valid:
                        while(True):
                                    
                            print("Daftar jam pemakaian: ")
                            list_jam = ["07.30 - 09.15", "09.20 - 12.00", "13.00 - 14.45", "14.50 - 16.35"]
                            print("1. ", list_jam[0])
                            print("2. ", list_jam[1])
                            print("3. ", list_jam[2])
                            print("4. ", list_jam[3])
                            jam = input("Pilih jam (dalam nomor 1-4 sesuai daftar): ")
                            if jam not in ['1', '2', '3','4']:
                                        
                                print("\n=== Nomor jam tidak valid, mohon inputkan antara 1-4 ===\n")
                                        
                                continue
                            else:
                                modul_pengguna.ubah_pesanan(jadwal_lama, kelass, tanggal, jam)
                                print("Jadwal berhasil di ganti")
                                
                                admin_menu()
                                break
                        break
            break
                    
            
    else: 
        print("KODE PESANAN TIDAK VALID")
        ganti_jadwal()
    # jadwal_baru = input("Masukkan jadwal baru: ")
    # kode untuk mengganti jadwal
    