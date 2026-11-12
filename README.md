pada soal 1
saya melakukan perhitungan manual mahasiswa andi dan dimas
1. andi
tugas = 80
uts = 70
uas = 90

perhitungan:
nilai_akhir = (80 * 0,3) + (70 * 0.3) + (90 * 0.4)
            = 24 + 21 + 36
            = 81
nilai_huruf = B karena dalam program jika nilai lebih dari atau sama dengan 70 dan kurang dari 85 mendapat predikat B

keterangan = lulus karena dalam program syarat lulus minimal predikat C

2. dimas
tugas = 75
uts = 80
uas = 65 

perhitungan: 
nilai_akhir = (75 * 0,3) + (80 * 0,3) + (65 * 0,4)
            = 22,5 + 24 + 26
            = 72,5
nilai_huruf = B karena dalam program jika nilai lebih dari atau sama dengan 70 dan kurang dari 85 mendapat predikat B
keterangan = lulus karena dalam program syarat lulus minimal predikat C

hasil perhitungan manual sesuai dengan hasil yang ditampilkan oleh program

untuk menambahkan fitur pencarian nilai tertinggi di perlukan fungsi bernama cari_nilai_tertinggi() fungsi tersebut digunakan untuk membandingkan nilai akhir kelima mahasiswa dan menentukan mahasiswa yang memperoleh nilai paling tinggi selain itu fungsi proses_mahasiswa() tetap digunakan untuk menghitung nilai dan mengembalikan nilai akhir menggunakan return 

fungsi tentukan_nilai_akhir(), tentukan_nilai_huruf(), dan tentukan_kelulusan() tidak perlu di ubah karena tugasnya tetap sama


pada soal nomo 2
saya melakukan perhitungan manual pada:
1. pesanan sari
berat = 5 kg
jarak 25 kg 
anggota = bukan 

biaya berat:
10.000 + (3 x 4000) = 22.000
biaya jarak = 5.000
diskon = 0
ongkos_kirim_akhir :
 22.000 + 5.0000 = 27.000

2. pesanan tono
berat = 5 kg
jarak 25 kg 
anggota = ya 

biaya berat:
10.000 + (3 x 4000) = 22.000
biaya jarak = 5.000
diskon = 10% (2.700)
ongkos_kirim_akhir sebelum diskon :
 22.000 + 5.0000 = 27.000

ongkos_kirim_akhir setelah diskon:
27.000 - 2.700 = 24.300

3. pesanan umar
berat = 5 kg
jarak 25 kg 
anggota = bukan 

biaya berat = 10.000
biaya jarak = 5.000
diskon = 10% (1.500)
ongkos_kirim_akhir  sebelum diskon:
 10.000 + 5.000 = 15.000
ongkos_kirim_akhir setelah diskon:
15.000 - 1.500 = 13.500

hasil perhitungan manual sesuai dengan program
pada soal 2 toko mengubah kebijakan biaya jarak menjadi:
-tidak ada biaya tambahan jika jarak tidak lebih dari 15 km
-biaya tambahan 7.000 jika jarak lebih dari 15 km

bagian yang perlu di ubah adalah fungsi:
hitung_biaya_jarak()

dari code sebelumnya:
def hitung_biaya_jarak(jarak):
    if jarak > 20:
        return 5_000
    else:
        return 0

menjadi:
def hitung_biaya_jarak(jarak):
    if jarak > 15:
        return 7_000
    else:
        return 0

dengan menggunakan fungsi tersebut perubahan kebijkan cukup dilakukan pada satu fungsi saja, fungsi lainnya tidak perlu diubah karena perhitungan berat, diskon, dan ongkos kirim akhir tetap sama
