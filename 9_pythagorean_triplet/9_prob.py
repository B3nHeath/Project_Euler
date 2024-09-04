import sys

m = 0
n = 0

while m < 500:
    m += 1
    for n in range (1,m):
        if m * (m + n) == 500:
            a = m ** 2 - n ** 2
            b = 2*m*n
            c = m **2 + n **2
            print(a*b*c)
            sys.exit
        else:
            continue
