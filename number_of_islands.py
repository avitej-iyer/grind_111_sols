class Solution:

    # For this problem, the challenge is to make sure the "1"s aren't counted twice.
    # I.e every one that is connected needs to be counted as one island.

    # Below is a DFS approach - we start at a "1" and then check all the adjacent blocks, which then check their adjacent blocks, etc.
    # blocks and so on. 

    # The key is to make sure that we mark the blocks we've already visited as "0" so that we don't double count them.

    

    def dfs(self, grid, x,y):
            grid[x][y] = 0
            for up, side in (0,1),(0,-1),(1,0),(-1,0):
                x_coord = x + up
                y_coord = y + side
                if 0 <= x_coord < len(grid) and 0 <= y_coord < len(grid[0]) and grid[x_coord][y_coord] == '1':
                    self.dfs(grid, x_coord, y_coord)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    self.dfs(grid, x, y)
                    island_count+=1
        return island_count            
        

