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
        self.raiz = Nodo(valor)

    def get_raiz(self):
        return self.raiz

    def set_raiz(self, valor):
        self.raiz = Nodo(valor)

    # -----------------------------------
    # Operaciones basicas del árbol
    # -----------------------------------

    def insertar_Nodo(self, nodo, valor):
        nuevo_nodo = Nodo(valor)
        nodo._hijos.append(nuevo_nodo)

    def es_vacio(self):
        return self.raiz is None

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


