# Funciones auxiliares para los distintos algorithmos de busqueda

def is_grogu(mandalorian, world):
    return mandalorian.current_position == world.grogu_position

def reconstruct_solution(goal):
        path = []
        cost = 0
        while goal.parent is not None:
            path.append(goal.current_position)
            cost += goal.cost
            goal = goal.parent
        path.append(goal.current_position)
        path.reverse()
        return path, cost