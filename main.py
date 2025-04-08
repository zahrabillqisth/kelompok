import mysql.connector
import pandas as pd

def create_connection():
    return mysql.connector.connect(
        host="localhost",      
        user="root",        
        password="",   
        database="zakat" 
    )

def add_zakat(nama, jenis_zakat, jumlah, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO zakat_data (nama, jenis_zakat, jumlah, tanggal) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nama, jenis_zakat, jumlah, tanggal))
    
    conn.commit()
    cursor.close()
    conn.close()

def update_zakat(id, nama, jenis_zakat, jumlah, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = """UPDATE zakat_data 
               SET nama = %s, jenis_zakat = %s, jumlah = %s, tanggal = %s 
               WHERE id = %s"""
    cursor.execute(query, (nama, jenis_zakat, jumlah, tanggal, id))
    
    conn.commit()
    cursor.close()
    conn.close()

def delete_zakat(id):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "DELETE FROM zakat_data WHERE id = %s"
    cursor.execute(query, (id,))
    
    conn.commit()
    cursor.close()
    conn.close()

def add_beras(nama_beras, harga_per_kg):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO master_beras (nama_beras, harga_per_kg) VALUES (%s, %s)"
    cursor.execute(query, (nama_beras, harga_per_kg))
    
    conn.commit()
    cursor.close()
    conn.close()

def view_master_beras():
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM master_beras"
    cursor.execute(query)
    result = cursor.fetchall()
    
    for row in result:
        print(f"ID: {row[0]}, Nama Beras: {row[1]}, Harga per Kg: {row[2]}")
    
    cursor.close()
    conn.close()

def add_transaksi_zakat(id_zakat, id_beras, jumlah_beras, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
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

def export_to_excel():
    conn = create_connection()
    query = "SELECT * FROM zakat_data"
    
    zakat_data = pd.read_sql(query, conn)
    
    zakat_data.to_excel("data_zakat.xlsx", index=False)
    
    conn.close()
    print("Data zakat berhasil diekspor ke dalam file 'data_zakat.xlsx'")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Zakat")
        print("2. Edit Data Zakat")
        print("3. Hapus Data Zakat")
        print("4. Lihat Data Master Beras")
        print("5. Tambah Transaksi Zakat")
        print("6. Lihat Transaksi Zakat")
        print("7. Ekspor Data Zakat ke Excel")
        print("8. Tambah Data Master Beras")
        print("9. Keluar")
        
        choice = input("Pilih opsi (1-8): ")
        
        if choice == "1":
            nama = input("Masukkan nama: ")
            jenis_zakat = input("Masukkan jenis zakat: ")
            jumlah = float(input("Masukkan jumlah zakat: "))
            tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
            add_zakat(nama, jenis_zakat, jumlah, tanggal)
            print("Data zakat berhasil ditambahkan.")
        
        elif choice == "2":
            id_zakat = int(input("Masukkan ID zakat yang ingin diubah: "))
            nama = input("Masukkan nama baru: ")
            jenis_zakat = input("Masukkan jenis zakat baru: ")
            jumlah = float(input("Masukkan jumlah zakat baru: "))
            tanggal = input("Masukkan tanggal baru (YYYY-MM-DD): ")
            update_zakat(id_zakat, nama, jenis_zakat, jumlah, tanggal)
            print("Data zakat berhasil diperbarui.")
        
        elif choice == "3":
            id_zakat = int(input("Masukkan ID zakat yang ingin dihapus: "))
            delete_zakat(id_zakat)
            print("Data zakat berhasil dihapus.")
        
        elif choice == "4":
            print("Master Data Beras:")
            view_master_beras()
        
        elif choice == "5":
            id_zakat = int(input("Masukkan ID zakat: "))
            id_beras = int(input("Masukkan ID beras: "))
            jumlah_beras = int(input("Masukkan jumlah beras (kg): "))
            tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
            add_transaksi_zakat(id_zakat, id_beras, jumlah_beras, tanggal)
            print("Transaksi zakat berhasil ditambahkan.")
        
        elif choice == "6":
            print("Transaksi Zakat:")
            view_transaksi_zakat()
        
        elif choice == "7":
            export_to_excel()

        elif choice == "8":
            nama_beras = input("Masukkan nama beras: ")
            harga_per_kg = float(input("Masukkan harga per kg: "))
            add_beras(nama_beras, harga_per_kg)
            print("Data beras berhasil ditambahkan.")
            break
        
        elif choice == "9":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()

def add_transaksi_zakat(id_zakat, id_beras, jumlah_beras, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
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


def export_to_excel():
    conn = create_connection()
    query = "SELECT * FROM zakat_data"
    
    zakat_data = pd.read_sql(query, conn)
    
    zakat_data.to_excel("data_zakat.xlsx", index=False)
    
    conn.close()
    print("Data zakat berhasil diekspor ke dalam file 'data_zakat.xlsx'")