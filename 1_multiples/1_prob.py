## Find the sum of all the multiples of 3 or 5 below 1000

s = 0
for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        s = s + x
    else:
        continue

print(s)