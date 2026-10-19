import time

class MinimaxAgent:
    def __init__(self, ai_player='O', human_player='X'):
        self.ai_player = ai_player
        self.human_player = human_player
        self.nodes_evaluated = 0

    def evaluate(self, board):
        """
        Evalua el tablero y devuelve un puntaje:
        +10 si la IA gana, -10 si el humano gana, 0 en caso de empate."""
        if board.check_winner(self.ai_player):
            return 10
        elif board.check_winner(self.human_player):
            return -10
        return 0

    def minimax(self, board, depth, is_maximizing):
        """
        Implementa el algoritmo Minimax para encontrar la mejor jugada.
        """
        self.nodes_evaluated += 1
        
        score = self.evaluate(board)
        if score == 10: 
            return score - depth
        if score == -10: 
            return score + depth
        if not board.get_available_moves(): 
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in board.get_available_moves():
                board.make_move(move, self.ai_player)
                current_score = self.minimax(board, depth + 1, False)
                board.undo_move(move)
                best_score = max(current_score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in board.get_available_moves():
                board.make_move(move, self.human_player)
                current_score = self.minimax(board, depth + 1, True)
                board.undo_move(move)
                best_score = min(current_score, best_score)
            return best_score

    def get_best_move(self, board):
        """
        Encuentra la mejor jugada para la IA usando Minimax.
        """
        self.nodes_evaluated = 0
        best_score = -float('inf')
        best_move = None

        for move in board.get_available_moves():
            board.make_move(move, self.ai_player)
            score = self.minimax(board, 0, False)
            board.undo_move(move)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move