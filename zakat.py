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

# Fungsi untuk menampilkan transaksi zakat
def view_transaksi_zakat():
    conn = create_connection()
    cursor = conn.cursor()
    
    query = """SELECT tz.id, z.nama, z.jenis_zakat, m.nama_beras, tz.jumlah_beras, tz.total_harga, tz.tanggal
               FROM transaksi_zakat tz
               JOIN zakat_data z ON tz.id_zakat = z.id
               JOIN master_beras m ON tz.id_beras = m.id"""
    cursor.execute(query)
    result = cursor.fetchall()
    
    for row in result:
        print(f"ID Transaksi: {row[0]}, Nama Zakat: {row[1]}, Jenis Zakat: {row[2]}, Nama Beras: {row[3]}, "
              f"Jumlah Beras: {row[4]}, Total Harga: {row[5]}, Tanggal: {row[6]}")
    
    cursor.close()
    conn.close()

    # Fungsi untuk mengekspor data zakat ke Excel
def export_to_excel():
    conn = create_connection()
    query = "SELECT * FROM zakat_data"
    
    # Mengambil data dari database
    zakat_data = pd.read_sql(query, conn)
    
    # Mengekspor data ke dalam file Excel
    zakat_data.to_excel("data_zakat.xlsx", index=False)
    
    conn.close()
    print("Data zakat berhasil diekspor ke dalam file 'data_zakat.xlsx'")