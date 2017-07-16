"""
Dengan fasilitas keyword argumen, Python mengizinkan kita untuk merubah urutan atau posisi argumen(parameter aktual)
pada saat melakukan pemanggilan fungsi seperti di bawah ini.
"""
def infoSiswa(nama, usia, pengalaman):
    print("nama: {}" .format(nama))
    print("Usia: {} tahun" .format(usia))
    print("Pengalaman: {} tahun" . format(pengalaman))
    print("\n")

def main():
    # memanggil fungsi infoSiswa()
    infoSiswa(nama="ananto", usia=20, pengalaman=3)
    infoSiswa(usia=21, pengalaman=4, nama="yudi")
    infoSiswa(pengalaman=5, nama="hendrawan", usia=22)

if __name__=="__main__":
    main()

"""
Output:
nama: ananto
Usia: 20 tahun
Pengalaman: 3 tahun


nama: yudi
Usia: 21 tahun
Pengalaman: 4 tahun


nama: hendrawan
Usia: 22 tahun
Pengalaman: 5 tahun
"""

"""
Seperti terlihat pada hasil di atas, semua cara pemanggilan akan di anggap legal dan memberikan hasil yang sama.
"""