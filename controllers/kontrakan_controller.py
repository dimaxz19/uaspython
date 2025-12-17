from database.db_connection import get_connection

def tambah_kontrakan(alamat, harga):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO kontrakan (alamat, harga, status) VALUES (?, ?, ?)",
        (alamat, harga, "Kosong")
    )
    conn.commit()
    conn.close()

def lihat_kontrakan():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM kontrakan")
    data = cursor.fetchall()

    conn.close()
    return data
