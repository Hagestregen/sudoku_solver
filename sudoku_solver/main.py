import tkinter as tk
from tkinter import messagebox

# Sudoku solving logic (same as before)

def clear_board():
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)


def is_valid(board, row, col, num):
    # Check if the number is not in the given row and column
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    # Check if the number is not in the specific 3x3 grid
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_board():
    board = []
    for row in range(9):
        board.append([])
        for col in range(9):
            value = entries[row][col].get()
            board[row].append(int(value) if value.isdigit() else 0)

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, board[i][j])
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists")

# Initialize the main window
window = tk.Tk()
window.title("Sudoku Solver")

# Create a frame for each 3x3 grid
frames = [[tk.Frame(window, borderwidth=2, relief="solid") for _ in range(3)] for _ in range(3)]

# Place the frames in a grid
for i in range(3):
    for j in range(3):
        frames[i][j].grid(row=i, column=j, padx=(1 if j > 0 else 0), pady=(1 if i > 0 else 0), sticky="nsew")

# Create entries within each frame
entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(frames[i // 3][j // 3], width=2, font=('Arial', 18), justify='center')
        entry.grid(row=i % 3, column=j % 3, sticky="nsew")
        row_entries.append(entry)
    entries.append(row_entries)

# Add solve and clear buttons
solve_button = tk.Button(window, text='Solve', command=solve_board)
solve_button.grid(row=3, column=0, columnspan=3, sticky="ew")

clear_button = tk.Button(window, text='Clear', command=clear_board)
clear_button.grid(row=3, column=1, columnspan=3, sticky="ew")

# Run the main loop
window.mainloop()
