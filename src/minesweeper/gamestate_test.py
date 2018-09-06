import unittest

from src.minesweeper.gamestate import GameState, Coordinate


class TestGameState(unittest.TestCase):

    def test_create_board(self):
        b = GameState(8, 0.1)
        result = b.get_state_of_cell(Coordinate(1,1))
        print(result)

    def test_reveal(self):
        b = GameState(8, 0)
        r = b.reveal(Coordinate(3,3))
        self.assertEqual(r.revealed, 1)
        self.assertEqual(r.mine, 0)
        self.assertEqual(r.adjacent, 0)

    def test_remain0(self):
        b = GameState(4, 0)
        self.assertEqual(b.cells_remaining(), 16)

    def test_remain1(self):
        b = GameState(4, 0)
        b.reveal(Coordinate(0,0))
        self.assertEqual(b.cells_remaining(), 15)


if __name__ == "__main__":
    unittest.main()