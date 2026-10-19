class GameModel:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None

    def make_move(self, move_or_row, col=None, player=None):
        if isinstance(move_or_row, tuple):
            row, c = move_or_row
            actual_player = player if player is not None else col
            p = actual_player if actual_player else self.current_player
        else:
            row = move_or_row
            c = col
            p = self.current_player

        if self.game_over or self.board[row][c] != "":
            return False

        self.board[row][c] = p
        
        if player is None and not isinstance(move_or_row, tuple):
            if self.check_winner(p):
                self.game_over = True
                self.winner = p
            elif self._check_draw():
                self.game_over = True
                self.winner = "Empate"
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        
        return True

    def undo_move(self, move):
        row, col = move
        self.board[row][col] = ""
        self.game_over = False
        self.winner = None

    def get_available_moves(self):
        moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    moves.append((r, c))
        return moves

    def check_winner(self, player):
        b = self.board
        for i in range(3):
            if all(b[i][j] == player for j in range(3)) or all(b[j][i] == player for j in range(3)):
                return True
        if all(b[i][i] == player for i in range(3)) or all(b[i][2 - i] == player for i in range(3)):
            return True
        return False

    def _check_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def get_board(self):
        return [row[:] for row in self.board]