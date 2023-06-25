class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # since the two subsets need to have an equal sum (that is half
        # the sum of the list) we can add that as a condition
        if sum(nums)%2:
            return False

        target = sum(nums)//2
        dp = set()
        dp.add(0)

        for iter in range(len(nums) - 1, -1, -1):
            new_dp = dp.copy()
            for x in dp:
                if x + nums[iter] == target:
                    return True
                new_dp.add(x + nums[iter])
            dp = new_dp

        return True if target in dp else False    