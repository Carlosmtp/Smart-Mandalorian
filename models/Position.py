class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def move_up(self):
        return Position(self.row - 1, self.column)

    def move_down(self):
        return Position(self.row + 1, self.column)

    def move_left(self):
        return Position(self.row, self.column - 1)

    def move_right(self):
        return Position(self.row, self.column + 1)

    def is_within(self, dimension):
        filas, columnas = dimension
        return 0 <= self.fila < filas and 0 <= self.columna < columnas

    def __eq__(self, other):
        return isinstance(other, Position) and self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash((self.row, self.column))

    def __repr__(self):
        return f"({self.row}, {self.column})"
