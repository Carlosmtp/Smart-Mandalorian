import time
from Mandalorian import Mandalorian
from Funciones import is_grogu, reconstruct_solution

# Este archivo contiene la implementación correspondiente a los
# algoritmos de búsqueda no informada: BFS, DFS, UCS
# -> BFS: Breadth First Search = Busqueda por Amplitud
# -> DFS: Depth First Search = Busqueda por Profundidad
# -> UCS: Uniform Cost Search = Busqueda de Costo Uniforme


def BreadthFirstSearch(world):
    root = Mandalorian(world, None,  None, 0, 0, 0)
    tree = []
    tree.append(root)
    explored = set()
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        current = tree.pop(0)
        if is_grogu(current, world):
            end_time = time.time()
            path, cost = reconstruct_solution(current)
            computation_time = end_time - start_time
            return path, expanded_nodes, len(path)-1, computation_time, cost
        else:
            for next in current.possible_moves():
                if next not in explored:
                    expanded_nodes += 1
                    tree.append(next)
                    explored.add(next)

def UniformCostSearch(world):
    root = Mandalorian(world, None,  None, 0, 0, 0)
    tree = []
    tree.append(root)
    explored = set()
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        tree.sort(key=lambda x: x.cost)
        current = tree.pop(0)
        if is_grogu(current, world):
            end_time = time.time()
            path, cost = reconstruct_solution(current)
            computation_time = end_time - start_time
            return path, expanded_nodes, len(path)-1, computation_time, cost
        else:
            for next in current.possible_moves():
                if next not in explored:
                    expanded_nodes += 1
                    tree.append(next)
                    explored.add(next)

def DepthFirstSearch(world):
    root = Mandalorian(world, None,  None, 0, 0, 0)
    tree = []
    tree.append(root)
    explored = set()
    explored_in_branch = set()
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        current = tree.pop()
        explored_in_branch = set()
        if is_grogu(current, world):
            end_time = time.time()
            path, cost = reconstruct_solution(current)
            computation_time = end_time - start_time
            return path, expanded_nodes, len(path)-1, computation_time, cost
        else:
            for next in current.possible_moves():
                if next not in explored and next not in explored_in_branch:
                    expanded_nodes += 1
                    tree.append(next)
                    explored_in_branch.add(next)
            explored.add(current)