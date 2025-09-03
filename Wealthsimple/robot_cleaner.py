grid = [
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ".", ""],
    ["", "", ".", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", ".", "", "", ""],
    ["", "", "", "", ".", "", "", "", ""],
    ["", ".", ".", "", "", "", "", "", ""],
    ["", "", ".", "", "", "", "", ".", ""],
    ["", "", "", "", "", "", "", "", "."]
]

movements = {
    "up":   (-1, 0),    # Move up: increase y by 1
    "right": (0, 1), # Move right: increase x by 1
    "down": (1, 0), # Move down: decrease y by 1
    "left": (0, -1)  # Move left: decrease x by 1
}


def traverse(grid, x, y):
    n = len(grid) - 1
    m = len(grid[0]) - 1

    def move(x, y, dir):
        dx, dy = movements.get(dir)

        newX, newY = x + dx, y + dy

        if newX < 0 or newY < 0 or newX > n or newY > m or \
            grid[newX][newY] == "." or grid[newX][newY] == "-":

            return None, False

        grid[newX][newY] = "-"
        return (newX, newY), True
    
    lastValid = [(x, y)]
    grid[x][y] = "-"

    while lastValid:
        curr = lastValid.pop()
        for dir in movements:
            position, flag = move(curr[0], curr[1], dir)
            if flag:
                lastValid.append(position)
    
    return grid

print(traverse(grid, 0, 0))