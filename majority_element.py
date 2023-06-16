class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1

        "[3,4,2,4,1,1,3,1,1,1,1]"

        for x in range(1, len(nums)):
            count += (1 if curr == nums[x] else -1)
            if count == 0:
                curr = nums[x+1] if x+1 < len(nums) else None
                count = 0

        return curr  