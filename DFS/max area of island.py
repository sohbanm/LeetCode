class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        high = 0
        
        def dfs(y, x):
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]) or grid[y][x] != 1 or (y, x) in visited:
                return 0

            visited.add((y, x))
            return dfs(y, x - 1) + dfs(y, x + 1) + dfs(y - 1, x) + dfs(y + 1, x) + 1
        
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if (y, x) not in visited:
                    if cell == 1:
                        high = max(high, dfs(y, x))

        return high