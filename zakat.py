# Fungsi untuk menambahkan transaksi zakat (beras yang didistribusikan)
def add_transaksi_zakat(id_zakat, id_beras, jumlah_beras, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Menghitung total harga beras
    query_beras = "SELECT harga_per_kg FROM master_beras WHERE id = %s"
    cursor.execute(query_beras, (id_beras,))
    harga_per_kg = cursor.fetchone()[0]
    
    total_harga = harga_per_kg * jumlah_beras
    
    query = """INSERT INTO transaksi_zakat (id_zakat, id_beras, jumlah_beras, total_harga, tanggal) 
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (id_zakat, id_beras, jumlah_beras, total_harga, tanggal))
    
    conn.commit()
    cursor.close()
    conn.close()
