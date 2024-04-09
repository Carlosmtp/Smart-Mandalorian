def is_grogu(mandalorian, world):
    """
    Comprueba si el mandaloriano se encuentra en la posición actual de Grogu en el mundo.

    Parámetros:
    - mandalorian: El objeto que representa al mandaloriano.
    - world: El objeto que representa al mundo.

    Retorna:
    - True si el mandaloriano se encuentra en la posición actual de Grogu.
    - False en caso contrario.
    """
    return mandalorian.current_position == world.grogu_position

def reconstruct_solution(goal):
    """
    Reconstruye la solución a partir del nodo meta.

    Parameters:
    goal (Nodo): El nodo meta desde el cual se reconstruirá la solución.

    Returns:
    tuple: Una tupla que contiene la lista de posiciones en el camino y el costo total de la solución.
    """
    path = []
    cost = 0
    while goal.parent is not None:
        path.append(goal.current_position)
        cost += goal.cost
        goal = goal.parent
    path.append(goal.current_position)
    path.reverse()
    return path, cost
