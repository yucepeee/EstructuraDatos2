import tkinter as tk

class GameView:
    def __init__(self, root, controller=None):
        self.root = root
        self.root.title("Tres en Raya - IA & Machine Learning")
        self.root.geometry("580x540")
        self.root.minsize(580, 540)
        self.root.config(bg="#f8f9fa")  # Fondo general limpio y suave
        
        self.controller = controller
        self._create_widgets()

    def set_controller(self, controller):
        """Asocia el controlador a la vista para manejar eventos de usuario."""
        self.controller = controller

    def _create_widgets(self):
        """Configura los elementos visuales con un diseño prolijo y moderno."""
        
        # Título Principal
        title_label = tk.Label(
            self.root, 
            text="Tres en Raya (Tic-Tac-Toe)", 
            font=("Segoe UI", 16, "bold"), 
            bg="#f8f9fa", 
            fg="#212529"
        )
        title_label.pack(pady=12)

        # Contenedor Principal (Divide tablero y panel lateral)
        main_frame = tk.Frame(self.root, bg="#f8f9fa")
        main_frame.pack(expand=True, padx=10, pady=5)

        # Marco del Tablero (Grilla de 3x3 botones con estilo moderno)
        self.board_frame = tk.Frame(main_frame, bg="#dee2e6", bd=1, relief=tk.SOLID)
        self.board_frame.pack(side=tk.LEFT, padx=10)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                btn = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Segoe UI", 26, "bold"),
                    width=3,
                    height=1,
                    bg="#ffffff",
                    activebackground="#e9ecef",
                    relief=tk.FLAT,
                    borderwidth=0,
                    command=lambda row=r, col=c: self._handle_click(row, col)
                )
                # Usamos grid con bordes simulados mediante padx/pady y fondo de grilla
                btn.grid(row=r, column=c, padx=3, pady=3)
                self.buttons[r][c] = btn

        # Panel Lateral de Estado y Controles
        side_panel = tk.Frame(main_frame, bg="#f8f9fa", width=230, height=450)
        side_panel.pack(side=tk.RIGHT, padx=10, fill=tk.Y)
        side_panel.pack_propagate(False)

        # Etiqueta de Estado de Turno
        self.status_label = tk.Label(
            side_panel,
            text="Turno: X (Humano)",
            font=("Segoe UI", 11, "bold"),
            bg="#e2e3e5",
            fg="#0c5460",
            wraplength=210,
            height=2,
            relief=tk.FLAT
        )
        self.status_label.pack(pady=(0, 10), fill=tk.X)

        # Selector de Modos de Juego
        self.game_mode_var = tk.StringVar(value="Minimax")
        mode_frame = tk.LabelFrame(
            side_panel, 
            text=" Modo de Juego ", 
            font=("Segoe UI", 9, "bold"), 
            bg="#f8f9fa", 
            fg="#495057",
            bd=1, relief=tk.GROOVE
        )
        mode_frame.pack(fill=tk.X, pady=4, padx=2)

        for text, val in [("Humano vs IA (Minimax)", "Minimax"), ("Humano vs IA (ML Tree)", "ML"), ("Humano vs Humano", "Humano")]:
            tk.Radiobutton(
                mode_frame, text=text, variable=self.game_mode_var, value=val,
                bg="#f8f9fa", fg="#212529", font=("Segoe UI", 9),
                activebackground="#f8f9fa", selectcolor="#f8f9fa",
                command=self._handle_reset
            ).pack(anchor="w", padx=8, pady=2)

        # Marco de Métricas y Rendimiento
        metrics_frame = tk.LabelFrame(
            side_panel, 
            text=" Métricas de Rendimiento ", 
            font=("Segoe UI", 9, "bold"), 
            bg="#f8f9fa", 
            fg="#495057",
            bd=1, relief=tk.GROOVE
        )
        metrics_frame.pack(fill=tk.X, pady=8, padx=2)

        self.nodes_label = tk.Label(
            metrics_frame, text="Nodos evaluados: 0", 
            font=("Segoe UI", 9), bg="#f8f9fa", fg="#6c757d", anchor="w"
        )
        self.nodes_label.pack(fill=tk.X, padx=8, pady=1)

        self.time_label = tk.Label(
            metrics_frame, text="Latencia: 0.00 ms", 
            font=("Segoe UI", 9), bg="#f8f9fa", fg="#6c757d", anchor="w"
        )
        self.time_label.pack(fill=tk.X, padx=8, pady=1)

        self.comp_label = tk.Label(
            metrics_frame, text="Precisión ML: --%", 
            font=("Segoe UI", 8, "italic"), bg="#f8f9fa", fg="#155724", 
            anchor="w", justify=tk.LEFT, height=2
        )
        self.comp_label.pack(fill=tk.X, padx=8, pady=2)

        # Botón de Comparativa
        self.benchmark_button = tk.Button(
            side_panel,
            text="Comparar Minimax vs ML",
            font=("Segoe UI", 9, "bold"),
            bg="#17a2b8",
            fg="white",
            activebackground="#138496",
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2",
            command=self._handle_benchmark
        )
        self.benchmark_button.pack(fill=tk.X, pady=5, padx=2, ipady=4)

        # Botón de Reiniciar
        self.reset_button = tk.Button(
            side_panel,
            text="Reiniciar Partida",
            font=("Segoe UI", 9, "bold"),
            bg="#dc3545",
            fg="white",
            activebackground="#c82333",
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2",
            command=self._handle_reset
        )
        self.reset_button.pack(fill=tk.X, pady=5, padx=2, ipady=4)

    def _handle_click(self, row, col):
        if self.controller:
            self.controller.handle_board_click(row, col)

    def _handle_reset(self):
        if self.controller:
            self.controller.handle_reset_click()

    def _handle_benchmark(self):
        if self.controller:
            self.controller.handle_benchmark_click()

    def update_board_ui(self, board_matrix):
        for r in range(3):
            for c in range(3):
                val = board_matrix[r][c]
                self.buttons[r][c].config(text=val)
                if val == "X":
                    self.buttons[r][c].config(fg="#007bff", bg="#f8f9fa")
                elif val == "O":
                    self.buttons[r][c].config(fg="#dc3545", bg="#f8f9fa")
                else:
                    self.buttons[r][c].config(text="", bg="#ffffff")

    def update_status(self, text, color="#0c5460"):
        self.status_label.config(text=text, fg=color)

    def update_metrics(self, nodes, elapsed_ms, extra_info=None):
        self.nodes_label.config(text=f"Nodos evaluados: {nodes}")
        self.time_label.config(text=f"Latencia: {elapsed_ms:.2f} ms")
        if extra_info is not None:
            self.comp_label.config(text=extra_info)