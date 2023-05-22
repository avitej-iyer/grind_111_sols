class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        # iter through nums with lower limit
        max_sum = -999999
        for x in range(0, len(nums)):
            cur_sum += nums[x]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum   