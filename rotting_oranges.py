class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_list, rotten_list = set(), []

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh_list.add((x,y))
                elif grid[x][y] == 2:
                    rotten_list.append((x,y))

        time_taken = 0
        while fresh_list and rotten_list:
            new_rotten = []
            for x,y in rotten_list:
                for coord in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if coord in fresh_list:
                        fresh_list.remove(coord)
                        new_rotten.append(coord)
            rotten_list = new_rotten
            time_taken+=1
        return -1 if fresh_list else time_taken  