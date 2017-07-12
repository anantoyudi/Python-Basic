"""
Variabel global adalah variabel yang di definisikan di luar fungsi sedangkan variabel lokal adalah variabel yang di 
definisikan di dalam fungsi
"""

# variable global
a = 10

def ubahNilai():
    a = 20

ubahNilai()
print("Nilai dari a dari fungsi pertama adalah: {}\n".format(a))

"""
Pada contoh di atas, pemanggilan fungsi ubahNilai() tidak mengubah nilai dari variabel a.
"""

a = 10
def ubahNilai():
    global a
    a = 20

ubahNilai()
print("Nilai dari a dari fungsi pertama adalah: {}".format(a))