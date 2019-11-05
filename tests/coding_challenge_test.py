from src.robots.robot import Robot, Robot_Position

X_MAX_POS = 5
Y_MAX_POS = 3


def test_E2E_From11E_WithRFRFRFRF_Returns11E():
    # Given
    test_robot = Robot(X_MAX_POS, Y_MAX_POS, 1, 1, 'E', 'RFRFRFRF')
    expected_robot = Robot_Position(1, 1, 'E')

    # When
    test_robot.move_robot()

    # Then
    assert test_robot.robot == expected_robot


def test_E2E_From32N_WithFRRFLLFFRRFLL_Returns33N():
    # Given
    test_robot = Robot(X_MAX_POS, Y_MAX_POS, 3, 2, 'N', 'FRRFLLFFRRFLL')
    expected_robot = Robot_Position(3, 3, 'N')

    # When
    test_robot.move_robot()

    # Then
    assert test_robot.robot == expected_robot


def test_E2E_From03W_WithLLFFFLFLFL_Returns23S():
    # Given
    test_robot = Robot(X_MAX_POS, Y_MAX_POS, 0, 3, 'W', 'LLFFFLFLFL')
    expected_robot = Robot_Position(2, 3, 'S')

    # When
    test_robot.move_robot()

    # Then
    assert test_robot.robot == expected_robot
