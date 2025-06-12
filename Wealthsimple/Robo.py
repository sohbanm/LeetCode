import random

class Robot:

    def __init__(self, row, col, room):
        self.row = row
        
        self.col = col
        self.room = room
        self.m = len(room)
        self.n = len(room[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.index = 0

    def move(self):
        new_row = self.row + self.directions[self.index][0]
        new_col = self.col + self.directions[self.index][0]

        if (
            0 <= new_col < self.n and
            0 <= new_row < self.row and 
            self.room[new_row][new_col] == 1
            ):
            self.row = new_row
            self.col = new_col
            return True
        return False

    def turnLeft(self):
        self.index = (self.index - 1) % 4

    def turnRight(self):
        self.index = (self.index + 1) % 4

    # def clean(self):
    #     self.room[self.row][self.col] = 2

    # def traverse(robot, grid): 
    #     seen = set()
    #     count = 0

    #     while True:
    #         if count >= sum(sum(grid, [])):
    #             return True

    #         if robot.move(grid):
    #             if (robot.row, robot.col) not in seen:
    #                 count += 1
    #             seen.add((robot.row, robot.col))

    #         choice = random.randint(0, 1) 

    #         if choice < 1:
    #             robot.turn_left()
    #         else:
    #             robot.turn_right()


    