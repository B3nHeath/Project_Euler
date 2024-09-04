amicable_numbers = []
divisors = []

for n in range(1,10001):
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)