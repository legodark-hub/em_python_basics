class Cell:
    def __init__(self) -> None:
        self.around_mines: int = 0
        self.mine: bool = False
        self.fl_open: bool = False