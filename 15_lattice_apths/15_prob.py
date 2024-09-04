## First potential solution uses the fact that you can use the sum of possible avenues above and to the left to solve
# Create a 21x21 matrix


# Create the first row in the matrix, equal to one, as there is one route to get to each dot in the top row
# Matrix is a list of lists
matrix = [[1]*21]

# Create another 20 rows that are set to zero
for _ in range(20):
    matrix.append([0]*21)

# Set each of the first items in a row to 1
for row in matrix:
    row[0] = 1

# For each row and column (starting in by one)
for r in range (1,21):
    for c in range(1,21):
        # Set position value equal to sum of position above, and to the left
        matrix[r][c] = matrix[r-1][c] + matrix[r][c-1] 

# Print the final position matrix value
print(matrix[20][20])


## The alternative solution uses mathematics. It uses the binomial coefficient, which shows the number of permutations for selecting k elements from n options

import math
size = 20

def fa(n):
    return math.factorial(n)

def calculate(n,k):
    return int(fa(n)/(fa(n-k)*fa(k)))

answer = calculate(size * 2, size)