tugas = 0.3
uts = 0.3
uas = 0.4

def tentukan_nilai_akhir(tugas, uts, uas):
    nilai = (tugas * 0.3 + uts * 0.3 + uas * 0.4)
    return nilai

def tentukan_nilai_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70 and nilai < 85:
        return "B"
    elif nilai >= 55 and nilai < 70:
        return "C"
    elif nilai >= 40 and nilai < 55:
        return "D"
    else:
        return "E"

def tentukan_kelulusan(huruf):
    return huruf in ("A", "B", "C")

def proses_mahasiswa(nama, tugas, uts, uas):
    akhir = tentukan_nilai_akhir(tugas, uts, uas)
    huruf = tentukan_nilai_huruf(akhir)
    if tentukan_kelulusan(huruf):
        keterangan = "lulus"
    else:
        keterangan = "tidak lulus"


    print(nama + " nilai = " + str(akhir) + " " +
     " predikat = " + str(huruf) + " " + "keterangan = " + " " + keterangan)
    return akhir



    

def tampilkan(total_nilai, jumlah_lulus, jumlah_mahasiswa):
    print("rata rata nilai mahasiswa = " + str(total_nilai/jumlah_mahasiswa))
    print("total nilai mahasiswa = " + str(total_nilai))
    print("jumlah mahasiswa lulus = " + str(jumlah_lulus))

def main():
    total_nilai = 0
    jumlah_lulus = 0

    akhir = proses_mahasiswa("andi", 80, 70, 90)
    total_nilai += akhir
    if tentukan_kelulusan(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("bunga", 90, 85, 88)
    total_nilai += akhir
    if tentukan_kelulusan(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("citra", 60, 45, 50)
    total_nilai += akhir
    if tentukan_kelulusan(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("dimas", 75, 80, 65)
    total_nilai += akhir
    if tentukan_kelulusan(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("eka", 30, 40, 35)
    total_nilai += akhir
    if tentukan_kelulusan(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    print(tampilkan(total_nilai, jumlah_lulus, 1))

    
    




if __name__ == "__main__":
    main()