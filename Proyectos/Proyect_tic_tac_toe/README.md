# Proyecto: Árbol Binario de Búsqueda (ABB)

Aplicación sencilla desarrollada en Python para trabajar con un **Árbol Binario de Búsqueda (ABB)** mediante una interfaz gráfica construida con Tkinter.

## Descripción

Un ABB organiza sus elementos de acuerdo con la siguiente regla:

- Los valores menores que un nodo se almacenan en su subárbol izquierdo.
- Los valores mayores se almacenan en su subárbol derecho.
- No se permiten valores duplicados.

Esta organización permite realizar búsquedas siguiendo únicamente la rama en la que podría encontrarse el valor.

## Funcionalidades

La aplicación permite:


## Requisitos

- Python 3.
- Tkinter, incluido normalmente en la instalación estándar de Python.

El archivo `requirements.txt` no requiere paquetes externos.

## Ejecución

Desde la carpeta raíz del proyecto, ejecuta:

```bash
python src/main.py
```

Luego ingresa un número entero en el campo de texto y selecciona la operación que deseas realizar.

## Operaciones del modelo

La clase `ArbolBB` ofrece los siguientes métodos principales:

| Método | Descripción |
| --- | --- |
| `insertar(valor)` | Inserta un valor si todavía no existe. |
| `buscar(valor)` | Devuelve `True` si el valor está en el árbol. |
| `es_hoja(valor)` | Indica si el nodo encontrado no tiene hijos. |
| `altura()` | Devuelve la altura del árbol. |
| `cantidad_nodos()` | Devuelve el total de nodos almacenados. |
| `inorden()` | Recorre izquierda, raíz y derecha. |
| `preorden()` | Recorre raíz, izquierda y derecha. |
| `postorden()` | Recorre izquierda, derecha y raíz. |

## Autor

- **Nombre:** Gabriel Romulo Arnez Joven
- **Registro:** 220000417
- **Materia:** Estructura de Datos 2
- **Docente:** Ing. Juan Carlos Peinado Pereira
