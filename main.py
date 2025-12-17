from database.__init__ import create_tables
from utils.menu import tampilkan_menu

from controllers.kontrakan_controller import (
    tambah_kontrakan,
    lihat_kontrakan
)
from controllers.penyewa_controller import tambah_penyewa
from controllers.pembayaran_controller import tambah_pembayaran


# 🔥 BUAT TABEL SEKALI SAAT PROGRAM DIJALANKAN
create_tables()

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")

    # ===== MENU 1 =====
    if pilihan == "1":
        alamat = input("Alamat Kontrakan: ")
        harga = int(input("Harga: "))
        tambah_kontrakan(alamat, harga)
        print("Kontrakan berhasil ditambahkan")

    # ===== MENU 2 =====
    elif pilihan == "2":
        data = lihat_kontrakan()
        if len(data) == 0:
            print("Belum ada data kontrakan")
        else:
            print("\nDAFTAR KONTRAKAN")
            for k in data:
                print(f"ID: {k[0]} | Alamat: {k[1]} | Harga: {k[2]} | Status: {k[3]}")

    # ===== MENU 3 =====
    elif pilihan == "3":
        nama = input("Nama Penyewa: ")
        no_hp = input("No HP: ")
        tambah_penyewa(nama, no_hp)
        print("Penyewa berhasil ditambahkan")

    # ===== MENU 4 =====
    elif pilihan == "4":
        penyewa_id = input("ID Penyewa: ")
        kontrakan_id = input("ID Kontrakan: ")
        bulan = input("Bulan: ")
        jumlah = int(input("Jumlah Bayar: "))
        tambah_pembayaran(penyewa_id, kontrakan_id, bulan, jumlah)
        print("Pembayaran berhasil disimpan")

    # ===== KELUAR =====
    elif pilihan == "0":
        print("Keluar program")
        break

    else:
        print("Menu tidak tersedia")
