import tkinter as tk

def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Sudoku Solver")
    
    # Create input grid for the Sudoku puzzle
    entries = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = tk.Entry(window, width=3, font=('Arial', 20))
            entry.grid(row=i, column=j)
            row.append(entry)
        entries.append(row)

    # Create Solve button
    solve_button = tk.Button(window, text="Solve", command=lambda: solve(entries))
    solve_button.grid(row=9, column=4)
    
    # Create Clear button
    clear_button = tk.Button(window, text="Clear", command=lambda: clear(entries))
    clear_button.grid(row=9, column=5)
    
    # Run the main event loop
    window.mainloop()

def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve(entries):
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            entry_value = entries[i][j].get()
            if entry_value:
                board[i][j] = int(entry_value)
    
    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
    else:
        print("No solution exists for the given Sudoku puzzle.")


def clear(entries):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

if __name__ == "__main__":
    create_gui()
