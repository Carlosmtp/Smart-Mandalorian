import time
from .Mandalorian import Mandalorian

def GreedySearch(world):
    root = Mandalorian(world, None,  None, 0, 0, 0, None)
    tree = []
    tree.append(root)
    explored = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        tree.sort(key=lambda x: x.heuristic())
        current = tree.pop(0)
        expanded_nodes += 1
        if current.found_grogu():
            compute_time = time.time()-start_time
            solution = current.solution()
            return solution ,tree_nodes, expanded_nodes, current.depth, compute_time, current.cost
        else:
            for next in current.expand('greedy'):
                if next not in explored:
                    tree_nodes += 1
                    tree.append(next)
                    explored.add(next)
                    
def AStarSearch(world):
    root = Mandalorian(world, None,  None, 0, 0, 0, None)
    tree = []
    tree.append(root)
    explored = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        tree.sort(key=lambda x: x.heuristic() + x.cost)
        current = tree.pop(0)
        expanded_nodes += 1
        if current.found_grogu():
            compute_time = time.time()-start_time
            return current.solution(),tree_nodes, expanded_nodes, current.depth, compute_time, current.cost
        else:
            for next in current.expand('a_star'):
                if next not in explored:
                    tree_nodes += 1
                    tree.append(next)
                    explored.add(next)
                     
