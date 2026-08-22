# Unidad I: Árboles Binarios de Búsqueda

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
        /  \    /  \
       3    9  18   24
      / \  / \  /
     1  4 7  12 17
```

  ## Operaciones básicas

  La clase `ABB` incluye las siguientes operaciones principales:

  | Operación | Descripción |
  | --- | --- |
  | `insertar(valor)` | Agrega un valor al árbol. No se permiten valores duplicados. |
  | `buscar(valor)` | Verifica si un valor existe y devuelve `True` o `False`. |
  | `eliminar(valor)` | Elimina un valor del árbol si se encuentra. |
  | `esta_vacio()` | Verifica si el árbol no contiene elementos. |

	### `insertar(valor)`

    Al insertar los valores `15`, `6` y `20`, el árbol queda así:

    ```text
      15
     /  \
    6    20
    ```

    Al insertar el valor `3`, como es menor que `15` y menor que `6`, se coloca
    en el subárbol izquierdo de `6`:

    ```text
      15
     /  \
    6    20
      /
     3
    ```

    ### `buscar(valor)`

    Para buscar el valor `9`, se realizan estas comparaciones:

    ```text
    9 > 6  -> avanzar al subárbol derecho
    9 < 15 -> avanzar al subárbol izquierdo

      15
     /  \
    6    20
     \
      9  <- valor encontrado
    ```

    Si se busca el valor `10`, se sigue el mismo camino, pero no se encuentra
    ningún nodo con ese valor:

    ```text
    10 < 15 -> avanzar a la izquierda
    10 > 6  -> avanzar a la derecha
    10 > 9  -> avanzar a la derecha
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
