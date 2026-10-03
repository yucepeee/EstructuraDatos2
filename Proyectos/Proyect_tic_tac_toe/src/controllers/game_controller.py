class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.set_controller(self)  # Establece el controlador con la view

        self.update_view() # Actualiza la vista con los datos iniciales del modelo

    def handle_board_click(self, row, col):
        # Lógica para manejar el clic en el tablero
        if self.model.game_over:
            return  # No hacer nada si el juego ha terminado

        # Intentar realizar un movimiento en el modelo
        move_success = self.model.make_move(row, col)

        if move_success:
            self.update_view()  # Actualiza la vista después de un movimiento exitoso

            if self.model.game_over:
                if self.model.winner == "Empate":
                    self.view.update_status("¡Empate!")
                    self.view.show_game_over("¡Empate!")
                else:
                    winner = self.model.winner
                    self.view.update_status(f"¡{winner} gana!")
                    self.view.show_game_over(f"¡{winner} gana!")
            

    def handle_reset_click(self):
        self.model.reset_game()  # Reinicia el juego en el modelo
        self.update_view()  # Actualiza la vista después de reiniciar
        self.view.update_status("Turno: X", color="#0056b3")  # Reinicia el estado del juego en la vista

    def update_view(self):
        """Actualiza la vista con los datos actuales del modelo."""
        board_data = self.model.get_board() 
        self.view.update_board_ui(board_data)  # Actualiza la interfaz del tablero en la vista
