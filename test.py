with open("p096_sudoku.txt", "r") as file:
      next(file)
      for index, line in enumerate(file, start = 1):
            print(f"{index}: {line}")