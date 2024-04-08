from Position import Position
class World:
    def __init__(self, file):
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
        return self.matrix[position.row][position.column]

    def is_empty(self, position):
        return self.get_tile(position) == 0

    def is_within_bounds(self, position):
        return position.is_within(self.dimension)
    
    def is_wall(self, position):
        return self.get_tile(position) == 1

    def remove_ship(self):
        self.ship_position = None

    def print_world(self):
        for row in self.matrix:
            print(" ".join(str(num) for num in row))