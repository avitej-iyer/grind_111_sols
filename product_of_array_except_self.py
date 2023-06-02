class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for this, we're basically using a double pass within one loop

        length = len(nums)
        sols = [1]*length
        pre = post = 1

        # for each element in nums, we can treat it as pre[x-1]*post[x+1]

        # in this vein, we do two passes calculating prefix and postfix
        # so for each element, they will multiply together
        for x in range(length):
            sols[x] *= pre
            pre *= nums[x]
            sols[length-1-x] *= post
            post *= nums[length-1-x]

        return sols    