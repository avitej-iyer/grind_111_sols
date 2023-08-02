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

###
# Below is the in-place backtracking solution I did for the 
# daily leetcode challenge
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         def backtrack(i, nums):
#             if i == len(nums):
#                 ret.append(nums[:])
#                 return
#             for j in range(i, len(nums)):
#                 nums[i], nums[j] = nums[j], nums[i]
#                 backtrack(i+1, nums)
#                 nums[j], nums[i] = nums[i], nums[j]

#         backtrack(0, nums)        

#         return ret    
  
