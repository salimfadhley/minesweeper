import random




class GameState:

    @staticmethod
    def _make_grid(size):
        return [[0 for _ in range(size)] for __ in range(size)]

    def __init__(self, board_size:int, mine_probability:float=0.1):
        self.mines = self._make_grid(board_size)
        self.revealed = self._make_grid(board_size)

        for row in self.mines:
            for i in range(board_size):
                if random.random() < mine_probability:
                    row[i] = 1






