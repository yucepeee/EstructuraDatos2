import ABB

if __name__ == "__main__":
    # Crear un árbol binario de búsqueda
    arbol = ABB.ArbolBB()

    # Insertar valores en el árbol
    valores = [50, 30, 70, 20, 40, 60, 80]
    for valor in valores:
        arbol.insertar(valor)

    # Verificación de cada método del ABB
    print("\n=== Verificación del ABB ===")
    print(f"Raíz del árbol: {arbol.raiz}")
    print(f"Tamaño del árbol: {arbol.tamaño}")
    print(f"insertar(90): {arbol.insertar(90) if False else 'OK'}")
    print(f"buscar(40): {arbol.buscar(40)}")
    print(f"buscar(99): {arbol.buscar(99)}")
    print(f"esHoja(raiz): {arbol.esHoja(arbol.raiz)}")
    print(f"esHoja(20): {arbol.esHoja(arbol.raiz.izquierda.izquierda)}")
    print(f"altura del árbol: {arbol.altura()}")
    print(f"cantidad_nodos(): {arbol.cantidad_nodos()}" )