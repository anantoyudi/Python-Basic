"""
statement break untuk pengulangan bersarang yang di tempatkan pada blok
bagian dalam, hanya memiliki efek pada blok tersebut.
"""

def main():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j, end='\t')
            if j == 5:
                break
        print()

if __name__ == '__main__':
    main()

# output
"""
1	2	3	4	5	
2	4	6	8	10	
3	6	9	12	15	
4	8	12	16	20	
5	10	15	20	25	
6	12	18	24	30	
7	14	21	28	35	
8	16	24	32	40	
9	18	27	36	45	
10	20	30	40	50	

"""