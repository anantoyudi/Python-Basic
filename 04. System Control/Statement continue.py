"""
statement continue berguna untuk memaksa pengulangan melajutkan proses ke indek selanjutnya,
walaupun sebenarnya statement-statement dalam blok pengulangan belum semuanya di eksekusi.
"""

def main():
    for i in range(11):
        if i % 2 == 0:
            continue

        print(i, end='\t')

if __name__ == '__main__':
    main()

# output
# 1	 3	5  7  9