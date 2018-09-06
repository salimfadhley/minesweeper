import unittest

from src.minesweeper.gamestate import GameState, Coordinate


class TestGameState(unittest.TestCase):

    def test_create_board(self):
        b = GameState(8, 0.1)
        result = b.get_state_of_cell(Coordinate(1,1))
        print(result)


if __name__ == "__main__":
    unittest.main()