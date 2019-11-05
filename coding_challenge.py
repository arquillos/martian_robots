"""Main program for coding challenge."""
from sys import exit
from src.robots.robot import Robot

X_MIN_VALUE = 0
X_MAX_VALUE = 50
Y_MIN_VALUE = 0
Y_MAX_VALUE = 50
MAX_ALLOWED_MOVEMENTS = 100
ALLOWED_MOVEMENTS = ['L', 'R', 'F']
FILE_NAME = 'robot_positions.txt'


def check_upper_right_coordinates(x_max, y_max):
    if (x_max < X_MIN_VALUE) or (x_max > X_MAX_VALUE):
        print(" - ERROR - Check grid max x value. Valid values: [{}..{}]".format(X_MIN_VALUE, X_MAX_VALUE))
        exit()

    if (y_max < Y_MIN_VALUE) or (y_max > Y_MAX_VALUE):
        print(" - ERROR - Check grid max y value. Valid values: [{}..{}]".format(Y_MIN_VALUE, Y_MAX_VALUE))
        exit()


def check_movement_list_values(movement_list):
    for c in movement_list:
        if not any(c in movement for movement in ALLOWED_MOVEMENTS):
            print(" - ERROR - Movement: {} is not valid. Allowed movements: {}".format(c, ALLOWED_MOVEMENTS))
            exit()


def check_movement_list_size(movement_list):
    if len(movement_list) > MAX_ALLOWED_MOVEMENTS:
        print(" - ERROR - Movement list too long. Max number of movements: {}".format(MAX_ALLOWED_MOVEMENTS))
        exit()


def main():
    print('Martian Robots Coding Challenge.')

    with open(FILE_NAME) as f:
        print("- Getting upper-right coordinates")
        upper_right_coordinates = f.readline().strip().split()
        x_max = int(upper_right_coordinates[0])
        y_max = int(upper_right_coordinates[1])
        print("   - {}, {}".format(x_max, y_max))

        print("- Checking upper-right coordinates")
        check_upper_right_coordinates(x_max, y_max)

        while True:
            print("\n- Getting initial robot position")
            initial_position = f.readline().strip().split(' ')

            print("- Getting robot movements list")
            movement_list = f.readline().strip()
            check_movement_list_values(movement_list)
            check_movement_list_size(movement_list)

            if not movement_list:
                break  # EOF
            else:
                x_initial = int(initial_position[0])
                y_initial = int(initial_position[1])
                dir_initial = initial_position[2]
                print("   - Initial position: {}, {}, {}".format(x_initial, y_initial, dir_initial))
                print("   - Movements list: {}".format(movement_list))

                # Create Robot
                robot = Robot(x_max, y_max, x_initial, y_initial, dir_initial, movement_list)
                # Move Robot
                robot.move_robot()


if __name__ == '__main__':
    main()
