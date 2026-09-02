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

        # Mostrar estructura del árbol
        self.mostrar_button = Button(self.frame, text="Estructura del ABB")
        self.mostrar_button.grid(row=2, column=0, padx=5, pady=5)

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

        # Campo de entrada para insertar datos
        self.entry = Entry(self.frame)
        self.entry.grid(row=0, column=2, padx=5, pady=5)

        # Etiqueta para mostrar resultados
        self.result_label = Label(self.frame, text="", font=("Segoe UI", 10))
        self.result_label.grid(row=1, column=2, pady=5, sticky="w")


    def get_entry_value(self):
        """Devuelve el valor ingresado en el campo de texto."""
        return self.entry.get().strip()

    def clear_entry(self):
        """Limpia el campo de texto."""
        self.entry.delete(0, 'end')

    def update_result(self, text):
        """Actualiza la etiqueta con la respuesta obtenida."""
        self.result_label.config(text=f"R: {text}")