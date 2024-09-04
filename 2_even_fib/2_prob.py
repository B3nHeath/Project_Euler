## Trying to generate a for loop that creates the fibonacci sequence
import math

x=1
y = 2
golden = (1 + 5 ** 0.5) / 2
a = 0

while x < 4000000:
    if x % 2 == 0:
        a = a + x
    x = round((((golden) ** y) - ((1 - golden) ** y)) / math.sqrt(5))
    y += 1

print(a)