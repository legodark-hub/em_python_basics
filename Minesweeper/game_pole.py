from random import randint
from cell import Cell


class GamePole:
    def __init__(self, n: int, m: int) -> None:
        self.size = n
        self.pole: list
        self.mines = m
        if m > n**2 or m < 1:
            raise AttributeError("Неправильное число мин")
        self.init(m)

    def init(self, mines: int) -> None:
        self.pole = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self._place_mines()
        self._place_mines_around_count()

    def _place_mines(self) -> None:
        mine_counter = 0
        while mine_counter < self.mines:
            row = randint(0, self.size - 1)
            col = randint(0, self.size - 1)
            if self.pole[row][col].mine == False:
                self.pole[row][col].mine = True
                mine_counter += 1

    def _place_mines_around_count(self) -> None:
        for row in range(self.size):
            for col in range(self.size):
                if self.pole[row][col].mine == False:
                    self.pole[row][col].around_mines = self._count_around_mines(
                        row, col
                    )

    def _count_around_mines(self, row: int, col: int) -> int:
        count = 0
        for i in range(max(0, row - 1), min(self.size, row + 2)):
            for j in range(max(0, col - 1), min(self.size, col + 2)):
                if self.pole[i][j].mine == True:
                    count += 1
        return count

    def _print_cell(self, cell):
        if cell.fl_open == False:
            return "#"
        elif cell.mine == True:
            return "*"
        else:
            return f"{cell.around_mines}"

    def show(self) -> None:
        for row in self.pole:
            cell_row = list(map(self._print_cell, row))
            print(" ".join(cell_row))
        print("")
            
    def open_cell(self, row: int, col: int) -> None:
        self.pole[row][col].fl_open = True