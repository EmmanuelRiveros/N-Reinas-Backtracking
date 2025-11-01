import copy
import time

def get_board(n):
    board = [["x"] * n for _ in range(n)]
    return board

def solve(board, col, n):
    if col >= n:
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            if col == n - 1:
                add_solution(board)
                board[i][col] = "x"
                return
            solve(board, col + 1, n)
            board[i][col] = "x"

def is_safe(board, row, col, n):
    for j in range(col):
        if board[row][j] == "Q":
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    x, y = row, col
    while x < n and y >= 0:
        if board[x][y] == "Q":
            return False
        x += 1
        y -= 1
    return True

def add_solution(board):
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)

def backtracking_experiment(n):
    global solutions
    board = get_board(n)
    solutions = []

    start = time.perf_counter()
    solve(board, 0, n)
    end = time.perf_counter()

    elapsed = end - start
    total_solutions = len(solutions)
    return elapsed, total_solutions

if __name__ == "__main__":
    for n in [4, 8, 12, 16, 20]:
        elapsed, total = backtracking_experiment(n)
        print(f"n={n:2} | Tiempo: {elapsed:.4f} s | Soluciones: {total}")
