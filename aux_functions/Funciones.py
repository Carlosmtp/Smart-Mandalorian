# Funciones auxiliares para los distintos algorithmos de busqueda
from models import World, Mandalorian

def is_grogu(mandalorian, world):
    return mandalorian.current_position == world.grogu_position

def is_enemy(position, world):
    return position in world.enemies