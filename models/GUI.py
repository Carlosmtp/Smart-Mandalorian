import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Mandalorian import Mandalorian
from World import World
from Position import Position
from SearchGUI import SearchGUI
import os

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Smart Mandalorian")
        self.master.geometry("1280x720")
        self.master.resizable(False, False)

        # Cargar imagen de fondo
        self.background_image = Image.open("../images/background.png")
        self.background_image = self.background_image.resize((1280, 720), Image.BICUBIC)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Inicializar variables
        self.world = None
        self.mandalorian = None
        self.search_algorithm = None

        # Crear botones
        self.btn_load_world = tk.Button(master, text="Cargar Archivo de Mundo", command=self.load_world)
        self.btn_load_world.place(x=200, y=250)

        self.lbl_file_name = tk.Label(master, text="", font=("Arial", 12))
        self.lbl_file_name.place(x=410, y=255)

        self.algorithm_var = tk.StringVar(master)
        self.algorithm_var.set("Seleccionar Tipo de Búsqueda")

        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, "No Informada", "Informada", command=self.show_algorithm_options)
        self.algorithm_menu.place(x=200, y=325)
        self.algorithm_menu.config(state=tk.DISABLED)

        self.algorithm_options_var = tk.StringVar(master)
        self.algorithm_options_var.set("Seleccionar Algoritmo")
        self.algorithm_options_menu = tk.OptionMenu(master, self.algorithm_options_var, "", "")
        self.algorithm_options_menu.place(x=200, y=400)
        self.algorithm_options_menu.config(state=tk.DISABLED)

        self.btn_run_algorithm = tk.Button(master, text="Ejecutar Búsqueda", command=self.run_algorithm)
        self.btn_run_algorithm.place(x=200, y=475)
        self.btn_run_algorithm.config(state=tk.DISABLED)

    def load_world(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Obtener la ruta relativa
            relative_path = os.path.relpath(file_path)
            # Mostrar la ruta relativa
            self.lbl_file_name.config(text=relative_path)
            # Crear instancia del mundo
            self.world = World(file_path)
            self.world.print_world()
            self.mandalorian = Mandalorian(self.world)
            self.algorithm_menu.config(state=tk.NORMAL)

    def show_algorithm_options(self, selection):
        if selection == "No Informada":
            algorithms = ["Amplitud", "Costo Uniforme", "Profundidad Evitando Ciclos"]
        elif selection == "Informada":
            algorithms = ["Avara", "A*"]
        else:
            algorithms = []

        # Actualizar las opciones del menú desplegable de algoritmos
        self.algorithm_options_var.set(algorithms[0])  # Establecer el primer algoritmo como predeterminado
        self.algorithm_options_menu["menu"].delete(0, "end")  # Limpiar las opciones actuales
        for algorithm in algorithms:
            self.algorithm_options_menu["menu"].add_command(label=algorithm, command=tk._setit(self.algorithm_options_var, algorithm))

        # Habilitar el menú desplegable de algoritmos y las opciones correspondientes
        self.algorithm_options_menu.config(state=tk.NORMAL)

        # Habilitar el botón de ejecución de algoritmo
        self.btn_run_algorithm.config(state=tk.NORMAL)

    def run_algorithm(self):
        ##selected_algorithm = self.algorithm_options_var.get()
        mandalorian_moves = [
            Position(2, 3),
            Position(2, 4),
            Position(3, 4),
            Position(3, 5)
        ]
        search = SearchGUI(self.lbl_file_name.cget("text"), mandalorian_moves)
        search.draw_tablero()

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

mundo = World("../test/test1.txt")
