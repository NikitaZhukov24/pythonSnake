class Board:
    def __init__ (self, x, y, size=20):
        self.x = x
        self.y = y
        self.ceil_size = size
        self.board = [[' ' for _ in range(y // size)] for _ in range(x // size)]
