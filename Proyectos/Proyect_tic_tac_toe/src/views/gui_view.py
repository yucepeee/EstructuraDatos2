import tkinter as tk

class GameView:
    def __init__(self, root, controller=None):
        self.root = root
        self.root.title("Tres en Raya - IA & Machine Learning")
        self.root.geometry("500x450")
        self.root.config(bg="#f0f0f0")
        
        self.controller = controller
        
        self._create_widgets()

    def set_controller(self, controller):
        """Asocia el controlador a la vista para manejar eventos de usuario."""
        self.controller = controller

    def _create_widgets(self):
        """Configura los elementos visuales de la ventana principal."""
        title_label = tk.Label(
            self.root, 
            text="Tres en Raya (Tic-Tac-Toe)", 
            font=("Arial", 18, "bold"), 
            bg="#f0f0f0", 
            fg="#333333"
        )
        title_label.pack(pady=10)

        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(expand=True)

        # Marco del Tablero (Grilla de 3x3 botones)
        self.board_frame = tk.Frame(main_frame, bg="#333333", bd=2)
        self.board_frame.pack(side=tk.LEFT, padx=15)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                btn = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=4,
                    height=2,
                    bg="#ffffff",
                    activebackground="#e0e0e0",
                    command=lambda row=r, col=c: self._handle_click(row, col)
                )
                btn.grid(row=r, column=c, padx=2, pady=2)
                self.buttons[r][c] = btn

        # Panel Lateral de Estado y Controles
        side_panel = tk.Frame(main_frame, bg="#f0f0f0")
        side_panel.pack(side=tk.RIGHT, padx=15, fill=tk.Y)

        self.status_label = tk.Label(
            side_panel,
            text="Turno: X",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#0056b3"
        )
        self.status_label.pack(pady=10)

        # Selector de Modo de Juego
        self.game_mode_var = tk.StringVar(value="IA")
        mode_frame = tk.LabelFrame(side_panel, text="Modo de Juego", font=("Arial", 10, "bold"), bg="#f0f0f0", fg="#333333")
        mode_frame.pack(fill=tk.X, pady=5, padx=5)

        tk.Radiobutton(
            mode_frame, text="Humano vs IA", variable=self.game_mode_var, value="IA",
            bg="#f0f0f0", font=("Arial", 9), command=self._handle_reset
        ).pack(anchor="w", padx=5, pady=2)

        tk.Radiobutton(
            mode_frame, text="Humano vs Humano", variable=self.game_mode_var, value="Humano",
            bg="#f0f0f0", font=("Arial", 9), command=self._handle_reset
        ).pack(anchor="w", padx=5, pady=2)

        # Marco de Métricas para la IA (Día 5)
        metrics_frame = tk.LabelFrame(
            side_panel, 
            text="Métricas de IA (Minimax)", 
            font=("Arial", 10, "bold"), 
            bg="#f0f0f0", 
            fg="#333333"
        )
        metrics_frame.pack(fill=tk.X, pady=10, padx=5)

        self.nodes_label = tk.Label(
            metrics_frame, 
            text="Nodos evaluados: 0", 
            font=("Arial", 9), 
            bg="#f0f0f0", 
            fg="#555555", 
            anchor="w"
        )
        self.nodes_label.pack(fill=tk.X, padx=5, pady=2)

        self.time_label = tk.Label(
            metrics_frame, 
            text="Tiempo: 0.0 ms", 
            font=("Arial", 9), 
            bg="#f0f0f0", 
            fg="#555555", 
            anchor="w"
        )
        self.time_label.pack(fill=tk.X, padx=5, pady=2)

        reset_button = tk.Button(
            side_panel,
            text="Reiniciar Partida",
            font=("Arial", 10),
            bg="#d9534f",
            fg="white",
            activebackground="#c9302c",
            activeforeground="white",
            command=self._handle_reset
        )
        reset_button.pack(fill=tk.X, pady=10)

    def _handle_click(self, row, col):
        if self.controller:
            self.controller.handle_board_click(row, col)

    def _handle_reset(self):
        if self.controller:
            self.controller.handle_reset_click()

    def update_board_ui(self, board_matrix):
        for r in range(3):
            for c in range(3):
                val = board_matrix[r][c]
                self.buttons[r][c].config(text=val)
                if val == "X":
                    self.buttons[r][c].config(fg="#007bff")
                elif val == "O":
                    self.buttons[r][c].config(fg="#dc3545")
                else:
                    self.buttons[r][c].config(fg="#000000")

    def update_status(self, text, color="#0056b3"):
        self.status_label.config(text=text, fg=color)

    def update_metrics(self, nodes, elapsed_ms):
        self.nodes_label.config(text=f"Nodos evaluados: {nodes}")
        self.time_label.config(text=f"Tiempo: {elapsed_ms:.1f} ms")

    def show_message(self, title, message):
        # Ya no se usan ventanas emergentes (MessageBox), se reemplaza por espacio visual o se omite.
        pass