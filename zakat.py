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
