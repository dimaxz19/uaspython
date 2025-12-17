from database.db_connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kontrakan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alamat TEXT NOT NULL,
        harga INTEGER NOT NULL,
        status TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS penyewa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        no_hp TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pembayaran (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        penyewa_id INTEGER,
        kontrakan_id INTEGER,
        bulan TEXT,
        jumlah INTEGER
    )
    """)

    conn.commit()
    conn.close()
