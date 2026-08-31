""" Arbol Binario
-------------------------
Implementación de un Árbol Binario  

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 2

Profesor: Ing. Juan Carlos Peinado Pereira

Fecha: 29/08/2026 """

class Nodo:
    def __init__(self, valor):
        self._valor = valor
        self._hijos = []

    """ Metodos de acceso para los atributos del nodo. """

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor

    def get_hijos(self):
        return self._hijos

    def set_hijos(self, hijos):
        self._hijos = hijos

class Arbol:
    """ Clase Árbol Binario. """
    def __init__(self, valor):
        self._raiz = Nodo(valor)

    """ Metodos de acceso para los atributos del árbol. """

    def get_raiz(self):
        return self._raiz

    def set_raiz(self, valor):
        self._raiz = Nodo(valor)

    # -----------------------------------
    # Operaciones basicas del árbol
    # -----------------------------------

    def insertar_Nodo(self, nodo, valor):
        """ Inserta un nuevo nodo con el valor dado como hijo del nodo especificado. """

        nuevo_nodo = Nodo(valor)
        nodo._hijos.append(nuevo_nodo)

    def es_vacio(self):
        """ Verifica si el árbol está vacío. """

        return self._raiz is None

    def es_hoja(self, nodo):
        """ Verifica si un nodo es hoja (no tiene hijos). """

        return len(nodo._hijos) == 0

    def buscar(self, nodo, valor):
        """ Busca un nodo con el valor dado en el árbol. """

        if nodo._valor == valor:
            return nodo
        for hijo in nodo._hijos:
            resultado = self.buscar(hijo, valor)
            if resultado is not None:
                return resultado
        return None

    def in_orden(self):
        """ Realiza un recorrido in-orden del árbol y devuelve una lista de los valores. """

        resultado = []
        self._in_orden_recursivo(self._raiz, resultado)
        return resultado

    def _in_orden_recursivo(self, nodo, resultado):
        """ Método auxiliar para el recorrido in-orden de manera recursiva. """

        if nodo is not None:
            if len(nodo._hijos) > 0:
                self._in_orden_recursivo(nodo._hijos[0], resultado)
            resultado.append(nodo._valor)
            for hijo in nodo._hijos[1:]:
                self._in_orden_recursivo(hijo, resultado)


# Ejemplo de uso del árbol binario

if __name__ == "__main__":
    # Crear un árbol binario
    arbol = Arbol(1)

    # Insertar nodos en el árbol
    arbol.insertar_Nodo(arbol.get_raiz(), 2)
    arbol.insertar_Nodo(arbol.get_raiz(), 3)
    arbol.insertar_Nodo(arbol.get_raiz().get_hijos()[0], 4)
    arbol.insertar_Nodo(arbol.get_raiz().get_hijos()[0], 5)
    arbol.insertar_Nodo(arbol.get_raiz().get_hijos()[1], 6)

    # Verificación de cada método del árbol
    print("\n=== Verificación del Árbol ===")
    print(f"Raíz del árbol: {arbol.get_raiz().get_valor()}")
    print(f"Es vacío: {arbol.es_vacio()}")
    print(f"Es hoja (raíz): {arbol.es_hoja(arbol.get_raiz())}")
    print(f"Es hoja (nodo 4): {arbol.es_hoja(arbol.get_raiz().get_hijos()[0].get_hijos()[0])}")
    print(f"Buscar nodo con valor 5: {arbol.buscar(arbol.get_raiz(), 5).get_valor()}")
    print(f"Buscar nodo con valor 10: {arbol.buscar(arbol.get_raiz(), 10)}")
    print(f"In-orden del árbol: {arbol.in_orden()}")

