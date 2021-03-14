# task from hyperskill.org

import numpy as np

O = [[4, 14, 15, 5]]
I = [[4, 14, 24, 34], [3, 4, 5, 6]]
S = [[5, 4, 14, 13], [4, 14, 15, 25]]
Z = [[4, 5, 15, 16], [5, 15, 14, 24]]
L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]


class Figure:
    def __init__(self, figure):
        self.figure = figure
        self.shift_hor = 0
        self.shift_bott = 0
        self.rot = 0

    """
    Returns if (m,n) field is occupied by figure, rotated and shifted 
    """
    def is_figure_here(self, m, n):
        idx = self.rot % len(self.figure)
        figure_rotated = self.figure[idx]
        for sq in figure_rotated:
            sqx = sq % 10 + self.shift_hor
            sqy = sq // 10 + self.shift_bott
            if m == sqx and n == sqy:
                return True
        return False


class GameBoard:
    def __init__(self, M, N):
        self.M = M  # cols
        self.N = N  # rows
        self.board = np.zeros((M, N), dtype=bool)

    def is_cell_occupied(self, col, row):
        # Return True (occupied) if out of range
        if col < 0 or col >= self.M:
            return True
        if row < 0 or row >= self.N:
            return True
        # Check actual cell
        return self.board[col, row]

    def is_bottom_filled(self):
        return all([self.is_cell_occupied(i, N-1) for i in range(0, M)])

    def remove_bottom_layer(self):
        for col in range(0, M):
            for row in range(N-2, 0, -1):
                self.board[col, row+1] = self.board[col, row]
            self.board[col, 0] = False

    def set_cell(self, col, row, val=True):
        self.board[col, row] = True

    def freeze_fig(self, fig: Figure):
        for row in range(0, N):
            for col in range(0, M):
                if fig.is_figure_here(col, row):
                    board.set_cell(col, row, True)

    def has_cells_in_top(self):
        return any([self.board[col, 0] for col in range(0, M)])


def ch(b):
    return "0" if b else "-"


def print_game(board: GameBoard, cur_fig: Figure) -> None:
    for n in range(0, N):
        for m in range(0, M):
            print(ch(cur_fig.is_figure_here(m, n) or board.is_cell_occupied(m, n)), end="")
            if m != M-1:
                print(" ", end="")
        print()
    print()


def can_move_right(board: GameBoard, fig: Figure) -> bool:
    for m in range(0, M):
        for n in range(0, N):
            if fig.is_figure_here(m, n):
                if board.is_cell_occupied(m+1, n):
                    return False
    return True


def can_move_left(board: GameBoard, fig: Figure) -> bool:
    for m in range(0, M):
        for n in range(0, N):
            if fig.is_figure_here(m, n):
                if board.is_cell_occupied(m-1, n):
                    return False
    return True


def can_move_down(board: GameBoard, fig: Figure) -> bool:
    for m in range(0, M):
        for n in range(0, N):
            if fig.is_figure_here(m, n):
                if board.is_cell_occupied(m, n+1):
                    return False
    return True


def overlap_exists(board: GameBoard, fig: Figure) -> bool:
    for m in range(0, M):
        for n in range(0, N):
            if fig.is_figure_here(m, n):
                if board.is_cell_occupied(m, n):
                    return True
    return False


if __name__ == "__main__":
    M, N = map(int, input().split())

    board = GameBoard(M, N)
    current_fig = Figure([[]])
    print_game(board, current_fig)

    while True:
        command = input()

        if command == "piece":
            fig_name = input().upper()
            fig = globals().get(fig_name)
            if fig is None:
                print("No such figure")
                raise Exception
            current_fig = Figure(fig)

            if overlap_exists(board, current_fig): 
                print_game(board, current_fig)
                #print("Game over!")
                break

        elif command == "right":
            if can_move_right(board, current_fig):
                current_fig.shift_hor += 1
            if can_move_down(board, current_fig):
                current_fig.shift_bott += 1
        elif command == "left":
            if can_move_left(board, current_fig):
                current_fig.shift_hor -= 1
            if can_move_down(board, current_fig):
                current_fig.shift_bott += 1
        elif command == "down":
            if can_move_down(board, current_fig):
                current_fig.shift_bott += 1
        elif command == "rotate":
            # TODO check if rotation is possible
            current_fig.rot += 1
            if can_move_down(board, current_fig):
                current_fig.shift_bott += 1
        elif command == "break":
            while board.is_bottom_filled():
                board.remove_bottom_layer()
        elif command == "exit":
            break

        print_game(board, current_fig)

        if not can_move_down(board, current_fig):
            board.freeze_fig(current_fig)
            current_fig = Figure([[]])
        else:
            if board.has_cells_in_top():
                break

