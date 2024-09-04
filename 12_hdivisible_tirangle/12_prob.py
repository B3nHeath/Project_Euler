## We need to calculate triangle numbers, their factors, and find the first triangle number with over 500 divisors


## Going to create a new way of doing this. Find the prime factorisation of the number and store it in a list,
## Then find the exponent of each prime and add 1, times them together to get the number of factors. 


## This all works fine
def main():
    prime_list = [2,3]
    p = 3
    while len(prime_list) < 10000:
        p += 2
        if Isprime(p):
            prime_list.append(p)
            continue
        else:
            continue

# Have a few things left to do. I need to start by creating the part of the code that identifies triangle numbers, thats easy enough
# follows the form:
        
# Create variables to prompt triangle numbers
    x = 1
    i = 1

# Create infinite loop
    while True:
        # Create the triangle numbers
        i += 1
        x = x + i
        # Creae empty list for prime factors
        prime_factors = []
        # Create a temporary placeholder for the x-value, so we do not ruin the original
        t = x
        # Find the list of prime factors for the number
        while t > 1:
            for y in prime_list:
                if t % y == 0:
                    t = t/y
                    prime_factors.append(y)
                    break
                else:
                    pass
    ## Here we need to create a rule that caclulates the factor rule
        if factor_number(prime_factors) > 500:
            print(x)
            print(prime_factors)
            break
        else:
            continue






def Isprime(n):
    state = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            state = False
    return state


def factor_number(list):
    exponents = []

    ## This is where the problem is
    for element in set(list):
        count_of_element = list.count(element)
        exponents.append(count_of_element + 1)
    product = 1
    for num in exponents:
        product *= num
    return product


if __name__ == "__main__":
    main()