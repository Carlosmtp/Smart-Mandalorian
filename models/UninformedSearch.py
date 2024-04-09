import time
from Mandalorian import Mandalorian
from Funciones import is_grogu, reconstruct_solution

def BreadthFirstSearch(world):
    """
    Realiza una búsqueda por amplitud en un mundo dado.

    Parámetros:
    - world: El mundo en el que se realizará la búsqueda.

    Retorna:
    - path: El camino encontrado desde el estado inicial hasta el estado objetivo.
    - tree_nodes: El número de nodos en el árbol de búsqueda.
    - expanded_nodes: El número de nodos expandidos durante la búsqueda.
    - depth: La profundidad del camino encontrado.
    - computation_time: El tiempo de computación utilizado para realizar la búsqueda.
    - cost: El costo total del camino encontrado.
    """
    root = Mandalorian(world, None,  None, 0, 0, 0)
    tree = []
    tree.append(root)
    explored = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        current = tree.pop(0)
        expanded_nodes += 1
        if is_grogu(current, world):
            end_time = time.time()
            path, cost = reconstruct_solution(current)
            computation_time = end_time - start_time
            return path, tree_nodes, expanded_nodes, len(path), computation_time, cost
        else:
            for next in current.possible_moves():
                if next not in explored:
                    tree_nodes += 1
                    tree.append(next)
                    explored.add(next)

def UniformCostSearch(world):
    """
    Realiza una búsqueda por costo uniforme en un mundo dado.

    Parámetros:
    - world: El mundo en el que se realizará la búsqueda.

    Retorna:
    - path: El camino encontrado desde el estado inicial hasta el estado objetivo.
    - tree_nodes: El número de nodos en el árbol de búsqueda.
    - expanded_nodes: El número de nodos expandidos durante la búsqueda.
    - depth: La profundidad del camino encontrado.
    - computation_time: El tiempo de computación utilizado para realizar la búsqueda.
    - cost: El costo total del camino encontrado.
    """
    root = Mandalorian(world, None,  None, 0, 0, 0)
    tree = []
    tree.append(root)
    explored = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        tree.sort(key=lambda x: x.cost)
        current = tree.pop(0)
        expanded_nodes += 1
        if is_grogu(current, world):
            end_time = time.time()
            path, cost = reconstruct_solution(current)
            computation_time = end_time - start_time
            return path, tree_nodes, expanded_nodes, len(path), computation_time, cost
        else:
            for next in current.possible_moves():
                if next not in explored:
                    tree_nodes += 1
                    tree.append(next)
                    explored.add(next)

def DepthFirstSearch(world):
    """
    Realiza una búsqueda en profundidad evitando ciclos en un mundo dado.

    Parámetros:
    - world: El mundo en el que se realizará la búsqueda.

    Retorna:
    - path: El camino encontrado desde el estado inicial hasta el estado objetivo.
    - tree_nodes: El número de nodos en el árbol de búsqueda.
    - expanded_nodes: El número de nodos expandidos durante la búsqueda.
    - depth: La profundidad del camino encontrado.
    - computation_time: El tiempo de computación utilizado para realizar la búsqueda.
    - cost: El costo total del camino encontrado.
    """
    root = Mandalorian(world, None,  None, 0, 0, 0)
    tree = []
    tree.append(root)
    explored = set()
    explored_in_branch = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        current = tree.pop()
        expanded_nodes += 1
        explored_in_branch = set()
        if is_grogu(current, world):
            end_time = time.time()
            path, cost = reconstruct_solution(current)
            computation_time = end_time - start_time
            return path, tree_nodes, expanded_nodes, len(path), computation_time, cost
        else:
            for next in current.possible_moves():
                if next not in explored and next not in explored_in_branch:
                    tree_nodes += 1
                    tree.append(next)
                    explored_in_branch.add(next)
            explored.add(current)