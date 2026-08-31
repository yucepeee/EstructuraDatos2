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

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor

    def get_hijos(self):
        return self._hijos

    def set_hijos(self, hijos):
        self._hijos = hijos

class Arbol:
    def __init__(self, valor):
        self._raiz = Nodo(valor)

    def get_raiz(self):
        return self._raiz

    def set_raiz(self, valor):
        self._raiz = Nodo(valor)

    # -----------------------------------
    # Operaciones basicas del árbol
    # -----------------------------------

    def insertar_Nodo(self, nodo, valor):
        nuevo_nodo = Nodo(valor)
        nodo._hijos.append(nuevo_nodo)

    def es_vacio(self):
        return self._raiz is None

    def es_hoja(self, nodo):
        return len(nodo._hijos) == 0

    def buscar(self, nodo, valor):
        if nodo._valor == valor:
            return nodo
        for hijo in nodo._hijos:
            resultado = self.buscar(hijo, valor)
            if resultado is not None:
                return resultado
        return None

    # dame una funcion que devuelva in_orden del arbol, es decir, que recorra el arbol en orden y devuelva una lista con los valores de los nodos en ese orden

    def in_orden(self):
        resultado = []
        self._in_orden_recursivo(self._raiz, resultado)
        return resultado

    def _in_orden_recursivo(self, nodo, resultado):
        if nodo is not None:
            if len(nodo._hijos) > 0:
                self._in_orden_recursivo(nodo._hijos[0], resultado)
            resultado.append(nodo._valor)
            for hijo in nodo._hijos[1:]:
                self._in_orden_recursivo(hijo, resultado)


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

