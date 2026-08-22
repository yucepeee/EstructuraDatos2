""" Árbol Binario (ABB) 
-------------------------
Implementación de un Árbol Binario de Búsqueda (ABB) en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 2

Profesor: Ing. Juan Carlos Peinado Pereira

Fecha: 21/08/2026 """

class Nodo:
    """ Clase Nodo para representar cada nodo del árbol binario. """

    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None  
        self.derecha = None

class ABB:
    """ Clase Árbol Binario de Búsqueda (ABB). """

    def __init__(self):
        self.raiz = None
        self.tamaño = 0

    #   -------------------------------------------------
    #   Operaciones básicas del ABB
    #   -------------------------------------------------

    def insertar(self, valor):
        """ Inserta un nuevo valor en el ABB. """

        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
        self.tamaño += 1

    def _insertar_recursivo(self, nodo_actual, valor):
        """ Método auxiliar para insertar un valor de manera recursiva. """

        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)
        # Si el valor ya existe, no se hace nada (no se permiten duplicados).
    
    def eliminar(self, valor):
        """ Elimina un valor del ABB. """

        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual, valor):
        """ Método auxiliar para eliminar un valor de manera recursiva. """

        if nodo_actual is None:
            return nodo_actual

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, valor)
        else:
            # Nodo encontrado
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda

            # Nodo con dos hijos: obtener el sucesor (mínimo en el subárbol derecho)
            sucesor = self._minimo(nodo_actual.derecha)
            nodo_actual.valor = sucesor.valor
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, sucesor.valor)

        return nodo_actual

    def buscar(self, valor):
        """ Busca un valor en el árbol. 

            return:
                True si el dato existe, False si no existe.

        """

        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        """ Método auxiliar para buscar un valor de manera recursiva. """

        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierda, valor)
        return self._buscar_recursivo(nodo_actual.derecha, valor)

    def esta_vacio(self):
        """ Verifica si el árbol está vacío. """

        return self.raiz is None

    def raiz(self):
        """ Devuelve el valor de la raíz del árbol. """

        if self.raiz is not None:
            return self.raiz.valor
        return None