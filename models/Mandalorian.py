class Mandalorian:
    def __init__(self, world, parent, operator, depth, cost, fuel):
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
        return self.parent
    
    def getOperator(self):
        return self.operator
    
    def is_in_ship(self):
        return self.in_ship
    
    def getDepth(self):
        return self.depth
    
    def getCost(self):
        return self.cost
    
    def getWorld(self):
        return self.state
    
    def move(self, new_position):
        if self.world.in_ship(new_position):
            self.board_ship()
        self.current_position = new_position

    def move_up(self):
        new_position = self.current_position.move_up()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)

    def move_down(self):
        new_position = self.current_position.move_down()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)

    def move_left(self):
        new_position = self.current_position.move_left()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)

    def move_right(self):
        new_position = self.current_position.move_right()
        if self.world.is_within_bounds(new_position):
            self.move(new_position)

    def possible_moves(self):
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
            
        up_cost = self.calculate_cost(position.move_up())
        down_cost = self.calculate_cost(position.move_down())
        left_cost = self.calculate_cost(position.move_left())
        right_cost = self.calculate_cost(position.move_right())
        
        if world.is_within_bounds(position.move_up()) and not world.is_wall(position.move_up()):
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, up_cost, new_fuel)
            new_mandalorian.current_position = position.move_up()
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_down()) and not world.is_wall(position.move_down()):
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, down_cost, new_fuel)
            new_mandalorian.current_position = position.move_down()
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_left()) and not world.is_wall(position.move_left()):
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, left_cost, new_fuel)
            new_mandalorian.current_position = position.move_left()
            moves.append(new_mandalorian)
        if world.is_within_bounds(position.move_right()) and not world.is_wall(position.move_right()):
            new_mandalorian = Mandalorian(world, self, 0, self.getDepth() + 1, right_cost, new_fuel)
            new_mandalorian.current_position = position.move_right()
            moves.append(new_mandalorian)
        return moves
    
    def calculate_cost(self, position):
        if self.in_ship and self.fuel > 0:
            return 0.5
        elif self.world.is_enemy(position):
            return 5
        return 1
               
    def leave_ship(self):
        self.in_ship = False
        self.fuel = 0

    def is_in_ship(self):
        return self.in_ship

    def __eq__(self, other):
        if isinstance(other, Mandalorian):
            return (self.current_position == other.current_position) and (self.in_ship == other.in_ship)
        return False
    
    def __hash__(self):
        return hash(self.current_position)