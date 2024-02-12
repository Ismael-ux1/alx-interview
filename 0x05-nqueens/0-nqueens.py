#!/usr/bin/python3
""" N queen """
import sys


def print_solution(board):
    """ print the solution """
    print("[", end="")
    for i in range(len(board)):
        if i != 0:
            print(", ", end="")
        print("[{}, {}]".format(i, board[i]), end="")
    print("]")


def is_safe(board, row, col):
    """ check if it's safe to place a queen at board[x][y]. """
    for i in range(col):
        if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
            return False
    return True


def solve_n_queens(board, col):
    """ Use backtracking to find all solution """
    n = len(board)
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_n_queens(board, col + 1)


def check_args():
    """ Check and validate the arguments """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    arg = sys.argv[1]
    if not arg.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(arg)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def main():
    """ Solve the N queen problem. """
    n = check_args()
    board = [-1] * n
    solve_n_queens(board, 0)


if __name__ == "__main__":
    main()
