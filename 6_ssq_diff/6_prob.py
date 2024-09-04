x = 0 
y = 0

for i in range(1,101):
    x = x + (i ** 2)

for i in range(1,101):
    y = y + i

y = y ** 2

print(y-x)
print(y)
print(x)