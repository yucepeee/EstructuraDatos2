class GameModel:
    def __init__(self):
        # El tablero es una matriz 3x3 inicializada en espacios vacíos ("")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # "X" empieza por defecto
        self.game_over = False
        self.winner = None

    def reset_game(self):
        """Reinicia el estado del juego a los valores iniciales."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None

    def make_move(self, row, col):
        """
        Intenta realizar un movimiento en la posición (row, col).
        Retorna True si el movimiento es válido, False en caso contrario.
        """
        if self.game_over or self.board[row][col] != "":
            return False

        self.board[row][col] = self.current_player
        
        # Verificar si hay un ganador o empate después del movimiento
        if self._check_win(self.current_player):
            self.game_over = True
            self.winner = self.current_player
        elif self._check_draw():
            self.game_over = True
            self.winner = "Empate"
        else:
            # Alternar turno
            self.current_player = "O" if self.current_player == "X" else "X"
            
        return True

    def _check_win(self, player):
        """Comprueba si el jugador actual ha ganado (filas, columnas o diagonales)."""
        b = self.board
        # Verificar filas y columnas
        for i in range(3):
            if all(b[i][j] == player for j in range(3)) or all(b[j][i] == player for j in range(3)):
                return True
        
        # Verificar diagonales
        if all(b[i][i] == player for i in range(3)) or all(b[i][2 - i] == player for i in range(3)):
            return True
            
        return False

    def _check_draw(self):
        """Comprueba si el tablero está lleno sin un ganador (empate)."""
        return all(cell != "" for row in self.board for cell in row)

    def get_board(self):
        """Retorna una copia del estado actual del tablero."""
        return [row[:] for row in self.board]