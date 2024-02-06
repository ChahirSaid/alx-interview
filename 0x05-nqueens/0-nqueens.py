#!/usr/bin/python3
"""Nqueens puzzle challenge."""
import sys


def nqueens(n):
    """Nqueens puzzle challenge."""
    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for col in range(n)] for row in range(n)]
    solve(board, 0, n)


def solve(board, col, n):
    """Solve the Nqueens puzzle challenge."""
    if col == n:
        print_board(board)
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, col + 1, n)
            board[row][col] = 0
    return False


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_board(board):
    """Print the board."""
    queens = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                queens.append([row, col])
    print(queens)


def handle_input(list) -> int:
    """Handle input."""
    if len(list) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(list[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    return n


if __name__ == "__main__":
    n = handle_input(sys.argv)
    nqueens(n)
