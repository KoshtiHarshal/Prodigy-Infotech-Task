import random

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, num, pos):
    row, col = pos

    if any(grid[row][i] == num for i in range(9) if i != col):
        return False

    if any(grid[i][col] == num for i in range(9) if i != row):
        return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True 
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0 

    return False

def generate_full_grid():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    numbers = list(range(1, 10))

    def fill_grid():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(grid, num, (i, j)):
                            grid[i][j] = num
                            if not find_empty(grid) or fill_grid():
                                return True
                            grid[i][j] = 0
                    return False
        return True

    fill_grid()
    return grid

def remove_numbers(grid, clues=30):
    attempts = 81 - clues
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while grid[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        backup = grid[row][col]
        grid[row][col] = 0
        copy_grid = [r[:] for r in grid]
        if not solve(copy_grid):
            grid[row][col] = backup
        attempts -= 1
    return grid

def get_user_input():
    print("Enter your Sudoku puzzle row by row. Use 0 for empty cells.")
    user_grid = []
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ")
            if len(row.split()) == 9 and all(ch.isdigit() and 0 <= int(ch) <= 9 for ch in row.split()):
                user_grid.append([int(ch) for ch in row.split()])
                break
            else:
                print("Invalid row. Please enter exactly 9 numbers (0-9) separated by spaces.")
    return user_grid

print("Choose an option:")
print("1. Generate a random Sudoku puzzle")
print("2. Enter your own Sudoku puzzle")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    print("\nRandomly Generated Sudoku Puzzle:")
    generated_grid = generate_full_grid()
    puzzle = remove_numbers(generated_grid, clues=30)
    print_grid(puzzle)
elif choice == '2':
    puzzle = get_user_input()
    print("\nYour Entered Sudoku Puzzle:")
    print_grid(puzzle)
else:
    print("Invalid choice. Defaulting to random puzzle.")
    generated_grid = generate_full_grid()
    puzzle = remove_numbers(generated_grid, clues=30)
    print_grid(puzzle)

if solve(puzzle):
    print("\nSolved Sudoku Puzzle:")
    print_grid(puzzle)
else:
    print("\nNo solution exists for the given Sudoku puzzle.")