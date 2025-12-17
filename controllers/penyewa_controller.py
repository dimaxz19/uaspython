from database.db_connection import get_connection

def tambah_penyewa(nama, no_hp):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO penyewa (nama, no_hp) VALUES (?, ?)",
        (nama, no_hp)
    )
    conn.commit()
    conn.close()
