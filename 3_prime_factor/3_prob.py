## This works but it is not something which is particularly efficient, and I'm sure there are better ways. It is worth looking into. One 
## comment in the thread is the sieve method

def main():
    # Initialise initial variables
    x = 600851475143
    # List of prime numbers
    prime = []
    # Prime factors of x
    f = []
    # for numbers in the range...
    for p in range(2,13000):
        # If p is prime
        if is_prime(p):
            # add it to our list of prime factors
            prime.append(p)


    while x > 1:
        # For each integer in our list of prime factors
        for p in prime:
            # if x / p leaves no remainder
            if x % p == 0:
                # divide x by p and replace the value
                x = x/p
                # add the prime number to our list of prime factors
                f.append(p)
            # If the prime factor is not relevant, move onto the next prime factor
            else:
                pass
        # Because we might not necessarily get the solution, print x regardless when we get to the end of our prime number list
        print(x)
    # If we break out of our loop and x == 1, then print our list of prime factors. 
    print(f)


# I have a small problem with this, code is inspired by one online. But surely if the number is divided by itself, 
# it will not leave a remainder? Hence all should be set to true? 

def is_prime(num):
    # Initialise factor flag to false
    flag = False
    # for numbers in range 2,number
    for i in range(2, num):
        # If our number divides by another number within the range without a remainder
        if (num % i) == 0:
            # Then it is not a prime factor and we should set the flag to True, break out the program
            flag = True
            break
    # If flag is true, the factor is not prime, return false
    if flag:
        return False
    # else return true
    else:
        return True

main() 


##  below is a better version of what I have run, it runs in a similar way, but uses maths to shorten the problem count significantly 

def Isprime(n):
    state = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            state = False
    return state


def PrimeFactory(n):
    biggestPrimeFactory = 0
    for i in range(int(n**0.5)+1,1,-1):
        if n % i == 0 and Isprime(i):
            biggestPrimeFactory = i
            break
    print(biggestPrimeFactory)

 # PrimeFactory(600851475143)