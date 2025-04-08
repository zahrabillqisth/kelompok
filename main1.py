

def tampilkan_harga_beras():
    print(f"Harga beras saat ini: Rp {zakat_uang_per_jiwa:,} per jiwa")

def input_harga_beras():
    global zakat_uang_per_jiwa
    try:
        zakat_uang_per_jiwa = int(input("Masukkan harga beras per jiwa (dalam Rupiah): "))
        print("Harga beras berhasil diperbarui!")
    except ValueError:
        print("Harap masukkan angka yang valid.")

def tampilkan_data_zakat():
    print("Data Zakat belum tersedia.")

def pembayaran_zakat():
    try:
        jumlah_anggota = int(input("Masukkan jumlah anggota keluarga: "))
        metode_pembayaran = input("Pilih metode pembayaran (beras/uang): ")
        if metode_pembayaran.lower() == "beras":
            total_zakat = jumlah_anggota * 2.5
            print(f"Total zakat yang harus dibayar: {total_zakat} kg beras")
        elif metode_pembayaran.lower() == "uang":
            total_zakat = jumlah_anggota * zakat_uang_per_jiwa
            print(f"Total zakat yang harus dibayar: Rp {total_zakat:,}")
        else:
            print("Metode pembayaran tidak valid. Silakan pilih 'beras' atau 'uang'.")
    except ValueError:
        print("Harap masukkan angka yang valid untuk jumlah anggota keluarga.")

def export_excel():
    data = {"Nama": ["Ahmad", "Budi", "Siti"], "Zakat (Rp)": [45000, 90000, 135000]}
    df = pd.DataFrame(data)
    df.to_excel("data_zakat.xlsx", index=False)
    print("Data zakat berhasil diekspor ke data_zakat.xlsx")

def main():
    while True:
        print("\nMenu:")
        print("1. Tampilkan Harga Beras")
        print("2. Input Harga Beras")
        print("3. Tampilkan Data Zakat")
        print("4. Pembayaran Zakat")
        print("5. Export Excel")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5/6): ")
        
        if pilihan == "1":
            tampilkan_harga_beras()
        elif pilihan == "2":
            input_harga_beras()
        elif pilihan == "3":
            tampilkan_data_zakat()
        elif pilihan == "4":
            pembayaran_zakat()
        elif pilihan == "5":
            export_excel()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    zakat_uang_per_jiwa = 45000
    main()
