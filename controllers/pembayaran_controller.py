from database.db_connection import get_connection

def tambah_pembayaran(penyewa_id, kontrakan_id, bulan, jumlah):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pembayaran (penyewa_id, kontrakan_id, bulan, jumlah) VALUES (?, ?, ?, ?)",
        (penyewa_id, kontrakan_id, bulan, jumlah)
    )
    conn.commit()
    conn.close()
