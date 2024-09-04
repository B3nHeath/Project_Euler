# Collatz sequence: For even numbers n -> n/2
#                   For odd numbers n -> 3n + 1

# Which starting number, under one million, produces the longest sequence

def main():
    n = 1000000
    Dsteps = {}
    for x in range(3,n,2):
        Dsteps[x] = collatz(x)
    print(max(Dsteps, key = Dsteps.get))



def collatz(n):
    steps = 0
    while n > 1:
        steps += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return steps
    

if __name__ == "__main__":
    main()
