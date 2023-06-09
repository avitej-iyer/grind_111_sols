class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []
        def backtracking(curr):
            if len(curr) == len(nums):
                ret.append(curr[:])
                return

            for x in nums:
                if x not in curr:
                    curr.append(x)
                    backtracking(curr)
                    curr.pop()
                    

        backtracking([])
        return ret    
