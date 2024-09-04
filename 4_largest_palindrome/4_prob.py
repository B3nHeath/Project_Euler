## We need to find a lapindrome that is the product of he largest three digit-numbers possible
# Their example is 9009 = 99 * 91
def main():
    pal = 0
    for x in range(999,1, -1):
        for y in range (999,1,-1):
            num = y * x
            if is_palindrome(num):
                if num > pal:
                    pal = num
                break
            else: 
                pass
    print(pal)


def is_palindrome(pal):
    pal = str(pal)
    split = int(len(pal)/2)
    left = pal[0:split]
    right = pal[split:]
    right = reverse(right)
    if left == right:
        return True
    else:
        return False

def reverse(x):
  return x[::-1]

main()
