import time
from models.minimax_agent import MinimaxAgent

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.ai_agent = MinimaxAgent(ai_player="O", human_player="X")
        self.view.set_controller(self)
        self.update_view()

    def handle_board_click(self, row, col):
        if self.model.game_over:
            return

        game_mode = self.view.game_mode_var.get() if hasattr(self.view, 'game_mode_var') else "IA"

        # Si es modo IA, validamos que sea el turno del humano ("X")
        if game_mode == "IA" and self.model.current_player != "X":
            return

        current_p = self.model.current_player
        move_success = self.model.make_move(row, col)

        if move_success:
            self.update_view()

            if self._check_game_end_conditions():
                return

            # Turno siguiente o respuesta de la IA
            if game_mode == "IA" and current_p == "X":
                self.view.update_status("Turno de la IA...", color="#d9534f")
                self.view.root.update_idletasks()
                self.root_after_ai_move()
            else:
                next_p = self.model.current_player
                color = "#0056b3" if next_p == "X" else "#dc3545"
                self.view.update_status(f"Turno: {next_p} (Humano)", color=color)
        else:
            # Reemplazamos messagebox por aviso rápido en estado
            self.view.update_status("Casilla ocupada. Elige otra.", color="#d9534f")

    def root_after_ai_move(self):
        if self.model.game_over:
            return

        start_time = time.time()
        best_move = self.ai_agent.get_best_move(self.model)
        end_time = time.time()
        
        elapsed_time_ms = (end_time - start_time) * 1000

        if best_move:
            r, c = best_move
            self.model.make_move(r, c)
            self.update_view()

            self.view.update_metrics(self.ai_agent.nodes_evaluated, elapsed_time_ms)

            if self._check_game_end_conditions():
                return

            self.view.update_status("Turno: X (Humano)", color="#0056b3")

    def _check_game_end_conditions(self):
        if self.model.game_over:
            if self.model.winner == "Empate":
                self.view.update_status("¡Empate!", color="#f0ad4e")
                self.view.update_metrics(self.ai_agent.nodes_evaluated, 0.0)
            else:
                winner = self.model.winner
                game_mode = self.view.game_mode_var.get() if hasattr(self.view, 'game_mode_var') else "IA"
                
                if game_mode == "IA":
                    msg = "¡Has ganado!" if winner == "X" else "¡La IA ha ganado!"
                else:
                    msg = f"¡Ganó el jugador {winner}!"

                color = "#28a745" if winner == "X" else "#dc3545"
                self.view.update_status(msg, color=color)
            return True
        return False

    def handle_reset_click(self):
        self.model.reset_game()
        self.update_view()
        self.view.update_status("Turno: X (Humano)", color="#0056b3")
        self.view.update_metrics(0, 0.0)

    def update_view(self):
        board_data = self.model.get_board()
        self.view.update_board_ui(board_data)