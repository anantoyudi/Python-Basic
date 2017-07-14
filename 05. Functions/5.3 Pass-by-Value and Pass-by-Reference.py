
"""
Dalam pemrograman, parameter dapat di lewatkan kedalam suatu fungsi menggunakan dua cara, yaitu:
1. Pass-by-Value (melewatkan parameter berdasarkan nilai)
2. Pass-by-Reference (melewatkan berdasarkan alamat atau referensinya)


Python tidak mengenal Pass-by-Value. Ini berarti bahwa semua parameter fungsi dalam Python selalu di lewatkan
menggunakan Pass-by-Reference.
"""



# contoh pengiriman parameter di dalam Python.

def ubahNilai(p):
    p *= 100
    print("\nNilai di dalam fungsi")
    print("p = %d" % p)
    return

def main():
    print("Output:")
    a = 5

    print("Sebelum pemanggilan fungsi")
    print("a = %d" % a)

    # memanggil fungsu ubahNilai()
    # dengan a sebagai parameter aktualnya
    ubahNilai(a)

    print("\nSetelah pemanggilan fungsi")
    print("a = %d" % a)

if __name__ == "__main__":
    main()

"""
Output:
Sebelum pemanggilan fungsi
a = 5

Nilai di dalam fungsi
p = 500

Setelah pemanggilan fungsi
a = 5
"""

"""
Hasil yang kita inginkan adalah a berubah menjadi 500 setelah fungsi ubahNilai() dipanggil. Untuk menganalisis
kasus ini, kita perlu mengingat kembali bahwa bilangan menrupakan objek yang tidak dapat diubah (immutable).
Pada saat program mengeksekusi statement ubahNilai(a), referensi p akan menunjuk ke objek yang sendang di tunjuk
oleh referensi a, sehingga p akan bernilai 5. Alamat memory dari p juga akan sama dengan a. Selanjutnya, ketika 
perintah p *= 100 di eksekusi, p akan menunjuk ke object baruyang nilainya 500 (berasal dari p * 100). Ini berarti
bahwa saat ini a dan p masing-masing menunjuk ke objek yang berlainan, dengan alamat memory yang berbeda. a masih 
menunjuk ke objek yang bernilai 5, sedangkan p sudah menunjuk ke object yang bernilai 500. Saat nilai a di panggil,
maka yang akan tampil adalah 5, bukan 500.
"""

