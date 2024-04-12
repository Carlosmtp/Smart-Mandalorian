from .Position import Position
class World:
    def __init__(self, file):
        """
        Inicializa una instancia de la clase World.

        Parámetros:
        - file: Ruta del archivo que contiene la matriz del mundo.

        Atributos:
        - matrix: Matriz que representa el mundo.
        - dimension: Tupla que indica las dimensiones de la matriz (filas, columnas).
        - start_position: Posición de inicio en el mundo.
        - ship_position: Posición de la nave en el mundo.
        - grogu_position: Posición de Grogu en el mundo.
        - enemies: Lista de posiciones de los enemigos en el mundo.
        """
        self.matrix = None
        self.dimension = (0, 0)
        self.start_position = None
        self.ship_position = None
        self.grogu_position = None
        self.enemies = []

        with open(file, 'r') as f:
            self.matrix = [[int(num) for num in line.split()] for line in f.readlines()]
            self.dimension = (len(self.matrix), len(self.matrix[0]))
            for i in range(self.dimension[0]):
                for j in range(self.dimension[1]):
                    if self.matrix[i][j] == 2:
                        self.start_position = Position(i, j)
                    elif self.matrix[i][j] == 3:
                        self.ship_position = Position(i, j)
                    elif self.matrix[i][j] == 5:
                        self.grogu_position = Position(i, j)
                    elif self.matrix[i][j] == 4:
                        self.enemies.append(Position(i, j))

    def get_tile(self, position):
        """
        Devuelve el valor de la casilla en la posición dada.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - El valor de la casilla en la posición dada.
        """
        return self.matrix[position.row][position.column]

    def is_empty(self, position):
        """
        Verifica si la casilla en la posición dada está vacía.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la casilla está vacía, False de lo contrario.
        """
        return self.get_tile(position) == 0
    
    def is_enemy(self, position):
        """
        Verifica si la posición dada contiene un enemigo.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la posición contiene un enemigo, False de lo contrario.
        """
        return position in self.enemies
    
    def in_ship(self, position):
        """
        Verifica si la posición dada está en la ubicación de la nave.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la posición está en la ubicación de la nave, False de lo contrario.
        """
        return position == self.ship_position
    
    def is_wall(self, position):
        """
        Verifica si la casilla en la posición dada es una pared.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la casilla es una pared, False de lo contrario.
        """
        return self.get_tile(position) == 1

    def remove_ship(self):
        """
        Elimina la posición de la nave en el mundo.
        """
        self.ship_position = None
        
    def is_within_bounds(self, position):
        """
        Verifica si la posición dada está dentro de los límites del mundo.

        Parámetros:
        - position: Posición en el mundo.

        Retorna:
        - True si la posición está dentro de los límites del mundo, False de lo contrario.
        """
        return position.is_within(self.dimension)
    