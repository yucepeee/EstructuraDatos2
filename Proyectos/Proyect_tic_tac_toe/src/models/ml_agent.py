import os
import csv
import random
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

from models.game_model import GameModel
from models.minimax_agent import MinimaxAgent


class MLAgent:
    """Clase que encapsula la lógica de un agente de Machine Learning para jugar Tres en Raya."""
    def __init__(self, csv_filename="tic_tac_toe_dataset.csv"):
        self.csv_filename = csv_filename
        self.model = DecisionTreeClassifier(criterion="entropy", random_state=42)
        self.is_trained = False
        
        # Mapeo fijo y consistente para las casillas del tablero
        self.cell_mapping = {"_": 0, "": 0, "X": 1, "O": -1}

    
    # Simulación y Generación de Dataset
    def simulate_and_save_dataset(self, num_games=1000):
        """Simula partidas entre Minimax y un jugador aleatorio y guarda el CSV."""
        print(f"Iniciando simulación de {num_games} partidas...")
        dataset = []

        for game_idx in range(num_games):
            game = GameModel()
            ai_agent = MinimaxAgent(ai_player="O", human_player="X")

            while not game.game_over:
                current_board = game.get_board()
                available_moves = game.get_available_moves()
                if not available_moves:
                    break

                if game.current_player == "O":
                    best_move = ai_agent.get_best_move(game)
                    if best_move:
                        flattened = [cell if cell != "" else "_" for row in current_board for cell in row]
                        dataset.append({
                            **{f"cell_{i}": flattened[i] for i in range(9)},
                            "optimal_row": best_move[0],
                            "optimal_col": best_move[1]
                        })
                        game.make_move(best_move[0], best_move[1])
                else:
                    random_move = random.choice(available_moves)
                    game.make_move(random_move[0], random_move[1])

            if (game_idx + 1) % 200 == 0:
                print(f"Progreso: {game_idx + 1}/{num_games} partidas simuladas...")

        keys = [f"cell_{i}" for i in range(9)] + ["optimal_row", "optimal_col"]
        with open(self.csv_filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(dataset)

        print(f"¡Dataset guardado en '{self.csv_filename}' con {len(dataset)} jugadas óptimas!")

    
    # Limpieza y Estructuración de Datos
    def load_and_preprocess_data(self):
        """Carga el CSV, limpia duplicados y codifica las 9 casillas y la etiqueta objetivo."""
        if not os.path.exists(self.csv_filename):
            print(f"No se encontró '{self.csv_filename}'. Generando dataset automáticamente...")
            self.simulate_and_save_dataset(num_games=1000)

        df = pd.read_csv(self.csv_filename)
        df = df.dropna().drop_duplicates()

        feature_cols = [f"cell_{i}" for i in range(9)]
        
        # Transformar '_', 'X', 'O' a números (0, 1, -1)
        X = df[feature_cols].replace(self.cell_mapping)
        
        # Convertir (optimal_row, optimal_col) en una sola clase del 0 al 8
        y = df["optimal_row"] * 3 + df["optimal_col"]

        return X, y

    
    # Entrenamiento y Visualización del Árbol
    def train_model(self):
        """Entrena el DecisionTreeClassifier y evalúa su precisión."""
        X, y = self.load_and_preprocess_data()

        # Dividir en conjunto de entrenamiento (80%) y prueba (20%) para medir precisión
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Entrenamos con el 100% de los datos tras validar para que aprenda todos los estados vistos
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        # Re-entrenar con todos los datos para maximizar su conocimiento en el juego real
        self.model.fit(X, y)
        self.is_trained = True

        print(f"¡Modelo DecisionTreeClassifier entrenado con éxito!")
        print(f"Precisión en validación: {acc * 100:.2f}%")
        print(f"Profundidad del árbol generado: {self.model.get_depth()}")
        print(f"Número de hojas (reglas finales): {self.model.get_n_leaves()}")
        return acc

    def export_tree_rules(self, txt_filename="reglas_arbol_decision.txt"):
        """Exporta las reglas lógicas del árbol en formato texto (Recomendación docente)."""
        if not self.is_trained:
            self.train_model()

        feature_names = [f"cell_{i}" for i in range(9)]
        rules_text = export_text(self.model, feature_names=feature_names)

        with open(txt_filename, "w", encoding="utf-8") as f:
            f.write("=== REGLAS LÓGICAS APRENDIDAS POR EL ÁRBOL DE DECISIÓN ===\n")
            f.write("(Nota: 0 = Vacío, 1 = Humano 'X', -1 = IA 'O')\n\n")
            f.write(rules_text)

        print(f"Reglas del árbol exportadas en '{txt_filename}'.")
        return rules_text

    def plot_and_save_tree(self, img_filename="arbol_decision.png", max_depth=3):
        """Genera y guarda una imagen gráfica de los primeros niveles del árbol."""
        if not self.is_trained:
            self.train_model()

        plt.figure(figsize=(20, 10))
        plot_tree(
            self.model,
            max_depth=max_depth,  # Limitamos a 3 niveles en la imagen para que sea legible
            feature_names=[f"cell_{i}" for i in range(9)],
            class_names=[f"Casilla {i}" for i in range(9)],
            filled=True,
            rounded=True,
            fontsize=9
        )
        plt.title("Árbol de Decisión - Tres en Raya (Primeros 3 niveles)")
        plt.savefig(img_filename, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Gráfico del árbol exportado exitosamente como '{img_filename}'.")

    # Inferencia en vivo
    def get_best_move(self, game_model):
        """Predice instantáneamente la mejor jugada (fila, col) usando el árbol entrenado."""
        if not self.is_trained:
            self.train_model()

        board = game_model.get_board()
        available_moves = game_model.get_available_moves()
        if not available_moves:
            return None

        # Convertir el estado actual del tablero al formato numérico de entrada
        flattened_numeric = [self.cell_mapping.get(cell, 0) for row in board for cell in row]
        input_df = pd.DataFrame([flattened_numeric], columns=[f"cell_{i}" for i in range(9)])

        # Predecir la casilla (0 a 8)
        predicted_cell = int(self.model.predict(input_df)[0])
        row, col = divmod(predicted_cell, 3)

        # Verificar que la casilla predicha esté vacía; si no, usar probabilidades o respaldo
        if (row, col) in available_moves:
            return (row, col)
        else:
            # Obtener probabilidades de cada clase y elegir la casilla disponible con mayor probabilidad
            probs = self.model.predict_proba(input_df)[0]
            classes = self.model.classes_
            sorted_indices = probs.argsort()[::-1]
            for idx in sorted_indices:
                r, c = divmod(int(classes[idx]), 3)
                if (r, c) in available_moves:
                    return (r, c)
            return random.choice(available_moves)

