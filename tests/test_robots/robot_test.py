from src.robots.robot import Robot, Robot_Position


def test_move_left_ValidPosition_ReturnsValidPosition():
    # Given
    test_robot = Robot(50, 50, 0, 0, 'N', 'RLF')
    new_robot_position = Robot_Position(0, 1, 'N')
    expected_robot_position = Robot_Position(0, 1, 'W')

    # When
    test_robot.move_left(new_robot_position)
    actual_robot_position = test_robot.robot

    # Then
    assert expected_robot_position == actual_robot_position


def test_move_right_ValidPosition_ReturnsValidPosition():
    # Given
    test_robot = Robot(50, 50, 0, 0, 'N', 'RLF')

    new_robot_position = Robot_Position(0, 1, 'N')
    expected_robot_position = Robot_Position(0, 1, 'E')

    # When
    test_robot.move_right(new_robot_position)
    actual_robot_position = test_robot.robot

    # Then
    assert expected_robot_position == actual_robot_position


def test_move_forward_ValidPosition_ReturnsValidPosition():
    # Given
    test_robot = Robot(50, 50, 0, 0, 'N', 'RLF')

    new_robot_position = Robot_Position(0, 1, 'N')
    expected_robot_position = Robot_Position(0, 2, 'N')

    # When
    test_robot.move_forward(new_robot_position)
    actual_robot_position = test_robot.robot

    # Then
    assert expected_robot_position == actual_robot_position
