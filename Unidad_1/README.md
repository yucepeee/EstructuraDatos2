
# Unidad I: Árboles Binarios de Búsqueda

Implementación en Python de un **árbol binario de búsqueda (ABB)** como parte de la Unidad I de la asignatura **Estructura de Datos 2**.

## Contenido

- [Concepto general](#concepto-general)
- [Terminología](#terminología)
- [Funcionamiento de un ABB](#funcionamiento-de-un-abb)
- [Recorrido inorden](#recorrido-inorden)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Ejecución](#ejecución)

## Concepto general

Un árbol binario es una estructura de datos no lineal formada por nodos. Cada nodo puede tener como máximo dos hijos: un **hijo izquierdo** y un **hijo derecho**.

Un **árbol binario de búsqueda** organiza sus elementos siguiendo esta regla:

- Los valores menores que el nodo actual se almacenan en el subárbol izquierdo.
- Los valores mayores o iguales se almacenan en el subárbol derecho.

Esta organización permite insertar y buscar elementos comparándolos desde la raíz y avanzando únicamente por la rama que puede contener el valor buscado.

## Terminología

| Término | Definición |
| --- | --- |
| **Nodo** | Elemento que almacena un dato y referencias a sus hijos. |
| **Raíz** | Primer nodo del árbol; no tiene padre. |
| **Padre** | Nodo que apunta a uno o más nodos descendientes. |
| **Hijo** | Nodo conectado directamente con otro nodo padre. |
| **Hoja** | Nodo que no tiene hijos. |
| **Subárbol** | Árbol formado por un nodo y todos sus descendientes. |
| **Nivel** | Distancia de un nodo respecto a la raíz. |
| **Altura** | Longitud del camino más largo desde un nodo hasta una hoja. |
| **Clave** | Valor utilizado para comparar y ordenar los nodos. |

## Funcionamiento de un ABB

La clase `arbolB` utiliza la clase `Node` para representar cada elemento. La inserción comienza en la raíz y compara el nuevo valor con cada nodo:

1. Si el árbol está vacío, el nuevo nodo se convierte en la raíz.
2. Si el valor es menor, se continúa por el hijo izquierdo.
3. Si el valor es mayor o igual, se continúa por el hijo derecho.
4. Cuando se encuentra una posición vacía, se enlaza el nuevo nodo.

Ejemplo de los valores insertados en el programa:

```text
							15
						/    \
					 6      20
					/ \    /  \
				 3   9  18   24
				/ \ / \  /
			 1  4 7 12 17
```
