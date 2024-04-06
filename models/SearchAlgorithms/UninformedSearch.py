# Este archivo contiene la implementación correspondiente a los
# algoritmos de búsqueda no informada: BFS, DFS, UCS
# -> BFS: Breadth First Search = Busqueda por Amplitud
# -> DFS: Depth First Search = Busqueda por Profundidad
# -> UCS: Uniform Cost Search = Busqueda de Costo Uniforme

import queue
from models import World, Mandalorian
from aux_functions import Funciones

def BreadthFirstSearch(world):
    mando = Mandalorian(world)

    frontier = queue.Queue()
    frontier.put(mando.current_position)
    came_from = {}
    came_from[mando.current_position] = None

    while not frontier.empty():
        current = frontier.get()

        if Funciones.is_grogu(mando, world):
            break

        for next in mando.possible_moves():
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from

