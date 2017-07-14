
# Dalam pemrograman, parameter dapat di lewatkan kedalam suatu fungsi menggunakan dua cara, yaitu:
# 1. Pass-by-Value (melewatkan parameter berdasarkan nilai)
# 2. Pass-by-Reference (melewatkan berdasarkan alamat atau referensinya)


# Python tidak mengenal Pass-by-Value. Ini berarti bahwa semua parameter fungsi dalam Python selalu di lewatkan
# menggunakan Pass-by-Reference.


# contoh pengiriman parameter di dalam Python.

def ubahNilai(p):
    p *= 100
    print("\nNilai di dalam fungsi")
    print("p = %d" % p)
    return

def main():
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