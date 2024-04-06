class Mandalorian:
    def __init__(self, world):
        self.world = world
        self.current_position = world.start_position
        self.in_ship = False
        self.fuel = 10

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
            self.move(new_position)
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

        if world.is_within_bounds(position.move_up()):
            moves.append(position.move_up())
        if world.is_within_bounds(position.move_down()):
            moves.append(position.move_down())
        if world.is_within_bounds(position.move_left()):
            moves.append(position.move_left())
        if world.is_within_bounds(position.move_right()):
            moves.append(position.move_right())

        return moves


    def board_ship(self):
        if self.world.get_tile(self.current_position) == 3:
            self.in_ship = True
            self.world.remove_ship()

    def is_in_ship(self):
        return self.current_position == self.world.ship_position