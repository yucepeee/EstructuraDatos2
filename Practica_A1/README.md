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

- Insertar números enteros en el ABB.
- Buscar un valor y comprobar si existe.
- Verificar si un nodo es una hoja.
- Consultar la altura del árbol.
- Consultar la cantidad de nodos.
- Mostrar los recorridos inorden, preorden y postorden.
- Informar cuando se intenta insertar un valor duplicado o cuando un valor no existe.

## Ejemplo de estructura

Al insertar los valores `[50, 30, 70, 20, 40, 60, 80]`, el árbol queda así:

```text
             50
           /    \
          30     70
        /  \    /  \
       20  40  60  80
```

El recorrido inorden de este árbol produce los valores ordenados:

```text
[20, 30, 40, 50, 60, 70, 80]
```

## Estructura del proyecto

```text
Practica_A1/
├── README.md
├── requirements.txt
└── src/
    ├── main.py
    ├── controllers/
    │   └── controller.py
    ├── models/
    │   └── model.py
    └── views/
        └── view.py
```

### Componentes principales

- `src/models/model.py`: contiene las clases `Nodo` y `ArbolBB`, junto con la lógica del ABB.
- `src/controllers/controller.py`: conecta las acciones de la interfaz con las operaciones del árbol y valida los datos ingresados.
- `src/views/view.py`: define la ventana, el campo de entrada, los botones y la presentación de resultados.
- `src/main.py`: inicia la aplicación y conecta el modelo, la vista y el controlador.

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
