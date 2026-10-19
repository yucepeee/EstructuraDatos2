# Tres en Raya: Minimax y Machine Learning

Proyecto de Tres en Raya en Python con interfaz gráfica Tkinter y arquitectura Modelo-Vista-Controlador (MVC). Se puede jugar contra otra persona, contra Minimax o contra un árbol de decisión entrenado con partidas simuladas. La interfaz también permite comparar el rendimiento de Minimax y del modelo de Machine Learning.

## Funcionalidades

- Tablero de 3 x 3, alternancia de turnos y detección de victoria o empate.
- Modos de juego: Humano vs. Humano, Humano vs. IA Minimax y Humano vs. IA ML.
- Reinicio de la partida y mensajes de estado en la interfaz.
- Métricas de la jugada de IA: latencia y nodos evaluados (en ML se informa una ruta de inferencia como un nodo).
- Comparativa Minimax vs. ML sobre 25 partidas simuladas, con latencia media y porcentaje de coincidencia de jugadas.
- Entrenamiento de un `DecisionTreeClassifier` y exportación de sus reglas y de una imagen del árbol.

## Requisitos e instalación

Se requiere Python 3 y Tkinter. El agente de Machine Learning también usa `pandas`, `scikit-learn` y `matplotlib`. Instala las dependencias del proyecto desde la carpeta raíz con:

```bash
python -m pip install -r requirements.txt
```

Tkinter normalmente viene incluido con Python. En algunas distribuciones de Linux puede ser necesario instalarlo por separado mediante el gestor de paquetes del sistema.

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python src/main.py
```

Al iniciar la aplicación, el controlador entrena el árbol de decisión. Usa `tic_tac_toe_dataset.csv` si está disponible en la carpeta de trabajo; si no existe, genera automáticamente un conjunto de datos a partir de 1,000 partidas simuladas entre Minimax y un jugador aleatorio. La ruta del CSV y de los archivos exportados es relativa a la carpeta desde la que se ejecuta el programa.

Para entrenar el modelo y exportar sus reglas y su gráfico sin abrir la interfaz, ejecuta desde la carpeta raíz:

```bash
python src/test_ml.py
```

Este comando genera `reglas_arbol_decision.txt` y `arbol_decision.png` en la carpeta de trabajo.

## Estructura del proyecto

```text
.
├── README.md
├── requirements.txt
├── tic_tac_toe_dataset.csv
└── src/
    ├── main.py
    ├── test.py
    ├── test_ml.py
    ├── controllers/
    │   └── game_controller.py
    ├── models/
    │   ├── game_model.py
    │   ├── minimax_agent.py
    │   └── ml_agent.py
    └── views/
        └── gui_view.py
```

## Componentes

### Modelo: `GameModel`

Gestiona el tablero, el turno actual, los movimientos disponibles y el resultado de la partida. Incluye operaciones para aplicar y deshacer movimientos, verificar ganadores y reiniciar el juego.

### Agente Minimax: `MinimaxAgent`

Explora recursivamente las jugadas posibles y deshace cada movimiento al retroceder (*backtracking*). Evalúa resultados de victoria, derrota y empate, y cuenta los nodos evaluados para mostrarlos en la interfaz.

### Agente de Machine Learning: `MLAgent`

Carga y preprocesa el CSV de partidas, convierte cada tablero en nueve características y combina la fila y columna de la jugada objetivo en una de nueve clases. Divide los datos para medir la precisión de validación y luego vuelve a entrenar el árbol con todos los datos disponibles. En una jugada, predice una casilla y, si está ocupada, intenta escoger la casilla disponible con mayor probabilidad.

El conjunto de datos se construye registrando las jugadas de Minimax cuando juega `O` contra movimientos aleatorios de `X`. Por ello, el árbol aprende de esos ejemplos; no garantiza encontrar siempre la misma jugada que Minimax ni ser óptimo en todos los tableros.

### Controlador: `GameController`

Conecta el modelo y la vista, procesa los clics, ejecuta la IA elegida, mide su latencia y actualiza las métricas. La comparativa ejecuta 25 partidas simuladas; en cada turno de `O` mide ambos agentes sobre el mismo tablero y registra si sus jugadas coinciden.

### Vista: `GameView`

Presenta el tablero, los tres modos de juego, los mensajes de estado, las métricas, el botón para comparar agentes y el botón para reiniciar.

## Pruebas

Desde la carpeta raíz, ejecuta las pruebas unitarias del modelo con:

```bash
python -m unittest discover -s src -p "test.py"
```

`src/test_ml.py` es un script de entrenamiento y exportación del modelo, no una suite de pruebas unitarias.

## Criterios de evaluación y rúbrica

### Complejidad y latencia

- **Minimax:** explora recursivamente el árbol de jugadas con complejidad exponencial en la profundidad de búsqueda (habitualmente expresada como $O(b^d)$, con factor de ramificación $b$ y profundidad $d$). El número de nodos visitados depende del tablero. La aplicación mide la latencia en la máquina donde se ejecuta; no se fija un tiempo universal.
- **Árbol de decisión:** el entrenamiento se realiza al iniciar la aplicación. Durante una jugada, recorre una ruta del árbol, por lo que el costo de inferencia depende de su altura $h$ (aproximadamente $O(h)$). La medición de la aplicación incluye la preparación de la entrada y puede variar según el equipo y el estado del programa.

### Optimalidad y precisión

- **Minimax:** con una evaluación y búsqueda correctas hasta el final de la partida, elige una jugada óptima para el estado actual; puede haber varias jugadas igualmente óptimas.
- **Árbol de decisión:** aproxima las jugadas de Minimax a partir de los ejemplos generados. El proyecto informa tanto la precisión calculada en una partición de validación como la coincidencia de jugadas observada en la comparativa. Son métricas distintas y sus resultados dependen del conjunto de datos; el modelo puede recomendar una jugada subóptima en estados no representados adecuadamente.

### Conclusión pedagógica

El Tres en Raya permite explorar con Minimax todo el árbol de jugadas en una escala manejable y comparar la búsqueda con una inferencia aprendida a partir de datos. La comparación ilustra el intercambio entre explorar estados para decidir y entrenar previamente un modelo que produce una respuesta recorriendo un árbol de decisión.

## Autoría

- **Nombre:** Gabriel Romulo Arnez Joven
- **Registro:** 220000417
- **Materia:** Estructura de Datos 2
- **Docente:** Ing. Juan Carlos Peinado Pereira
