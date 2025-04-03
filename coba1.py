def hitung_zakat(jumlah_anggota, metode_pembayaran):
    zakat_beras_per_jiwa = 2.5  # kg
    zakat_uang_per_jiwa = 45000  # IDR (misalnya Rp 45.000 per jiwa)
    
    if metode_pembayaran.lower() == "beras":
        total_zakat = jumlah_anggota * zakat_beras_per_jiwa
        return f"Total zakat yang harus dibayar: {total_zakat} kg beras"
    elif metode_pembayaran.lower() == "uang":
        total_zakat = jumlah_anggota * zakat_uang_per_jiwa
        return f"Total zakat yang harus dibayar: Rp {total_zakat:,}"
    else:
        return "Metode pembayaran tidak valid. Silakan pilih 'beras' atau 'uang'."

if __name__ == "__main__":
    print("=== Program Pembayaran Zakat Fitrah ===")
    try:
        jumlah_anggota = int(input("Masukkan jumlah anggota keluarga: "))
        metode_pembayaran = input("Pilih metode pembayaran (beras/uang): ")
        hasil = hitung_zakat(jumlah_anggota, metode_pembayaran)
        print(hasil)
    except ValueError:
        print("Harap masukkan angka yang valid untuk jumlah anggota keluarga.")
