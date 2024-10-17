# Program Pembayaran Bimbel Matematika

# Input nama siswa
nama = input("Masukkan nama siswa: ")

# Input jumlah pertemuan bimbel per minggu
pertemuan_per_minggu = int(input("Masukkan jumlah pertemuan bimbel per minggu: "))

# Input tarif per jam
tarif_per_pertemuan = float(input("Masukkan tarif per pertemuan: "))

# Hitung total biaya per minggu
total_biaya_per_minggu = pertemuan_per_minggu * tarif_per_pertemuan

# Tampilkan informasi pembayaran
print("Rincian Pembayaran")
print("Nama Siswa:", nama)
print("Jumlah Pertemuan Per Minggu:", pertemuan_per_minggu)
print("Tarif Per Pertemuan: Rp", tarif_per_pertemuan)
print("Total Biaya Per Minggu: Rp", total_biaya_per_minggu)

# Input pembayaran
pembayaran = float(input("Masukkan jumlah pembayaran: "))

# Hitung sisa pembayaran
sisa = pembayaran - total_biaya_per_minggu

# Tampilkan sisa pembayaran
if sisa > 0 or sisa == 0:
    print("Sisa Pembayaran: Rp", sisa)
    print("Pembayaran sudah lunas.")
else:
    print("Pembayaran belum lunas.")

if sisa < 0:
    print("Pembayaran kurang: Rp", sisa)
    print("Mohon maaf segera lunasi pembayaran.")
else:
    print("Terima Kasih.")


