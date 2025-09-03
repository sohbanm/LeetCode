import random

class Robot:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.direction = (0, 1)
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.direction_index = 0

    def move(self, grid):
        temp_row = self.row + self.direction[0]
        temp_col = self.col + self.direction[1]

        if (
            0 <= temp_row < len(grid)
            and 0 <= temp_col < len(grid[0])
            and grid[temp_row][temp_col] == 1
        ):
            self.row += self.direction[0]
            self.col += self.direction[1]
            return True
        else:
            return False

    def turn_left(self):
        self.direction_index = (self.direction_index - 1) % 4
        self.direction = self.directions[self.direction_index]

    def turn_right(self):
        self.direction_index = (self.direction_index + 1) % 4
        self.direction = self.directions[self.direction_index]


def traverse(robot, grid):
    seen = set()
    count = 0

    while True:
        if count >= sum(sum(grid, [])):
            return True

        if robot.move(grid):
            if (robot.row, robot.col) not in seen:
                count += 1
            seen.add((robot.row, robot.col))

        choice = random.randint(0, 1) 

        if choice < 1:
            robot.turn_left()
        else:
            robot.turn_right()


robot = Robot(1, 3)
grid = [
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

print(traverse(robot, grid))