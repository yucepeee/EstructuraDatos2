# filepath: /tkinter-mvc-app/tkinter-mvc-app/src/main.py

import tkinter as tk
from views.gui_view import GameView
from controllers.game_controller import GameController
from models.game_model import GameModel 

def main():
    root = tk.Tk()
    root.title("App (ABB)")

    root.geometry("550x380")  # Tamaño de la ventana
    root.update_idletasks()  # Actualiza la ventana antes de centrarla

    # Centrar la ventana en la pantalla
    ancho = root.winfo_width()      
    alto = root.winfo_height()

    pantalla_ancho = root.winfo_screenwidth()       
    pantalla_alto = root.winfo_screenheight()

    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    root.geometry(f"+{x}+{y}")
    
    model = GameModel()
    view = GameView(root)
    controller = GameController(model, view)
    
    root.mainloop()

if __name__ == "__main__":
    main()