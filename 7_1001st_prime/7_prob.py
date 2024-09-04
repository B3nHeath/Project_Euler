def main():
    prime = []
    i = 1
    while len(prime) < 10001:
        i += 1
        if Isprime(i):
              prime.append(i)
              continue
        else:
            continue
    print(prime[10000])



def Isprime(n):
    state = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            state = False
    return state

if __name__ == "__main__":
    main()