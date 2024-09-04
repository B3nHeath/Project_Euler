import sys
import os
import math
from sudoku_solver import Puzzle

# Transferring over puzzle contents

text = ""
sudokus = []
with open("p096_sudoku.txt", "r") as file:
      next(file)
      for index, line in enumerate(file, start = 1):
            if index % 10 != 0:
                  text += line.strip("\n")
            else:
                  sudokus.append(text)
                  text = ""

solve_sum = 0
for sudoku in sudokus:
      solve_num = ""
      puzzle = Puzzle()
      for index, cell in enumerate(sudoku):
            if cell != "0":
                  row = math.floor(index/9)
                  column = index % 9
                  puzzle.matrix[row][column] = int(cell)
      puzzle.solve()
      solve_num += str(puzzle.matrix[0][0]) + str(puzzle.matrix[0][1]) + str(puzzle.matrix[0][2])
      print(solve_num)


# replace known values in the sudoku
# for index, cell in enumerate(numbers):
#         if cell != "0":
#             row = math.floor(index/9)
#             column = index % 9
#             puzzle.matrix[row][column] = int(cell)
# print(puzzle, end = "\n\n")
# puzzle.solve()
# print(puzzle)
