def hitung_biaya_berat(berat):
    if berat <= 2:
        return 10_000
    else:
        return 10_000 + ((berat - 2) * 4_000)

def hitung_biaya_jarak(jarak):
    if jarak > 20:
        return 5_000
    else:
        return 0

def hitung_diskon(total, anggota):
    if anggota == True:
        return total * 0.1
    else:
        return 0

def hitung_ongkir_akhir(biaya_berat, biaya_jarak, diskon):
    total = biaya_berat + biaya_jarak
    return total - diskon

def proses_pesanan(nama, berat, jarak, anggota):
    biaya_berat = hitung_biaya_berat(berat)
    biaya_jarak = hitung_biaya_jarak(jarak)
    total = biaya_berat + biaya_jarak
    diskon = hitung_diskon(total, anggota)
    ongkir = hitung_ongkir_akhir(biaya_berat, biaya_jarak, diskon)

    print("pelanggan = ", nama)
    print("biaya berat = ", biaya_berat)
    print("biaya_jarak = ", biaya_jarak)
    print("diskon = ", diskon)
    print("ongkir akhir = ", ongkir)

    return ongkir

def main():
    total_pendapatan = 0

    ongkir1 = proses_pesanan("rina", 1, 10, False)
    total_pendapatan += ongkir1

    ongkir2 = proses_pesanan("sari", 5, 25, False)
    total_pendapatan += ongkir2

    ongkir3 = proses_pesanan("tono", 5, 25, True)
    total_pendapatan += ongkir3

    ongkir4 = proses_pesanan("umar", 2, 30, True)
    total_pendapatan += ongkir4

    ongkir5 = proses_pesanan("vina", 8, 15, False)
    total_pendapatan += ongkir5

    print("total pendapatan = ", total_pendapatan)
    



if __name__ == "__main__":
    main()