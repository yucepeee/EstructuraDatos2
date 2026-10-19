
from models.ml_agent import MLAgent
"""
if __name__ == "__main__":
    # Instanciar el simulador de la Semana 3 - Día 1
    simulator = MLAgentSimulator()
    
    # Generar 1,000 partidas automatizadas (Minimax vs Aleatorio)
    simulator.simulate_games(num_games=10)
    
    # Guardar los resultados en el dataset sintético
    simulator.save_dataset_to_csv("tic_tac_toe_dataset.csv")"""

# Bloque de prueba para ejecutar el Día 3
if __name__ == "__main__":
    ml_agent = MLAgent()
    ml_agent.train_model()
    ml_agent.export_tree_rules()
    ml_agent.plot_and_save_tree()