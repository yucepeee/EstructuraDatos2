""" Árbol Binario (ABB) 
-------------------------
Implementación de un Árbol Binario de Búsqueda (ABB) en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 2

Profesor: Ing. Juan Carlos Peinado Pereira

Fecha: 31/08/2026 """

class Nodo:
    """ Clase Nodo para representar cada nodo del árbol binario. """

    def __init__(self, valor):
        self._valor = valor
        self._izquierda = None
        self._derecha = None

    def __repr__(self):
        return f"Nodo({self._valor})"

    """ Metodos de acceso para los atributos del nodo. """

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def izquierda(self):
        return self._izquierda

    @izquierda.setter
    def izquierda(self, valor):
        self._izquierda = valor

    @property
    def derecha(self):
        return self._derecha

    @derecha.setter
    def derecha(self, valor):
        self._derecha = valor

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor


class ArbolBB:
    """ Clase Árbol Binario de Búsqueda (ABB). """

    def __init__(self):
        self._raiz = None
        self._tamaño = 0

    """ Metodos de acceso para los atributos del árbol. """

    @property
    def raiz(self):
        return self._raiz

    @raiz.setter
    def raiz(self, valor):
        if valor is not None and not isinstance(valor, Nodo):
            raise TypeError("La raíz debe ser un Nodo o None.")
        self._raiz = valor

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, valor):
        if not isinstance(valor, int):
            raise TypeError("El tamaño debe ser un entero.")
        if valor < 0:
            raise ValueError("El tamaño no puede ser negativo.")
        self._tamaño = valor

    #   -------------------------------------------------
    #   Operaciones básicas del ABB
    #   -------------------------------------------------

    def insertar(self, valor):
        """ Inserta un nuevo valor en el ABB manteniendo 
            la propiedad del árbol binario de búsqueda.
        """
        if self._raiz is None:
            self._raiz = Nodo(valor)
            self._tamaño += 1
            return

        if self._insertar_recursivo(self._raiz, valor):
            self._tamaño += 1

    def _insertar_recursivo(self, nodo, valor):
        """ Método auxiliar para insertar un valor de manera recursiva.
        
        """
        if valor < nodo._valor:
            if nodo._izquierda is None:
                nodo._izquierda = Nodo(valor)
                return True
            return self._insertar_recursivo(nodo._izquierda, valor)
        elif valor > nodo._valor:
            if nodo._derecha is None:
                nodo._derecha = Nodo(valor)
                return True
            return self._insertar_recursivo(nodo._derecha, valor)
        # Si el valor ya existe, no se hace nada (no se permiten duplicados).

    def buscar(self, valor):
        """ Busca un valor en el ABB. Devuelve True si se encuentra, 
            de lo contrario devuelve False.
        """
        return self._buscar_recursivo(self._raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        """ Método auxiliar para buscar un valor de manera recursiva. 
        """
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def esHoja(self, nodo):
        """ Verifica si un nodo es hoja (no tiene hijos).
    """
        if nodo is None:
            return False
        return nodo.izquierda is None and nodo.derecha is None

    def altura(self):
        """ Calcula la altura del ABB."""

        return self._altura_recursiva(self._raiz)

    def _altura_recursiva(self, nodo):
        """ Método auxiliar para calcular la altura de manera recursiva. """

        if nodo is None:
            return 0
        return 1 + max(self._altura_recursiva(nodo._izquierda), self._altura_recursiva(nodo._derecha))

    def cantidad_nodos(self):
        """ Devuelve la cantidad de nodos en el ABB. """

        return self._tamaño

# Ejemplo de uso del ABB

if __name__ == "__main__":
    # Crear un ABB
    arbol = ArbolBB()

    # Insertar valores en el ABB
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)

    # Buscar valores en el ABB
    print("Buscar 40:", arbol.buscar(40))  # True
    print("Buscar 90:", arbol.buscar(90))  # False

    # Verificar si un nodo es hoja
    nodo_20 = arbol._raiz.izquierda.izquierda  # Nodo con valor 20
    print("Es hoja (20):", arbol.esHoja(nodo_20))  # True

    # Altura del ABB
    print("Altura del ABB:", arbol.altura())  # 3

    # Cantidad de nodos en el ABB
    print("Cantidad de nodos:", arbol.cantidad_nodos())  # 7