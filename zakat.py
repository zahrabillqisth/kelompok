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
