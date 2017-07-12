"""
Statement return akan menghentikan proses eksekusi kode di dalam fungsi dan eksekusi akan di arahkan ke baris pemanggil
"""


def tambah(a,b):
    c = a + b
    return c

def main():
    x = int(input('Masukan bilangan ke-1: '))
    y = int(input('Masukan bilangan ke-2: '))

    hasil = tambah(x, y)
    print('hasil dari: {} + {} = {}'.format(x, y, hasil))

if __name__ == '__main__':
    main()