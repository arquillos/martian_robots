The program reads the input from a file called "robot_positions.txt"

Requirements:
 - python 3.5+
 - pytest 5.1.2+


Code Structure:

```
martian_robots
  ├── src
  │    ├── robots
  │    │     └── robot.py        
  │    └── coding_challenge.py
  └──  tests  
         ├── test_robots
         │     └── robot_test.py
         └── coding_challenge_test.py
```

 - robot.py - Robot class
 - coding_challenge.py - Main program and input validations
 - robot_test.py - Robot class automatic checks
 - coding_challenge_test.py - E2E tests
 
## Running the program
From main directory (martian_robots)

```
python coding_challenge.py
```

## Running Tests
From main directory (martian_robots)
```
python -m pytest tests
```