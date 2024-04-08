# Funciones auxiliares para los distintos algorithmos de busqueda
from Mandalorian import Mandalorian
from World import World

def is_grogu(mandalorian, world):
    return mandalorian.current_position == world.grogu_position

def is_enemy(position, world):
    return position in world.enemies

def is_ship(position, world):
    return position == world.ship_position