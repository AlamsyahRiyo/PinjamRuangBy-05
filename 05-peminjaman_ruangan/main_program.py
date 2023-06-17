import os
os.system ("cls")
import modul_pengguna
import modul_admin
import colorama
import admin_menu
from colorama import Fore, Back, Style

colorama.init()

print(Back.BLACK)
print(Style.NORMAL)

print(Fore.LIGHTBLACK_EX + "Sekertariat Teknik Industri UNS ")
print("Alamat: Jalan Ir Sutami No 36-A Kentingan Surakarta. Kode Pos, 57126. Telp, (0271) 646994. Fax, (0271) 646655,")
print("")
print("Selamat datang di program PINJAMRUANG, Silahkan pilih menu untuk melanjutkan")

def main():
    print((Fore.BLUE)+"1. User")
    print((Fore.MAGENTA)+"2. Admin")
    print((Fore.GREEN)+"0. Keluar")
    print((Fore.MAGENTA)+"Masukkan pilihan: ")
    choice = input()
    if choice == "1":
        while(True):
            print((Fore.BLUE+"Apakah Anda sudah memiliki akun? (y/n): "))
            user_choice = input()
            if user_choice == "n":
                print(Fore.BLUE+"=== REGISTER ===")
                username = input("Masukkan username baru: ")
                password = input("Masukkan password baru: ")
                # modul_pengguna.register(username, password)
                modul_pengguna.simpan_data(username, password)

                print("Pendaftaran berhasil!")
                print(Fore.BLUE+"=== LOGIN ===")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")

                modul_pengguna.cek_pengguna(username, password)
                main()

            elif user_choice == "y":
                print(Fore.BLUE+ "=== LOGIN ===")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")

                modul_pengguna.cek_pengguna(username, password)
                main()
            else:
                print("Pilihan tidak valid!")
                continue
    elif choice == "2":
            print("=== LOGIN SEBAGAI ADMIN ===")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            modul_admin.cek_admin(username, password)
            main()
            
    elif choice == "0":
        print("PROGRAM BERAKHIR.")
        exit()
    else:
        print("Pilihan tidak valid.")
        main()

if __name__ == "__main__":
    main()

