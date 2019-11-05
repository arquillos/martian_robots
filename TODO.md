# TODOs
  - Logging system
  - Input parameters using click framework
  - Document code
  - Create a new package with validations methods from "coding_challenge.py":
    - check_upper_right_coordinates
    - check_movement_list_values
    - check_movement_list_size
  - Add more unit checks:
    - class Robot
      1. init class check
      2. move_left from a N direction ends in an invalid position
      3. move_left from a S direction ends in an invalid position
      4. move_left from a E direction ends in an invalid position
      5. move_left from a W direction ends in an invalid position
      6. move_left with initial valid position ends in an invalid position
      7. move_left with initial invalid position ends in a valid position
      8. move_right from a N direction ends in an invalid position
      9. move_right from a S direction ends in an invalid position
      10. move_right from a E direction ends in an invalid position
      11. move_right from a W direction ends in an invalid position
      12. move_right with initial valid position ends in an invalid position
      13. move_right with initial invalid position ends in a valid position
      14. move_forward from a N direction ends in an invalid position
      15. move_forward from a S direction ends in an invalid position
      16. move_forward from a E direction ends in an invalid position
      17. move_forward from a W direction ends in an invalid position
      18. move_forward with initial valid position ends in an invalid position
      19. move_forward with initial invalid position ends in a valid position
      20. check_problematic_position
      21. set_robot_lost_coordinates
      22. print_robot_status
    - module coding_challenge
      1. check_upper_right_coordinates
      2. check_movement_list_values
      3. check_movement_list_size
  - Create integration checks (file I/O)
  - Add more E2E checks
    1. Dont move (empty movement lists)
    - Move 4 times left (ends in same position)
    - Move 4 times right (ends in same position)
    - Move left then right (ends in same position)
    - ...
    
 