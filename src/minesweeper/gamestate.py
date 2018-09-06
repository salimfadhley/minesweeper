import itertools
import random
from collections import namedtuple
from typing import Sequence

CellState = namedtuple("CellState", ["mine", "revealed", "adjacent"])

Coordinate = namedtuple("Coordinate", ["x", "y"])


class YouHaveExploded(RuntimeError):
    """
    You shizz be ganked
    """

class GameState:

    @staticmethod
    def _count_grid(g:Sequence[Sequence[int]]):
        return sum(itertools.chain(*g))

    @staticmethod
    def _make_grid(size):
        return [[0 for _ in range(size)] for __ in range(size)]

    @staticmethod
    def _lookup_in_grid(g, c:Coordinate)->int:
        return g[c.x][c.y]

    @staticmethod
    def _set_state_in_grid(g, c:Coordinate, v:int)->None:
        g[c.x][c.y] = v

    def __init__(self, board_size:int, mine_probability:float=0.1):
        self.mines = self._make_grid(board_size)
        self.revealed = self._make_grid(board_size)
        self.board_size:int = board_size

        for row in self.mines:
            for i in range(board_size):
                if random.random() < mine_probability:
                    row[i] = 1


    @staticmethod
    def _get_adjacent_coordinates(c:Coordinate, board_size:int)->Sequence[Coordinate]:
        all_x = [x for x in [c.x-1, c.x, c.x+1] if x >= 0 and x < board_size]
        all_y = [y for y in [c.y-1, c.y, c.y+1] if y >= 0 and y < board_size]

        coordinates = []

        for x in all_x:
            for y in all_y:
                cc = Coordinate(x,y)
                if cc != c:
                    coordinates.append(cc)

        return coordinates

    def get_state_of_cell(self, c:Coordinate) -> CellState:
        return CellState(
            self._lookup_in_grid(self.mines, c),
            self._lookup_in_grid(self.revealed, c),
            sum(self._lookup_in_grid(self.mines, adj) for adj in self._get_adjacent_coordinates(c, self.board_size))
        )

    def reveal(self, c:Coordinate):
        cell = self.get_state_of_cell(c)
        if cell.mine:
            raise YouHaveExploded("There was a mine at %r" % c)
        self._set_state_in_grid(self.revealed, c, 1)
        return self.get_state_of_cell(c)

    def add_mine(self, c):
        self._set_state_in_grid(self.mines, c, 1)

    def cells_remaining(self):
        return self.board_size ** 2 - \
               (self._count_grid(self.mines) + self._count_grid(self.revealed))










