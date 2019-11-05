from collections import namedtuple

Robot_Position = namedtuple('RPos', ['X', 'Y', 'Direction'])

lost_robot_positions = []


# Parametros de la clase:
# x_max, y_max, x_initital, y_initial, dir_initial, movements_list
# Metodos necesarios:
#   move()
class Robot(object):
    """Create nice little robots."""

    def __init__(self, x_max, y_max, x_initial, y_initial, dir_initial, movements_list):
        self.x_min = 0
        self.x_max = x_max
        self.y_min = 0
        self.y_max = y_max
        self.robot = Robot_Position(x_initial, y_initial, dir_initial)
        self.robot_last_position = Robot_Position(x_initial, y_initial, dir_initial)
        self.movements_list = movements_list
        self.robot_lost = False
        self.print_robot_status()
        print(" - Initial movements list: {}".format(self.movements_list))

    def move_left(self, rpos):
        print("   - Move left - Initial position.")
        self.print_robot_status()

        self.robot_last_position = Robot_Position(rpos.X, rpos.Y, rpos.Direction)

        if rpos.Direction == 'N':
            self.robot = Robot_Position(rpos.X, rpos.Y, 'W')
        elif rpos.Direction == 'W':
            self.robot = Robot_Position(rpos.X, rpos.Y, 'S')
        elif rpos.Direction == 'S':
            self.robot = Robot_Position(rpos.X, rpos.Y, 'E')
        else:
            # rpos.Direction == 'E'
            self.robot = Robot_Position(rpos.X, rpos.Y, 'N')

        print("   - Move left - Final robot position")
        self.print_robot_status()

    def move_right(self, rpos):
        print("   - Move right - Initial position")
        self.print_robot_status()

        self.robot_last_position = Robot_Position(rpos.X, rpos.Y, rpos.Direction)

        if rpos.Direction == 'N':
            self.robot = Robot_Position(rpos.X, rpos.Y, 'E')
        elif rpos.Direction == 'E':
            self.robot = Robot_Position(rpos.X, rpos.Y, 'S')
        elif rpos.Direction == 'S':
            self.robot = Robot_Position(rpos.X, rpos.Y, 'W')
        else:
            # rpos.Direction == 'W'
            self.robot = Robot_Position(rpos.X, rpos.Y, 'N')

        print("   - Move right - Final robot position")
        self.print_robot_status()

    def move_forward(self, rpos):
        print("   - Move forward - Initial position")
        self.print_robot_status()

        self.robot_last_position = Robot_Position(rpos.X, rpos.Y, rpos.Direction)

        if rpos.Direction == 'N':
            if not self.check_problematic_position(self.robot_last_position):
                if (rpos.Y + 1) > self.y_max:
                    self.set_robot_lost_coordinates()
                else:
                    self.robot = Robot_Position(rpos.X, rpos.Y + 1, 'N')
            else:
                print("Detected problematic position. Not moving.")
        elif rpos.Direction == 'E':
            if (rpos.X + 1) > self.x_max:
                self.set_robot_lost_coordinates()
            else:
                self.robot = Robot_Position(rpos.X + 1, rpos.Y, 'E')
        elif rpos.Direction == 'S':
            if (rpos.Y - 1) < self.y_min:
                self.set_robot_lost_coordinates()
            else:
                self.robot = Robot_Position(rpos.X, rpos.Y - 1, 'S')
        else:
            # rpos.Direction == 'W'
            if (rpos.X - 1) < self.x_min:
                self.set_robot_lost_coordinates()
            else:
                self.robot = Robot_Position(rpos.X - 1, rpos.Y, 'W')

        print("   - Move forward - Final robot position:")
        self.print_robot_status()

    def move_robot(self):
        for c in self.movements_list:
            if not self.robot_lost:
                print("Next movement: {}".format(c))
                if c == 'L':
                    self.move_left(self.robot)
                elif c == 'R':
                    self.move_right(self.robot)
                else:
                    self.move_forward(self.robot)
            else:
                print("Robot is LOST. Not moving anymore.")

        # print("Lost robots positions: {}".format(lost_robot_positions))

        if self.robot_lost:
            print("{} {} {} LOST".format(self.robot.X, self.robot.Y, self.robot.Direction))
        else:
            print("{} {} {}".format(self.robot.X, self.robot.Y, self.robot.Direction))

    def check_problematic_position(self, rpos):
        print("Checking position: {}".format(rpos))

        if lost_robot_positions:
            for pos in lost_robot_positions:
                print("   - Lost robot position: {}".format(pos))
                if (rpos.X == pos.X) and (rpos.Y == pos.Y) and (rpos.Direction == pos.Direction):
                    print("   - Position matched!")
                    return True
        else:
            print("   - No lost robot positions")
        return False

    def set_robot_lost_coordinates(self):
        lost_robot_positions.append(self.robot_last_position)
        self.robot_lost = True
        print("Robot Lost. Last known position: {}, {}, {} LOST".format(self.robot_last_position.X, 
                                                                        self.robot_last_position.Y,
                                                                        self.robot_last_position.Direction))

    def print_robot_status(self):
        print("   - Robot is at coordinates: [X:{}, Y:{}], Heading: {}".format(self.robot.X, self.robot.Y,
                                                                               self.robot.Direction))
