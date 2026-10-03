import tkinter as tk
from tkinter import messagebox

class GameView:
    def __init__(self, root, controller=None):
        self.root = root
        self.root.title("Tres en Raya ")
        self.root.geometry("500x400")
        self.root.config(bg="#f0f0f0")
        
        self.controller = controller
        
        self._create_widgets()

    def set_controller(self, controller):
        """Asocia el controlador a la vista para manejar eventos de usuario."""
        self.controller = controller

    def _create_widgets(self):
        """Configura los elementos visuales de la ventana principal."""
        # Título principal
        title_label = tk.Label(
            self.root, 
            text="Tres en Raya (Tic-Tac-Toe)", 
            font=("Arial", 18, "bold"), 
            bg="#f0f0f0", 
            fg="#333333"
        )
        title_label.pack(pady=10)

        # Contenedor principal para dividir tablero y panel lateral
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
        self.status_label.pack(pady=20)

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
        reset_button.pack(fill=tk.X, pady=5)

    def _handle_click(self, row, col):
        """Notifica al controlador cuando el usuario hace clic en una casilla."""
        if self.controller:
            self.controller.handle_board_click(row, col)

    def _handle_reset(self):
        """Notifica al controlador para reiniciar el juego."""
        if self.controller:
            self.controller.handle_reset_click()

    def update_board_ui(self, board_matrix):
        """Actualiza el texto y estado visual de los botones según la matriz del modelo."""
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
        """Actualiza el texto del panel de estado lateral."""
        self.status_label.config(text=text, fg=color)

    def show_message(self, title, message):
        """Muestra una ventana emergente (MessageBox) con resultados o avisos."""
        messagebox.showinfo(title, message)