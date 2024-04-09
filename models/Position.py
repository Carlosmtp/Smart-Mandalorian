class Position:
    def __init__(self, row, column):
        """
        Crea una nueva instancia de la clase Position.

        Args:
            row (int): La fila de la posición.
            column (int): La columna de la posición.
        """
        self.row = row
        self.column = column

    def move_up(self):
        """
        Mueve la posición hacia arriba.

        Returns:
            Position: La nueva posición después de mover hacia arriba.
        """
        return Position(self.row - 1, self.column)

    def move_down(self):
        """
        Mueve la posición hacia abajo.

        Returns:
            Position: La nueva posición después de mover hacia abajo.
        """
        return Position(self.row + 1, self.column)

    def move_left(self):
        """
        Mueve la posición hacia la izquierda.

        Returns:
            Position: La nueva posición después de mover hacia la izquierda.
        """
        return Position(self.row, self.column - 1)

    def move_right(self):
        """
        Mueve la posición hacia la derecha.

        Returns:
            Position: La nueva posición después de mover hacia la derecha.
        """
        return Position(self.row, self.column + 1)

    def is_within(self, dimension):
        """
        Verifica si la posición está dentro de los límites de una dimensión dada.

        Args:
            dimension (tuple): Una tupla que representa las dimensiones (filas, columnas).

        Returns:
            bool: True si la posición está dentro de los límites, False de lo contrario.
        """
        filas, columnas = dimension
        return 0 <= self.row < filas and 0 <= self.column < columnas

    def __eq__(self, other):
        """
        Compara si dos posiciones son iguales.

        Args:
            other (Position): La otra posición a comparar.

        Returns:
            bool: True si las posiciones son iguales, False de lo contrario.
        """
        return isinstance(other, Position) and self.row == other.row and self.column == other.column

    def __hash__(self):
        """
        Calcula el hash de la posición.

        Returns:
            int: El hash de la posición.
        """
        return hash((self.row, self.column))

    def __repr__(self):
        """
        Devuelve una representación en cadena de la posición.

        Returns:
            str: La representación en cadena de la posición.
        """
        return f"({self.row}, {self.column})"