from tkinter import Tk, Label, Button, Frame, Entry, ttk

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("App (ABB)")

        # Frame principale
        self.frame = Frame(master)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        # ---------------------------------------------------------
        # PANEL IZQUIERDO: Botones y Control de Operaciones
        # ---------------------------------------------------------
        self.left_panel = Frame(self.frame)
        self.left_panel.grid(row=0, column=0, sticky="nw", padx=(0, 10))

        # Entrada de datos (Input)
        self.entry_label = Label(self.left_panel, text="Valor del Nodo:", font=("Segoe UI", 9, "bold"))
        self.entry_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 2))

        self.entry = Entry(self.left_panel, width=22)
        self.entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=(0, 10))

        # --- Columna 1 de Botones: Operaciones Básicas ---
        self.insert_button = Button(self.left_panel, text="Insertar dato")
        self.insert_button.grid(row=2, column=0, sticky="we", padx=2, pady=2)

        self.buscar_button = Button(self.left_panel, text="Buscar dato")
        self.buscar_button.grid(row=3, column=0, sticky="we", padx=2, pady=2)

        self.eliminar_button = Button(self.left_panel, text="Eliminar Nodo")
        self.eliminar_button.grid(row=4, column=0, sticky="we", padx=2, pady=2)

        self.sucesor_button = Button(self.left_panel, text="Sucesor")
        self.sucesor_button.grid(row=5, column=0, sticky="we", padx=2, pady=2)

        self.es_hoja_button = Button(self.left_panel, text="Es Hoja?")
        self.es_hoja_button.grid(row=6, column=0, sticky="we", padx=2, pady=2)

        # --- Columna 2 de Botones: Consultas y Recorridos ---
        self.altura_button = Button(self.left_panel, text="Altura del Árbol")
        self.altura_button.grid(row=2, column=1, sticky="we", padx=2, pady=2)

        self.cantidad_nodos_button = Button(self.left_panel, text="Cantidad de Nodos")
        self.cantidad_nodos_button.grid(row=3, column=1, sticky="we", padx=2, pady=2)

        self.inorden_button = Button(self.left_panel, text="Mostrar Inorden")
        self.inorden_button.grid(row=4, column=1, sticky="we", padx=2, pady=2)

        self.preorden_button = Button(self.left_panel, text="Mostrar Preorden")
        self.preorden_button.grid(row=5, column=1, sticky="we", padx=2, pady=2)

        self.postorden_button = Button(self.left_panel, text="Mostrar Postorden")
        self.postorden_button.grid(row=6, column=1, sticky="we", padx=2, pady=2)

        self.recorrido_niveles_button = Button(self.left_panel, text="Recorrido por Niveles")
        self.recorrido_niveles_button.grid(row=7, column=0, columnspan=2, sticky="we", padx=2, pady=2)

        # Etiqueta para mostrar resultados
        self.result_label = Label(self.left_panel, text="R: -", font=("Segoe UI", 9, "italic"), wraplength=200, justify="left")
        self.result_label.grid(row=8, column=0, columnspan=2, sticky="w", pady=(10, 0))

        # ---------------------------------------------------------
        # PANEL DERECHO: Visualización del Árbol (Treeview)
        # ---------------------------------------------------------
        self.tree_frame = Frame(self.frame)
        self.tree_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        # Configurar expansión proporcional de la columna derecha
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.tree_frame, height=15)
        self.tree.heading('#0', text='Estructura ABB', anchor='w')
        self.tree.pack(side="left", fill="both", expand=True)

        # Scrollbar vertical
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

    # ---------------------------------------------------------
    # Métodos para interactuar con la vista
    # ---------------------------------------------------------
    def get_entry_value(self):
        """Devuelve el valor ingresado en el campo de texto."""
        return self.entry.get().strip()

    def update_result(self, text):
        """Actualiza la etiqueta con la respuesta obtenida."""
        self.result_label.config(text=f"R: {text}")

    def clear_entry(self):
        """Limpia el campo de texto."""
        self.entry.delete(0, 'end')

    def limpiar_treeview(self):
        """Elimina todos los elementos del Treeview."""
        for item in self.tree.get_children():
            self.tree.delete(item)