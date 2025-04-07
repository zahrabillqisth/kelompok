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