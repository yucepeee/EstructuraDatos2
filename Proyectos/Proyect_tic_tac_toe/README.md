# Proyecto: Tres en Raya (Tic-Tac-Toe)

Juego clásico de tres en raya desarrollado en Python con interfaz gráfica usando Tkinter y siguiendo un patrón MVC (Modelo-Vista-Controlador).

## Descripción

La aplicación permite jugar partidas de tres en raya entre dos jugadores (`X` y `O`) en un tablero 3x3. El estado del juego se gestiona en el modelo, la interfaz se dibuja en la vista y las interacciones del usuario se procesan en el controlador.

La lógica del juego incluye:

- Alternancia de turnos entre `X` y `O`
- Verificación automática de ganador por filas, columnas o diagonales
- Detección de empate cuando el tablero se llena
- Botón para reiniciar la partida
- Indicador visual de turno y resultado

## Estructura del proyecto

```text
src/
├── main.py
├── controllers/
│   └── game_controller.py
├── models/
│   └── game_model.py
└── views/
    └── gui_view.py
```

## Funcionalidades

La aplicación permite:

- Hacer clic en cualquier casilla del tablero para jugar
- Evitar movimientos inválidos en casillas ocupadas
- Mostrar el turno actual en la interfaz
- Determinar si hubo ganador o empate
- Reiniciar la partida en cualquier momento

## Requisitos

- Python 3
- Tkinter, incluido normalmente en la instalación estándar de Python

El archivo `requirements.txt` no requiere paquetes externos.

## Ejecución

Desde la carpeta raíz del proyecto, ejecuta:

```bash
python src/main.py
```

Se abrirá una ventana con el tablero del juego y las opciones de estado y reinicio.

## Componentes principales

### Modelo (`GameModel`)

La clase `GameModel` administra el estado del tablero y la lógica del juego:

| Método | Descripción |
| --- | --- |
| `reset_game()` | Reinicia el tablero, el turno y el estado de la partida. |
| `make_move(row, col)` | Intenta colocar una marca en la posición indicada. |
| `get_board()` | Devuelve una copia del estado actual del tablero. |

### Controlador (`GameController`)

La clase `GameController` conecta la vista con el modelo:

| Método | Descripción |
| --- | --- |
| `handle_board_click(row, col)` | Procesa el clic en una casilla y aplica la lógica del movimiento. |
| `handle_reset_click()` | Reinicia la partida desde el controlador. |
| `update_view()` | Actualiza la interfaz con los datos actuales del modelo. |

### Vista (`GameView`)

La clase `GameView` crea y actualiza la interfaz gráfica con Tkinter:

| Método | Descripción |
| --- | --- |
| `update_board_ui(board_matrix)` | Actualiza el texto y color de cada casilla del tablero. |
| `update_status(text, color)` | Cambia el texto y el color del estado actual. |
| `show_message(title, message)` | Muestra un mensaje emergente. |

## Autor

- **Nombre:** Gabriel Romulo Arnez Joven
- **Registro:** 220000417
- **Materia:** Estructura de Datos 2
- **Docente:** Ing. Juan Carlos Peinado Pereira
