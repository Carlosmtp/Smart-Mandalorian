import queue
import time
from Mandalorian import Mandalorian
from World import World
import Funciones

# Este archivo contiene la implementación correspondiente a los
# algoritmos de búsqueda no informada: BFS, DFS, UCS
# -> BFS: Breadth First Search = Busqueda por Amplitud
# -> DFS: Depth First Search = Busqueda por Profundidad
# -> UCS: Uniform Cost Search = Busqueda de Costo Uniforme


def BreadthFirstSearch(world):
    root = Mandalorian(world, None,  None, 0, 0)
    tree = queue.Queue()
    tree.put(root)
    explored = set()
    expanded_nodes = 0

    start_time = time.time()

    while not tree.empty():
        current = tree.get()
        expanded_nodes += 1
        if Funciones.is_grogu(current, world):
            path = []
            while current.parent is not None:
                path.append(current.current_position)
                current = current.parent
            path.append(current.current_position)
            path.reverse()
            end_time = time.time()
            computation_time = end_time - start_time
            return path, expanded_nodes, len(path), computation_time, len(path)
        for next in current.possible_moves():
            if next not in explored:
                tree.put(next)
                explored.add(next)
                
def UniformCostSearch(world):
    return

def DepthFirstSearch(world):
    return