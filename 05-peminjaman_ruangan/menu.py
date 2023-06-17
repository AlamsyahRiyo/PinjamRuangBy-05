from ast import main
import csv
import modul_pengguna
from colorama import Fore

def menu():
    print("selamat datang di menu utama")
    list_Menu = ["Pemesanan Ruangan", "Panduan Reschedule", "Customer Service"]
    print("1. ", list_Menu[0])
    print("2. ", list_Menu[1])
    print("3. ", list_Menu[2])
    print("="*50)
    print(" ")

    while (True):
        menu=input("Pilih menu:  ")
        if menu == "1":
                nama=input("Nama: ")
                NIM =input("Nomor NIM: ")
                while(True):
                    print(" ")
                    print("Daftar kelas: ")
                    list_kelas = ["1303", "1304", "1209", "5401", "5402"]
                    print("1. ", list_kelas[0])
                    print("2. ", list_kelas[1])
                    print("3. ", list_kelas[2])
                    print("4. ", list_kelas[3])
                    print("5. ", list_kelas[4])
                    
                    kelass=input("Pilih Kelas: ")
                    if kelass == "1":
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
                                    jam=input("Pilih jam (dalam nomor 1-4 sesuai daftar): ")
                                    if jam not in ['1', '2', '3','4']:
                                        
                                        print("\n=== Nomor jam tidak valid, mohon inputkan antara 1-4 ===\n")
                                        
                                        continue
                                    else:
                                        print(" ")
                                        modul_pengguna.simpan_pesanan(nama, NIM, kelass, tanggal, jam)
                                        print("=== Jadwal berhasil di booking, silahkan lanjut! ===")
                                        break
                                break
                            else:
                                continue

                    elif kelass=="2":
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
                                
                                print("\n===Format tanggal tidak sesuai. Harap gunakan format dd/mm/tttt.===\n")
                                
                                tanggal_valid = False

                            if tanggal_valid:
                                while(True):
                                    
                                    
                                    print("Daftar jam pemakaian: ")
                                    list_jam = ["07.30 - 09.15", "09.20 - 12.00", "13.00 - 14.45", "14.50 - 16.35"]
                                    print("1. ", list_jam[0])
                                    print("2. ", list_jam[1])
                                    print("3. ", list_jam[2])
                                    print("4. ", list_jam[3])
                                    jam=input("Pilih jam (dalam nomor 1-4 sesuai daftar): ")
                                    if jam not in ['1', '2', '3','4']:
                                        
                                        print("\n=== Nomor jam tidak valid, mohon inputkan antara 1-4 ===\n")
                                        
                                        continue
                                    else:
                                        print(" ")
                                        modul_pengguna.simpan_pesanan(nama, NIM, kelass, tanggal, jam)
                                        print("=== Jadwal berhasil di booking, silahkan lanjut! ===")
                                        break
                                break
                            else:
                                continue

                    elif kelass=="3":
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
                                    jam=input("Pilih jam (dalam nomor 1-4 sesuai daftar): ")
                                    if jam not in ['1', '2', '3','4']:
                                        
                                        print("\n=== Nomor jam tidak valid, mohon inputkan antara 1-4 ===\n")
                                        
                                        continue
                                    else:
                                        print(" ")
                                        modul_pengguna.simpan_pesanan(nama, NIM, kelass, tanggal, jam)
                                        print("=== Jadwal berhasil di booking, silahkan lanjut! ===")
                                        break
                                break
                            else:
                                continue
                    elif kelass=="4":
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
                                    jam=input("Pilih jam (dalam nomor 1-4 sesuai daftar): ")
                                    if jam not in ['1', '2', '3','4']:
                                        
                                        print("\n=== Nomor jam tidak valid, mohon inputkan antara 1-4 ===\n")
                                        
                                        continue
                                    else:
                                        print(" ")
                                        modul_pengguna.simpan_pesanan(nama, NIM, kelass, tanggal, jam)
                                        print("=== Jadwal berhasil di booking, silahkan lanjut! ===")
                                        break
                                break
                            else:
                                continue

                    elif kelass=="5":
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
                                    jam=input("Pilih jam (dalam nomor 1-4 sesuai daftar): ")
                                    if jam not in ['1', '2', '3','4']:
                                        
                                        print("\n=== Nomor jam tidak valid, mohon inputkan antara 1-4 ===\n")
                                        
                                        continue
                                    else:
                                        print(" ")
                                        modul_pengguna.simpan_pesanan(nama, NIM, kelass, tanggal, jam)
                                        print("=== Jadwal berhasil di booking, silahkan lanjut! ===")
                                        break
                                break

                            else:
                                continue

                    else:
                        
                        print("\n=== Nomor kelas tidak valid, mohon inputkan nomor kelas yang tersedia 1/2/3/4/5! ===\n")
                        
                        
                        continue
                    kodepesanan = tanggal.replace('/', '') + kelass + jam
                    
                    print(Fore.LIGHTBLUE_EX + f'''
                    ======= STRUCK BUKTI PEMINJAMAN =======
                    Pesanan atas identitas :
                    Nama            : {nama}
                    NIM             : {NIM}
                    Kelas           : {kelass}
                    Sesi Jam        : {jam}
                    Tanggal         : {tanggal}
                    Kode Pesanan    : {kodepesanan}
                    ========== BERHASIL DIPESAN ===========
                
                        ''')
                    print("Silahkan menggunakan ruang kelas sesuai kelas yang  anda pesan.")
                    print("Terimakasih atas kepercayaan  Anda \n")
                    
                    while(True):
                        o = input("Apakah Anda ingin menghentikan program? (y/n): ")
                        if o=='y' or o == 'Y':
                            print("PROGAM BERAKHIR")
                            exit()
                        elif o=='n' or o == 'N':
                            print("selamat datang di menu utama")
                            list_Menu = ["Pemesanan Ruangan", "Panduan Reschedule", "Customer Service"]
                            print("1. ", list_Menu[0])
                            print("2. ", list_Menu[1])
                            print("3. ", list_Menu[2])
                            print("=====================================")
                            break
                        else:
                            print("PILIHAN TIDAK VALID")
                            continue
                    break
                        
                    
                    
                    

        elif menu=="2":
            print("Panduan reschedule ruang kelas:")
            print("1. Isi formulir reschdule disertai keterangan reschecule ruang kelas")
            print("2. Sertakan bukti pemesanan")
            print("3. Kirimkan kepada nomor customer service yang tersedia")
            print("")
            print("Terimakasih!")
            while(True):
                ulang=input("Kembali ke menu utama ?(y/n): ")
                if ulang=='y' or ulang == 'Y':
                    print("selamat datang di menu utama")
                    list_Menu = ["Pemesanan Ruangan", "Panduan Reschedule", "Customer Service"]
                    print("1. ", list_Menu[0])
                    print("2. ", list_Menu[1])
                    print("3. ", list_Menu[2])
                    print("=====================================")
                    break
                if ulang == 'n' or ulang == 'N':
                    return
                else:
                    print("PILIHAN TIDAK VALID")
                    continue
            
            
            
            
        
        elif menu=="3":
            print("Mohon hubungi kontak kami apabila ada kendala dan meminta bantuan.")
            listCS = ["(0271)714039", "121 / (021)121", "08.00-17.00"]
            print("Office phone : ", listCS[0])
            print("Contact center : ", listCS[1])
            print("Jam pelayanan : ", listCS[2])
            print("")
            print("Terima kasih")
            while(True):
                ulang=input("Kembali ke menu utama ?(y/n): ")
                if ulang=='y' or ulang == 'Y':
                    print("selamat datang di menu utama")
                    list_Menu = ["Pemesanan Ruangan", "Panduan Reschedule", "Customer Service"]
                    print("1. ", list_Menu[0])
                    print("2. ", list_Menu[1])
                    print("3. ", list_Menu[2])
                    print("=====================================")
                    break
                if ulang == 'n' or ulang == 'N':
                    return
                else:
                    print("PILIHAN TIDAK VALID")
                    continue
        else:
            print("Menu tidak valid, pilih menu 1-3!")
            while(True):
                ulang=input("Kembali ke menu utama ?(y/n): ")
                if ulang=='y' or ulang == 'Y':
                    print("selamat datang di menu utama")
                    list_Menu = ["Pemesanan Ruangan", "Panduan Reschedule", "Customer Service"]
                    print("1. ", list_Menu[0])
                    print("2. ", list_Menu[1])
                    print("3. ", list_Menu[2])
                    print("=====================================")
                    break
                if ulang == 'n' or ulang == 'N':
                    return
                else:
                    print("PILIHAN TIDAK VALID")
                    continue
pass
