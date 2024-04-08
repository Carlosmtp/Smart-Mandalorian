from World import World
class Mandalorian:
    def __init__(self, world, parent, operator, depth, cost):
        self.world = world
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
        self.current_position = world.start_position
        self.in_ship = False
        self.fuel = 10

    def getParent(self):
        return self.parent
    
    def getOperator(self):
        return self.operator
    
    def getDepth(self):
        return self.depth
    
    def getCost(self):
        return self.cost
    
    def getWorld(self):
        return self.state
    
    def move(self, new_position):
        if self.in_ship:
            move_cost = 0.5
            if self.world.is_empty(new_position):
                self.current_position = new_position
                self.fuel -= 1
                if self.fuel <= 0:
                    self.in_ship = False
#            else:
#                print("Imposible mover. Casilla ocupada.")

        else:
            move_cost = 1
            if self.world.is_empty(new_position):
                self.current_position = new_position
#            else:
#                print("Imposible mover. Casilla ocupada.")

    def move_up(self):
        new_position = self.current_position.move_up()
        if self.world.is_within_bounds(new_position):
            return self.move(new_position)
#        else:
#            print("Imposible mover hacia arriba. Fuera de los límites.")


    def move_down(self):
        new_position = self.current_position.move_down()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)
#        else:
#            print("Imposible mover hacia abajo. Fuera de los límites.")

    def move_left(self):
        new_position = self.current_position.move_left()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)
#        else:
#            print("Imposible mover hacia la izquierda. Fuera de los límites.")

    def move_right(self):
        new_position = self.current_position.move_right()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)
#        else:
#            print("Imposible mover hacia la derecha. Fuera de los límites.")

    def possible_moves(self):
        moves = []
        position = self.current_position
        world = self.world
        if world.is_within_bounds(position.move_up()) and world.is_wall(position.move_up()) == False:
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, 1)
            new_mandalorian.current_position = position.move_up()
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_down()) and world.is_wall(position.move_down()) == False:
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, 1)
            new_mandalorian.current_position = position.move_down()
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_left()) and world.is_wall(position.move_left()) == False:
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, 1)
            new_mandalorian.current_position = position.move_left()
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_right()) and world.is_wall(position.move_right()) == False:
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, 1)
            new_mandalorian.current_position = position.move_right()
            moves.append(new_mandalorian)

        return moves


    def board_ship(self):
        if self.world.get_tile(self.current_position) == 3:
            self.in_ship = True
            self.world.remove_ship()

    def is_in_ship(self):
        return self.current_position == self.world.ship_position

    def __eq__(self, other):
        if isinstance(other, Mandalorian):
            return self.current_position == other.current_position
        return False
    
    def __hash__(self):
        return hash(self.current_position)