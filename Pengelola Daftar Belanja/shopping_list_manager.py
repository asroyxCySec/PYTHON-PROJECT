def display_menu():
    print("Pengelola Daftar Belanja")
    print("1. Tambah Item")
    print("2. Hapus Item")
    print("3. Lihat Daftar Belanja")
    print("4. Keluar")

def add_item(shopping_list):
    item = input("Masukkan nama item yang ingin ditambah: ")
    shopping_list.append(item)
    print(f"'{item}' telah ditambahkan ke daftar belanja.")

def remove_item(shopping_list):
    item = input("Masukkan nama item yang ingin dihapus: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' telah dihapus dari daftar belanja.")
    else:
        print(f"'{item}' tidak ditemukan dalam daftar belanja.")

def view_list(shopping_list):
    if shopping_list:
        print("Daftar Belanja:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Daftar belanja kosong.")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Keluar dari aplikasi. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
