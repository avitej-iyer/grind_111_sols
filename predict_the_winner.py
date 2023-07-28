class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp_table = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if i == j:
                    dp_table[i][j] = nums[i]
                else:
                    dp_table[i][j] = max(nums[i] - dp_table[i+1][j], nums[j] - dp_table[i][j-1]) 
        return dp_table[0][n-1] >= 0