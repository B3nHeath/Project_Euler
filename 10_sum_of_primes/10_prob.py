from prob7 import Isprime

def main():
    s = 0
    for i in range(2,2000001):
        if Isprime(i):
            s = s + i
        else:
            continue

    print(s)

if __name__ == "__main__":
    main()

### This one took ages, this is an example version on the forum below, try to work this out

marked = [0] * 1000000
value = 3
s = 2
while value < 1000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 1000000:
            marked[i] = 1
            i += value
    value += 2
print s