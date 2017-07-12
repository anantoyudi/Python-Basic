# statement break di gunakan untuk memaksa menghentikan pengulangan

def main():
    for i in range(11):
        print(i)
        if i == 7:
            break

if __name__ == '__main__':
    main()

# output
"""
0
1
2
3
4
5
6
7
"""