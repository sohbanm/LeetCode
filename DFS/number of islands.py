class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count=0
        
        def dfs(y,x):
            if y<0 or y>=len(grid) or x<0 or x>=len(grid[0]) or (y,x) in visited:
                return
            if grid[y][x]=="1":
                visited.add((y,x))
                dfs(y+1,x)
                dfs(y-1,x)
                dfs(y,x+1)
                dfs(y,x-1)
        
        for y,row in enumerate(grid):
            for x,cell in enumerate(row):
                if (y,x) not in visited:
                    if cell=="1":
                        count+=1
                        dfs(y,x)

        return count