from models.Position import Position

class Tile:
    def __init__(self, position: Position, cost: int, maze: [[int]], isGrogu: bool):
        self._position = position
        self._cost = cost
        self._maze = maze
        self._isGrogu = isGrogu

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def maze(self):
        return self._maze

    @maze.setter
    def maze(self, value):
        self._maze = value

    @property
    def isGrogu(self):
        return self._isGrogu

    @isGrogu.setter
    def isGrogu(self, value):
        self._isGrogu = value