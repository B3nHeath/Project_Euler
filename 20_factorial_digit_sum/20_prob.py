import math

number = str(math.factorial(100))

total = 0
for num in number:
    total += int(num)

print(total)