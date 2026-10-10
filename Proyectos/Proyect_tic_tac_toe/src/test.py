import unittest
from models.game_model import GameModel

class TestGameModel(unittest.TestCase):
    def setUp(self):
        self.game = GameModel()

    def test_initial_state(self):
        self.assertEqual(self.game.current_player, "X")
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.winner, None)
        self.assertEqual(self.game.get_board(), [["", "", ""], ["", "", ""], ["", "", ""]])

    def test_valid_and_invalid_moves(self):
        # Movimiento válido
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], "X")
        self.assertEqual(self.game.current_player, "O")

        # Movimiento inválido en la misma casilla
        self.assertFalse(self.game.make_move(0, 0))

    def test_win_condition_row(self):
        # Simular victoria de X en la primera fila
        self.game.make_move(0, 0) # X
        self.game.make_move(1, 0) # O
        self.game.make_move(0, 1) # X
        self.game.make_move(1, 1) # O
        self.game.make_move(0, 2) # X (Gana)

        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, "X")

if __name__ == "__main__":
    unittest.main()