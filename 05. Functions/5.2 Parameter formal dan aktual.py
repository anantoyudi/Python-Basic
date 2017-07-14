"""
Parameter formal adalah parameter-parameter yang terdapat pada bagian definisi fungsi. Pada contoh kode berikut,
p disebut sebagai parameter formal. Dalam dunia pemrograman biasa di sebut parameter(saja).
"""

def tambahSatu(p):
    "Menambah bilangan p dengan nilai 1"
    hasil = p + 1
    return hasil

"""
Parameter aktual adalah parameter-parameter yang di kirimkan atau dilewatkan pada saat pemanggilan fungsi, Pada 
contoh berikut 4 dan a disebut sebagai parameter aktual. Dalam dunia pemrograman biasa di sebut argument.
"""

x = tambahSatu(4)
print(x)

a = 7
y = tambahSatu(a)
print(y)

