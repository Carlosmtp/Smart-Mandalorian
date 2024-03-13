from models.Tile import Tile

class EmptyTile(Tile):
    def __init__(self, position, maze):
        super().__init__(position, 1, maze, False)

    def __str__(self):
        return ('{' + (f"position: {self.position},"
                      f"cost: {self.cost},"
                      f"maze: {self.maze},"
                      f"isGrogu: {self.isGrogu}") +
                '}')

    def __eq__(self, other):
        return self.position == other.position and self.cost == other.cost and self.isGrogu == other.isGrogu