"""
Python juga mengizinkan kita untuk mendefinisikan parameter opsional (default) di dalam fungsi. Parameter default
adalah parameter yang nilainya diinisialisasi pada saat fungsi di definisikan.
"""

def infoSiswa(nama, usia=30):
    print("Output:")
    print("name: {}" .format(nama))
    print("Usia: {}" .format(usia))

infoSiswa("ananto")

"""
Output:
name: ananto
Usia: 30
"""

"""
Pada contoh di atas, kita mendefinisikan parameter usia sebagai parameter default dengan nilai awal 30. ketika
fungsi infoSiswa() di panggil dengan cara di atas. Maka fungsi akan menghasilkan nama ananto dan umur 30.
"""