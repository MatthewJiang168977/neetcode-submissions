class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c): 
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] != 1: 
                return 0 
            else:
                grid[r][c] = "#"
                return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
        max_area = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: 
                    max_area = max(max_area, dfs(r,c))
        return max_area 
            