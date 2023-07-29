class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        left_sum = 0
        right_sum = sum(nums)

        for ind, num in enumerate(nums):
            right_sum -= num
            nums[ind] = abs(left_sum-right_sum)
            left_sum += num

        return nums    