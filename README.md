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

## 3. Konsep Pemrograman yang Digunakan

### 3.1 Object Oriented Programming (OOP)
Program menggunakan **class** untuk merepresentasikan objek nyata.

Contoh:
- Kontrakan
- Penyewa
- Pembayaran

Contoh class:
```python
class Kontrakan:
    def __init__(self, id, alamat, harga, status):
        self.id = id
        self.alamat = alamat
        self.harga = harga
        self.status = status

## 4. Tujuan Pembuatan Aplikasi
Tujuan dibuatnya aplikasi ini adalah:
1. Menerapkan konsep **OOP** dalam Python
2. Menggunakan **module dan package**
3. Menerapkan **percabangan (if/elif/else)** dan **perulangan (while, for)**
4. Menghubungkan Python dengan **database SQLite**
5. Membuat aplikasi CRUD (Create, Read)
