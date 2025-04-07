import mysql.connector
import pandas as pd

# Koneksi ke database MySQL
def create_connection():
    return mysql.connector.connect(
        host="localhost",      # Alamat host MySQL
        user="root",           # Username MySQL
        password="",   # Password MySQL
        database="zakat" # Nama database
    )
# Fungsi untuk menambahkan data zakat
def add_zakat(nama, jenis_zakat, jumlah, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO zakat_data (nama, jenis_zakat, jumlah, tanggal) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nama, jenis_zakat, jumlah, tanggal))
    
    conn.commit()
    cursor.close()
    conn.close()
# Fungsi untuk mengupdate data zakat
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
# Fungsi untuk menghapus data zakat
def delete_zakat(id):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "DELETE FROM zakat_data WHERE id = %s"
    cursor.execute(query, (id,))
    
    conn.commit()
    cursor.close()
    conn.close()
# Fungsi untuk menambahkan data beras ke dalam master data beras
def add_beras(nama_beras, harga_per_kg):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO master_beras (nama_beras, harga_per_kg) VALUES (%s, %s)"
    cursor.execute(query, (nama_beras, harga_per_kg))
    
    conn.commit()
    cursor.close()
    conn.close()
# Fungsi untuk menampilkan data master beras
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
