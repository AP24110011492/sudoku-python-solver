"""
Sudoku Solver using Backtracking Algorithm.
"""

# Global counter for recursive calls
recursive_calls = 0

def print_board(board, title=None):
    """
    Prints the Sudoku board in a clean 9x9 grid format with clear visibility.
    """
    if title:
        print(f"\n{'='*25}")
        print(f" {title} ")
        print(f"{'='*25}\n")
    
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            
            val = board[i][j]
            display_val = "." if val == 0 else str(val)
            
            if j == 8:
                print(display_val)
            else:
                print(display_val + " ", end="")
    print()

def is_valid(board, row, col, num):
    """
    Checks if placing num at board[row][col] is valid.
    """
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
                
    return True

def solve_sudoku(board):
    """
    Solves the Sudoku board using backtracking.
    """
    global recursive_calls
    recursive_calls += 1
    
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        if solve_sudoku(board):
                            return True
                        
                        # Backtrack
                        board[row][col] = 0
                
                return False
    
    return True

def load_board(filename):
    """
    Loads a Sudoku board from a text file.
    """
    board = []
    try:
        if not os.path.exists(filename):
            return None
        with open(filename, 'r') as f:
            for line in f:
                row = [int(x) for x in line.split()]
                if row:
                    board.append(row)
        return board
    except Exception as e:
        print(f"Error loading board: {e}")
        return None

if __name__ == "__main__":
    import os
    import sys

    # ANSI Colors for better visibility
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

    # Check if ANSI colors are supported (simplified check)
    if os.name == 'nt':
        os.system('color') 

    input_file = "sample_input.txt"
    
    if os.path.exists(input_file):
        print(f"{CYAN}>>> Loading Sudoku puzzle from '{input_file}'...{RESET}")
        sample_board = load_board(input_file)
    else:
        print(f"{YELLOW}>>> File not found. Using default internal puzzle...{RESET}")
        sample_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    if not sample_board or len(sample_board) != 9:
        print(f"{RED}Error: Invalid board format. Please provide a 9x9 grid.{RESET}")
    else:
        print_board(sample_board, "INITIAL SUDOKU BOARD")
        
        print(f"{YELLOW}Solving puzzle, please wait...{RESET}")
        
        if solve_sudoku(sample_board):
            print_board(sample_board, "SOLVED SUDOKU BOARD")
            print(f"{GREEN}SUCCESS!{RESET}")
            print(f"Puzzle solved in {YELLOW}{recursive_calls}{RESET} recursive calls.")
        else:
            print(f"{RED}NO SOLUTION EXISTS for the provided board.{RESET}")
