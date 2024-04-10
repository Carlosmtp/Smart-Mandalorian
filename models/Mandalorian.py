class Mandalorian:
    def __init__(self, world, parent, operator, depth, cost, fuel):
        """
        Inicializa una instancia de la clase Mandalorian, que representa un nodo
        en los algoritmos de búsqueda.

        Args:
            world (World): El mundo en el que se encuentra el Mandalorian.
            parent (Mandalorian): El Mandalorian padre.
            operator (int): El operador utilizado para llegar a esta instancia.
            depth (int): La profundidad de esta instancia en el árbol de búsqueda.
            cost (float): El costo de esta instancia.
            fuel (int): La cantidad de combustible del Mandalorian.
        """
        self.world = world
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
        self.current_position = world.start_position
        if fuel > 0:
            self.fuel = fuel
            self.in_ship = True
        else:
            self.fuel = 0
            self.in_ship = False

    def getParent(self):
        """
        Obtiene el Mandalorian padre.

        Returns:
            Mandalorian: El Mandalorian padre.
        """
        return self.parent
    
    def getOperator(self):
        """
        Obtiene el operador utilizado para llegar a esta instancia.

        Returns:
            int: El operador utilizado.
        """
        return self.operator
    
    def is_in_ship(self):
        """
        Verifica si el Mandalorian está dentro de la nave.

        Returns:
            bool: True si el Mandalorian está dentro de la nave, False en caso contrario.
        """
        return self.in_ship
    
    def getDepth(self):
        """
        Obtiene la profundidad de esta instancia en el árbol de búsqueda.

        Returns:
            int: La profundidad de esta instancia.
        """
        return self.depth
    
    def getCost(self):
        """
        Obtiene el costo acumulado de la instancia.

        Returns:
            float: El costo acumulado.
        """
        return self.cost
    
    def getWorld(self):
        """
        Obtiene el mundo en el que se encuentra el Mandalorian.

        Returns:
            World: El mundo en el que se encuentra el Mandalorian.
        """
        return self.state
    
    def move(self, new_position):
        """
        Mueve al Mandalorian a una nueva posición.

        Args:
            new_position (Position): La nueva posición a la que se moverá el Mandalorian.
        """
        if self.world.in_ship(new_position):
            self.board_ship()
        self.current_position = new_position

    def move_up(self):
        """
        Mueve al Mandalorian hacia arriba.
        """
        new_position = self.current_position.move_up()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)

    def move_down(self):
        """
        Mueve al Mandalorian hacia abajo.
        """
        new_position = self.current_position.move_down()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)

    def move_left(self):
        """
        Mueve al Mandalorian hacia la izquierda.
        """
        new_position = self.current_position.move_left()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)

    def move_right(self):
        """
        Mueve al Mandalorian hacia la derecha.
        """
        new_position = self.current_position.move_right()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)

    def possible_moves(self):
        """
        Obtiene los posibles movimientos que puede realizar el Mandalorian.

        Returns:
            list[Mandalorian]: Lista de instancias de Mandalorian que representan los posibles movimientos.
        """
        moves = []
        position = self.current_position
        world = self.world
        new_fuel = 0
        if self.world.in_ship(position):
            self.in_ship = True
            self.fuel = 10
            self.world.remove_ship()
        if self.in_ship:
            new_fuel = self.fuel - 1
        
        up_cost = self.cost+self.calculate_cost(position.move_up())
        down_cost = self.cost+self.calculate_cost(position.move_down())
        left_cost = self.cost+self.calculate_cost(position.move_left())
        right_cost = self.cost+self.calculate_cost(position.move_right())
        if world.is_within_bounds(position.move_right()) and not world.is_wall(position.move_right()):
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, right_cost, new_fuel)
            new_mandalorian.current_position = position.move_right()
            new_mandalorian.operator = 4
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_left()) and not world.is_wall(position.move_left()):
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, left_cost, new_fuel)
            new_mandalorian.current_position = position.move_left()
            new_mandalorian.operator = 3
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_down()) and not world.is_wall(position.move_down()):
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, down_cost, new_fuel)
            new_mandalorian.current_position = position.move_down()
            new_mandalorian.operator = 2
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_up()) and not world.is_wall(position.move_up()):
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, up_cost, new_fuel)
            new_mandalorian.current_position = position.move_up()
            new_mandalorian.operator = 1
            moves.append(new_mandalorian)
        
            
        return moves
    
    def calculate_cost(self, position):
        """
        Calcula el costo para moverse a una posición específica.

        Args:
            position (Position): La posición a la que se desea mover.

        Returns:
            float: El costo para moverse a la posición especificada.
        """
        if self.in_ship and self.fuel > 0:
            return 0.5
        elif self.world.is_enemy(position):
            return 5
        return 1
    
    def found_grogu(self):
        """
        Verifica si el Mandalorian ha encontrado a Grogu.

        Returns:
            bool: True si el Mandalorian ha encontrado a Grogu, False en caso contrario.
        """
        return self.current_position == self.world.grogu_position
    
    def solution(self):
        """
        Reconstruye la solución a partir del nodo meta.

        Returns:
            list[Position]: La lista de posiciones en el camino.
        """
        path = []
        current = self
        while current.parent is not None:
            path.append(current.current_position)
            current = current.parent
        path.append(current.current_position)
        path.reverse()
        return path

    def __eq__(self, other):
        """
        Compara si dos instancias de Mandalorian son iguales.

        Args:
            other (Mandalorian): La otra instancia de Mandalorian a comparar.

        Returns:
            bool: True si las instancias son iguales, False en caso contrario.
        """
        if isinstance(other, Mandalorian):
            return (self.current_position == other.current_position) and (self.in_ship == other.in_ship)
        return False
    
    def __hash__(self):
        """
        Obtiene el hash de la instancia de Mandalorian.

        Returns:
            int: El hash de la instancia.
        """
        return hash(self.current_position)