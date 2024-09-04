def main():
    x = 2519
    while True:
        x += 1
        if is_divisible_20(x):
            print(x)
            break
        else:
            continue

def is_divisible_20(x):
    for d in range(20,10,-1):
        if x % d != 0:
            return False
        else:
            continue
    return True

main()

## we got the answer, 232792560. However, it was slow. 
# What we could do is remove some, if its divisible by 20, its divisible by 10 and 2 etc.
# I've done this, but it did not significant reduce the magnitude of the problem, need to read about this one