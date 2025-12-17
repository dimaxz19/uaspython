# 🏠 Sistem Sewa Kontrakan  
Aplikasi Python + SQLite (CLI)

## 1. Deskripsi Proyek
Sistem Sewa Kontrakan adalah aplikasi berbasis **Command Line Interface (CLI)** yang dibuat menggunakan **Python** dan **database SQLite**.  
Aplikasi ini digunakan untuk mengelola data **kontrakan**, **penyewa**, dan **pembayaran sewa**.

| Screenshot | Screenshot |
|-----------|------------|
<img src="img/Screenshot 2025-12-17 225621.png" width="400"> | <img src="img/Screenshot 2025-12-17 225630.png" width="400"> |
| <img src="img/Screenshot 2025-12-17 225700.png" width="400"> | <img src="img/Screenshot 2025-12-17 225738.png" width="400"> |

Proyek ini dibuat untuk memenuhi tugas yang menerapkan konsep:
- Object Oriented Programming (OOP)
- Module dan Package Python
- Percabangan dan Perulangan
- Database SQLite (CRUD)

---

## 2. Fitur Aplikasi
Aplikasi memiliki fitur sebagai berikut:
1. Menambahkan data kontrakan
2. Menampilkan daftar kontrakan
3. Menambahkan data penyewa
4. Mencatat pembayaran sewa
5. Menyimpan data secara permanen menggunakan SQLite

---

## 3. Struktur Folder
Struktur folder pada project ini adalah:

sewa_kontrakan/
│
├── main.py # Program utama
│
├── database/
│ ├── init.py
│ ├── db_connection.py # Koneksi database SQLite
│ ├── init_db.py # Pembuatan tabel database
│ └── sewa_kontrakan.db # File database
│
├── controllers/
│ ├── init.py
│ ├── kontrakan_controller.py # Logika data kontrakan
│ ├── penyewa_controller.py # Logika data penyewa
│ └── pembayaran_controller.py# Logika data pembayaran
│
├── models/
│ ├── init.py
│ ├── kontrakan.py # Class Kontrakan
│ ├── penyewa.py # Class Penyewa
│ └── pembayaran.py # Class Pembayaran
│
├── utils/
│ ├── init.py
│ └── menu.py # Tampilan menu
│
└── README.md
