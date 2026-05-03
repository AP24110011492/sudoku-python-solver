# Sudoku Solver

A clean and efficient Sudoku Solver built with Python using the **Backtracking** algorithm. This project demonstrates how recursion can be used to solve constraint-satisfaction problems like Sudoku.

## 🚀 Features

- **Backtracking Algorithm**: Efficiently explores possible solutions and backtracks when a dead end is reached.
- **Visual Grid Output**: Prints the solved Sudoku board in a clean, human-readable 9x9 format.
- **Recursive Call Counter**: Tracks how many recursive calls were made to find the solution.
- **Validation Logic**: Robust checks for rows, columns, and 3x3 subgrids.

## 🛠️ How it Works

The solver follows these steps:
1. Finds an empty cell (represented by `0`).
2. Tries placing numbers `1` through `9` in that cell.
3. Checks if the number is valid (not already in the row, column, or 3x3 box).
4. If valid, recursively tries to solve the rest of the board.
5. If the board cannot be solved with that number, it resets the cell (backtracks) and tries the next number.

## 💻 How to Run

1. **Clone or Save**: Ensure you have `sudoku_solver.py` in your local directory.
2. **Execute**: Run the script using Python:

   ```bash
   python sudoku_solver.py
   ```

## 🧩 Customization

To solve your own puzzle, open `sudoku_solver.py` and update the `sample_board` variable:

```python
sample_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    # ... fill in the rest ...
]
```

## 📊 Example Output

```text
Initial Sudoku Board:
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
- - - - - - - - - - -
...

Solving...

Solved Sudoku Board:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
- - - - - - - - - - -
...
Solved in 4209 recursive calls.
```
