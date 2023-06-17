import csv
from admin_menu import admin_menu
from menu import menu


def login(username, password):
    with open('data_admin.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(list(row))
            if row[0] == username and row[1] == password:
                return True
    return False

def cek_admin(username, password):
    if login(username, password):
        print("Login berhasil!")
        # Panggil fungsi menu di sini
        admin_menu()
    else:
        print("Login gagal!")
        