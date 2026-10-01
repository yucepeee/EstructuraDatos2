from tkinter import Tk, Label, Button, Frame, Entry

class View:
    def __init__(self, master):
        self.master = master
        master.title("App (ABB)")

        self.frame = Frame(master)
        self.frame.pack()

        """ Botones del ABB. """
        # Insertar
        self.insert_button = Button(self.frame, text="Insertar dato")
        self.insert_button.grid(row=0, column=0, padx=5, pady=5)

        # Buscar dato
        self.buscar_button = Button(self.frame, text="Buscar dato")
        self.buscar_button.grid(row=1, column=0, padx=5, pady=5)

        # Es hoja
        self.es_hoja_button = Button(self.frame, text="Es Hoja?")
        self.es_hoja_button.grid(row=3, column=0, padx=5, pady=5)

        # Altura del árbol
        self.altura_button = Button(self.frame, text="Altura del Árbol")
        self.altura_button.grid(row=4, column=0, padx=5, pady=5)

        # Cantidad de nodos
        self.cantidad_nodos_button = Button(self.frame, text="Cantidad de Nodos")
        self.cantidad_nodos_button.grid(row=5, column=0, padx=5, pady=5)

        # Mostrar inorden
        self.inorden_button = Button(self.frame, text="Mostrar Inorden")
        self.inorden_button.grid(row=6, column=0, padx=5, pady=5)

        # Mostrar preorden
        self.preorden_button = Button(self.frame, text="Mostrar Preorden")
        self.preorden_button.grid(row=7, column=0, padx=5, pady=5)

        # Mostrar postorden
        self.postorden_button = Button(self.frame, text="Mostrar Postorden")
        self.postorden_button.grid(row=8, column=0, padx=5, pady=5)

        # Mostrar recorrido por niveles
        self.recorrido_niveles_button = Button(self.frame, text="Recorrido por Niveles")
        self.recorrido_niveles_button.grid(row=9, column=0, padx=5, pady=5)

        # Mostrar sucesor
        self.sucesor_button = Button(self.frame, text="Sucesor")
        self.sucesor_button.grid(row=10, column=0, padx=5, pady=5)

        # Eliminar nodo
        self.eliminar_button = Button(self.frame, text="Eliminar Nodo")
        self.eliminar_button.grid(row=11, column=0, padx=5, pady=5)

        # Campo de entrada para insertar datos
        self.entry = Entry(self.frame)
        self.entry.grid(row=0, column=2, padx=5, pady=5)

        # Etiqueta para mostrar resultados
        self.result_label = Label(self.frame, text="", font=("Segoe UI", 10))
        self.result_label.grid(row=1, column=2, pady=5, sticky="w")

    """
    Métodos para interactuar con la vista.
    """

    def get_entry_value(self):
        """Devuelve el valor ingresado en el campo de texto."""
        return self.entry.get().strip()

    def update_result(self, text):
        """Actualiza la etiqueta con la respuesta obtenida."""
        self.result_label.config(text=f"R: {text}")