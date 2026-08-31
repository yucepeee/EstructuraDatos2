# Unidad I: Árboles Binarios

Este módulo cubre dos estructuras fundamentales de datos con árboles:

1. **Árbol Binario (AB)** - Estructura básica sin restricciones de ordenamiento
2. **Árbol Binario de Búsqueda (ABB)** - Estructura ordenada que facilita búsquedas eficientes

## Árbol Binario (AB)

Un **árbol binario** es una estructura de datos no lineal formada por nodos. Cada nodo puede tener como máximo dos hijos: un **hijo izquierdo** y un **hijo derecho**. No existe restricción en el ordenamiento de los valores.

### Características del Árbol Binario

- Cada nodo contiene un valor
- Cada nodo puede tener 0, 1 o 2 hijos
- No existe restricción de ordenamiento entre padres e hijos
- Es flexible para almacenar datos sin un orden específico

---

## Árbol Binario de Búsqueda (ABB)

Un **árbol binario de búsqueda** es un caso especial de árbol binario que organiza sus elementos siguiendo esta regla:

- Los valores **menores** que el nodo actual se almacenan en el subárbol izquierdo.
- Los valores **mayores o iguales** se almacenan en el subárbol derecho.

Esta organización permite insertar y buscar elementos comparándolos desde la raíz y avanzando únicamente por la rama que puede contener el valor buscado.

## Terminología

| Término | Definición |
| --- | --- |
| **Nodo** | Elemento que almacena un dato y referencias a sus hijos. |
| **Raíz** | Primer nodo del árbol; no tiene padre. |
| **Padre** | Nodo que apunta a uno o más nodos descendientes. |
| **Hijo** | Nodo conectado directamente con otro nodo padre. |
| **Hijo Izquierdo** | Descendiente directo en la rama izquierda de un nodo. |
| **Hijo Derecho** | Descendiente directo en la rama derecha de un nodo. |
| **Hoja** | Nodo que no tiene hijos. |
| **Subárbol** | Árbol formado por un nodo y todos sus descendientes. |
| **Nivel** | Distancia de un nodo respecto a la raíz. |
| **Altura** | Longitud del camino más largo desde un nodo hasta una hoja. |
| **Clave** | Valor utilizado para comparar y ordenar los nodos (en ABB). |

---

## Operaciones del Árbol Binario (AB)

La clase `Arbol` (en `arbolB.py`) utiliza la clase `Nodo` para representar cada elemento. 

### Métodos Principales

| Operación | Descripción |
| --- | --- |
| `insertar_Nodo(nodo, valor)` | Agrega un nuevo nodo como hijo del nodo especificado. |
| `buscar(nodo, valor)` | Busca un valor en el árbol desde un nodo dado. Devuelve el nodo si lo encuentra. |
| `es_vacio()` | Verifica si el árbol está vacío. |
| `es_hoja(nodo)` | Verifica si un nodo es hoja (no tiene hijos). |
| `in_orden()` | Realiza un recorrido in-orden del árbol. |

### Ejemplo de Árbol Binario

```
      1
     / \
    2   3
   / \
  4   5 
   \
    6
```

**Creación y inserción:**

```python
arbol = Arbol(1)
arbol.insertar_Nodo(arbol.get_raiz(), 2)           # Hijo izquierdo de 1
arbol.insertar_Nodo(arbol.get_raiz(), 3)           # Hijo derecho de 1
arbol.insertar_Nodo(arbol.get_raiz().get_hijos()[0], 4)  # Hijo izquierdo de 2
arbol.insertar_Nodo(arbol.get_raiz().get_hijos()[0], 5)  # Hijo derecho de 2
arbol.insertar_Nodo(arbol.get_raiz().get_hijos()[0].get_hijos()[0], 6)  # Hijo de 4
```

**Búsqueda y validaciones:**

```python
resultado = arbol.buscar(arbol.get_raiz(), 5)  # Encuentra el nodo con valor 5
print(arbol.es_vacio())                        # False
print(arbol.es_hoja(arbol.get_raiz()))        # False (tiene hijos)
```

---



## Operaciones del Árbol Binario de Búsqueda (ABB)

La clase `ArbolBB` (en `ABB.py`) implementa un árbol binario de búsqueda con restricciones de ordenamiento.

### Métodos Principales

| Operación | Descripción |
| --- | --- |
| `insertar(valor)` | Agrega un valor al árbol manteniendo la propiedad ABB. No se permiten duplicados. |
| `buscar(valor)` | Verifica si un valor existe en el árbol. Devuelve `True` o `False`. |
| `esHoja(nodo)` | Verifica si un nodo es hoja (no tiene hijos). |
| `altura()` | Calcula la altura total del árbol. |
| `cantidad_nodos()` | Devuelve el número total de nodos. |

### Funcionamiento de un ABB

La inserción comienza en la raíz y compara el nuevo valor con cada nodo:

1. Si el árbol está vacío, el nuevo nodo se convierte en la raíz.
2. Si el valor es menor, se continúa por el hijo izquierdo.
3. Si el valor es mayor, se continúa por el hijo derecho.
4. Cuando se encuentra una posición vacía, se enlaza el nuevo nodo.

Ejemplo de los valores insertados en orden [50, 30, 70, 20, 40, 60, 80]:

```text
             50
           /    \
          30     70
        /  \    /  \
       20  40  60  80
```

### `insertar(valor)`

Al insertar el valor `30` en un ABB con raíz `50`:
- Como 30 < 50, se coloca en el subárbol izquierdo

```text
      50
     /
    30
```

Al insertar `70` (70 > 50), se coloca a la derecha:

```text
      50
     /  \
    30   70
```

Al insertar `20` (20 < 50 y 20 < 30), se coloca a la izquierda de 30:

```text
      50
     /  \
    30   70
   /
  20
```

### `buscar(valor)`

Para buscar el valor `40` en el ABB:

```text
40 < 50  -> avanzar al subárbol izquierdo
40 > 30  -> avanzar al subárbol derecho

      50
     /  \
    30   70
   / \
  20 40  <- valor encontrado
```

Si se busca el valor `25`, se sigue el mismo camino pero no se encuentra:

```text
25 < 50 -> avanzar a la izquierda
25 < 30 -> avanzar a la izquierda
25 > 20 -> avanzar a la derecha (no hay nodo)
        -> valor no existe
```

### Ejemplo de Uso del ABB

```python
arbol = ArbolBB()

# Insertar valores
valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    arbol.insertar(valor)

# Búsqueda
print(arbol.buscar(40))   # True
print(arbol.buscar(90))   # False

# Altura
print(arbol.altura())      # 3

# Cantidad de nodos
print(arbol.cantidad_nodos())  # 7
```
    None    -> valor no encontrado
    ```

    ### `eliminar(valor)`

    Antes de eliminar el valor `6`:

    ```text
      15
     /  \
    6    20
      / \
     3   9
    ```

    Después de eliminarlo, sus hijos se reorganizan y el árbol queda así:

    ```text
      15
     /  \
    9    20
      /
     3
    ```

    ### `esta_vacio()`

    Un ABB recién creado no tiene raíz:

    ```text
    ABB vacío
    raíz: None
    ```

    Después de insertar un valor, deja de estar vacío:

    ```text
     15
    ```
