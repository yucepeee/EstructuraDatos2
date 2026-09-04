class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Conectar los botones de la vista con los métodos del controlador
        self.view.insert_button.config(command=self.handle_insert)
        self.view.buscar_button.config(command=self.handle_buscar)
        self.view.es_hoja_button.config(command=self.handle_es_hoja)
        self.view.altura_button.config(command=self.handle_altura)
        self.view.cantidad_nodos_button.config(command=self.handle_cantidad_nodos)
        self.view.inorden_button.config(command=self.handle_inorden)
        self.view.preorden_button.config(command=self.handle_preorden)
        self.view.postorden_button.config(command=self.handle_postorden)

    def _obtener_valor_numerico(self):
        text = self.view.get_entry_value()
        if not text:
            self.view.update_result("Por favor, ingresa un número.")
            return None
        try:
            return int(text)
        except ValueError:
            self.view.update_result("Debe ser un número entero válido.")
            return None

    def handle_insert(self):
        val = self._obtener_valor_numerico()
        if val is not None:
            exito = self.model.insertar(val)
            if exito:
                self.view.update_result(f"Nodo '{val}' insertado correctamente.")
            else:
                self.view.update_result(f"El nodo '{val}' ya existe en el árbol.")
            self.view.clear_entry()

    def handle_buscar(self):
        val = self._obtener_valor_numerico()
        if val is not None:
            encontrado = self.model.buscar(val)
            res = f"El nodo {val} Si existe." if encontrado else f"El nodo {val} No existe."
            self.view.update_result(res)

    def handle_es_hoja(self):
        val = self._obtener_valor_numerico()
        if val is not None:
            resultado = self.model.es_hoja(val)
            if resultado is None:
                self.view.update_result(f"El nodo {val} no fue encontrado.")
            elif resultado:
                self.view.update_result(f"El nodo {val} Es una hoja.")
            else:
                self.view.update_result(f"El nodo {val} No es una hoja.")


    def handle_altura(self):
        h = self.model.altura()
        self.view.update_result(f"Altura del árbol = {h}")

    def handle_cantidad_nodos(self):
        cant = self.model.cantidad_nodos()
        self.view.update_result(f"Cantidad de nodos = {cant}")

    def handle_inorden(self):
        res = self.model.inorden()
        self.view.update_result(f"Inorden: {res}")

    def handle_preorden(self):
        res = self.model.preorden()
        self.view.update_result(f"Preorden: {res}")

    def handle_postorden(self):
        res = self.model.postorden()
        self.view.update_result(f"Postorden: {res}")