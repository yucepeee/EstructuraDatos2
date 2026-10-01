class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Conectar los botones de la vista con los métodos del controlador
        self.view.insert_button.config(command=self.insert)
        self.view.buscar_button.config(command=self.buscar)
        self.view.es_hoja_button.config(command=self.es_hoja)
        self.view.altura_button.config(command=self.altura)
        self.view.cantidad_nodos_button.config(command=self.cantidad_nodos)
        self.view.inorden_button.config(command=self.inorden)
        self.view.preorden_button.config(command=self.preorden)
        self.view.postorden_button.config(command=self.postorden)
        self.view.recorrido_niveles_button.config(command=self.recorrido_niveles)
        self.view.sucesor_button.config(command=self.sucesor)
        self.view.eliminar_button.config(command=self.eliminar)

    """
    Métodos del controlador para manejar la lógica de la aplicación.
    """

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

    def insert(self):
        val = self._obtener_valor_numerico()
        if val is not None:
            if self.model.insertar(val):
                self.view.update_result(f"Nodo '{val}' insertado.")
                self.dibujar_estructura()  # Actualiza el Treeview al insertar
            else:
                self.view.update_result(f"El nodo '{val}' ya existe.")
            self.view.clear_entry()

    def buscar(self):
        val = self._obtener_valor_numerico()
        if val is not None:
            encontrado = self.model.buscar(val)
            res = f"El nodo {val} Si existe." if encontrado else f"El nodo {val} No existe."
            self.view.update_result(res)

    def es_hoja(self):
        val = self._obtener_valor_numerico()
        if val is not None:
            resultado = self.model.es_hoja(val)
            if resultado is None:
                self.view.update_result(f"El nodo {val} no fue encontrado.")
            elif resultado:
                self.view.update_result(f"El nodo {val} Es una hoja.")
            else:
                self.view.update_result(f"El nodo {val} No es una hoja.")


    def altura(self):
        h = self.model.altura()
        self.view.update_result(f"Altura del árbol = {h}")

    def cantidad_nodos(self):
        cant = self.model.cantidad_nodos()
        self.view.update_result(f"Cantidad de nodos = {cant}")

    def inorden(self):
        res = self.model.inorden()
        self.view.update_result(f"InOrden: {res}")

    def preorden(self):
        res = self.model.preorden()
        self.view.update_result(f"PreOrden: {res}")

    def postorden(self):
        res = self.model.postorden()
        self.view.update_result(f"PostOrden: {res}")

    def recorrido_niveles(self):
        res = self.model.recorrido_niveles()
        self.view.update_result(f"Recorrido por niveles: {res}")

    def sucesor(self):
        val = self._obtener_valor_numerico()
        if val is not None:
            sucesor = self.model.sucesor(val)
            if sucesor is None:
                self.view.update_result(f"No se encontró sucesor para el nodo {val}.")
            else:
                self.view.update_result(f"El sucesor de {val} es {sucesor}.")

    def eliminar(self):
        val = self._obtener_valor_numerico()
        if val is not None:
            eliminado = self.model.eliminar(val)
            if eliminado:
                self.view.update_result(f"Nodo '{val}' eliminado correctamente.")
            else:
                self.view.update_result(f"El nodo '{val}' no existe en el árbol.")
            self.view.clear_entry()

    def dibujar_estructura(self):
        """Limpia y vuelve a cargar la estructura jerárquica en el Treeview."""
        self.view.limpiar_treeview()
        if self.model.raiz is not None:
            self._cargar_treeview_recursivo(self.model.raiz, padre="")

    def _cargar_treeview_recursivo(self, nodo, padre=""):
        if nodo is None:
            return

        # Generamos un ID único para cada item utilizando su ID en memoria
        id_nodo = str(id(nodo))
        etiqueta = f"Nodo: {nodo.valor}" if padre == "" else f"{nodo.valor}"

        # Insertar el nodo actual en el Treeview y expandir por defecto
        self.view.tree.insert(padre, 'end', id_nodo, text=etiqueta, open=True)

        # Recorrido recursivo para ramas izquierda y derecha
        if nodo.izquierda:
            self._cargar_treeview_recursivo(nodo.izquierda, id_nodo)
        if nodo.derecha:
            self._cargar_treeview_recursivo(nodo.derecha, id_nodo)