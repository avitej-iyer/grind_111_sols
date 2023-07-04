class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # this is a DP solution where we store the number of ways to reach the end from each cell
        # we start from the end and go backwards

        # base case: there is only one way to reach the end from the last row and last column (only one direction to go)
        # so we really only need to start iterating from the second last row and second last column

        # the number of paths from any cell to the end is the sum of the number of paths 
        # from the cell below it and the cell to the right of it
        
        dp = [[1 for x in range(n)] for y in range(m)]

        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                dp[row][col] = dp[row+1][col] + dp[row][col+1]

        return dp[0][0]   