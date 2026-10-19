import time
import random
import tkinter as tk
from models.minimax_agent import MinimaxAgent
from models.ml_agent import MLAgent
from models.game_model import GameModel

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Instanciar ambos agentes de IA
        self.minimax_agent = MinimaxAgent(ai_player="O", human_player="X")
        self.ml_agent = MLAgent()
        
        # Entrenar el modelo ML al iniciar (si ya existe el CSV, tarda menos de 1 segundo)
        acc = self.ml_agent.train_model()
        self.ml_accuracy = acc * 100
        
        self.view.set_controller(self)
        self.update_view()
        self.view.update_metrics(0, 0.0, f"Precisión ML: {self.ml_accuracy:.1f}%")

    def handle_board_click(self, row, col):
        if self.model.game_over:
            return

        game_mode = self.view.game_mode_var.get()

        # Si es modo contra alguna IA, validamos que sea el turno del humano ("X")
        if game_mode in ("Minimax", "ML") and self.model.current_player != "X":
            return

        current_p = self.model.current_player
        move_success = self.model.make_move(row, col)

        if move_success:
            self.update_view()

            if self._check_game_end_conditions():
                return

            # Turno de la IA (Minimax o Machine Learning)
            if game_mode in ("Minimax", "ML") and current_p == "X":
                self.view.update_status(f"IA ({game_mode}) pensando...", color="#d9534f")
                self.view.root.update_idletasks()
                self.root_after_ai_move(game_mode)
            else:
                next_p = self.model.current_player
                color = "#0056b3" if next_p == "X" else "#dc3545"
                self.view.update_status(f"Turno: {next_p} (Humano)", color=color)
        else:
            self.view.update_status("Casilla ocupada. Elige otra.", color="#d9534f")

    def root_after_ai_move(self, game_mode):
        if self.model.game_over:
            return

        start_time = time.perf_counter()
        
        if game_mode == "Minimax":
            best_move = self.minimax_agent.get_best_move(self.model)
            nodes = self.minimax_agent.nodes_evaluated
        else:
            # Inferencia instantánea con el Árbol de Decisión (1 sola evaluación del árbol, 0 backtracking)
            best_move = self.ml_agent.get_best_move(self.model)
            nodes = 1  # El árbol de decisión evalúa 1 sola ruta directa (sin backtracking)

        end_time = time.perf_counter()
        elapsed_time_ms = (end_time - start_time) * 1000

        if best_move:
            r, c = best_move
            self.model.make_move(r, c)
            self.update_view()

            self.view.update_metrics(nodes, elapsed_time_ms)

            if self._check_game_end_conditions():
                return

            self.view.update_status("Turno: X (Humano)", color="#0056b3")

    def handle_benchmark_click(self):
        """
        Inicia la prueba comparativa de forma asíncrona (con root.after)
        para no congelar ni deformar la interfaz gráfica de Tkinter.
        """
        # Deshabilitar botón temporalmente para evitar dobles clics
        self.view.benchmark_button.config(state=tk.DISABLED)
        
        self._bench_mm_times = []
        self._bench_ml_times = []
        self._bench_matches = 0
        self._bench_total_moves = 0
        self._bench_total_games = 25  # 25 partidas de prueba

        # Iniciar el ciclo asíncrono desde la partida 0
        self._run_benchmark_step(0)

    def _run_benchmark_step(self, game_idx):
        """Ejecuta una sola partida de prueba y cede el control a la UI antes de la siguiente."""
        if game_idx < self._bench_total_games:
            self.view.update_status(
                f"Comparando...\nPartida {game_idx + 1}/{self._bench_total_games}", 
                color="#0275d8"
            )

            test_game = GameModel()
            while not test_game.game_over and test_game.get_available_moves():
                if test_game.current_player == "O":
                    # 1. Medir Minimax
                    t0 = time.perf_counter()
                    mm_move = self.minimax_agent.get_best_move(test_game)
                    t1 = time.perf_counter()
                    self._bench_mm_times.append((t1 - t0) * 1000)

                    # 2. Medir Árbol ML
                    t2 = time.perf_counter()
                    ml_move = self.ml_agent.get_best_move(test_game)
                    t3 = time.perf_counter()
                    self._bench_ml_times.append((t3 - t2) * 1000)

                    if mm_move == ml_move:
                        self._bench_matches += 1
                    self._bench_total_moves += 1

                    test_game.make_move(mm_move[0], mm_move[1])
                else:
                    mv = random.choice(test_game.get_available_moves())
                    test_game.make_move(mv[0], mv[1])

            # Programar la siguiente partida en 10ms para que la interfaz se refresque sin congelarse
            self.view.root.after(10, lambda: self._run_benchmark_step(game_idx + 1))
        else:
            # Finalizó la comparativa: calcular promedios y mostrarlos
            avg_mm = sum(self._bench_mm_times) / len(self._bench_mm_times) if self._bench_mm_times else 0
            avg_ml = sum(self._bench_ml_times) / len(self._bench_ml_times) if self._bench_ml_times else 0
            match_pct = (self._bench_matches / self._bench_total_moves * 100) if self._bench_total_moves else 0

            resumen = (
                f"MM: {avg_mm:.1f}ms | ML: {avg_ml:.2f}ms\n"
                f"Coincidencia: {match_pct:.1f}%"
            )
            self.view.update_metrics("MM vs ML", avg_ml, resumen)
            self.view.update_status("¡Comparativa completada!", color="#28a745")
            self.view.benchmark_button.config(state=tk.NORMAL)

    def _check_game_end_conditions(self):
        if self.model.game_over:
            if self.model.winner == "Empate":
                self.view.update_status("¡Empate técnico!", color="#f0ad4e")
            else:
                winner = self.model.winner
                game_mode = self.view.game_mode_var.get()
                
                if game_mode in ("Minimax", "ML"):
                    msg = "¡Has ganado!" if winner == "X" else f"¡La IA ({game_mode}) ha ganado!"
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