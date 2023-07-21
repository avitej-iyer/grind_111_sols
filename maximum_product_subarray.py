class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # simple solution - since there's negative numbers as well
        # we should store the most negative nums as well
        # the smallest number can become the lasrgest if multiplied 
        # by a negative

        # this is also wy sliding window CANNOT be used here - 
        # a negative number further down (outside the window) can
        # lead to a max subarray

        cur_min = cur_max = 1

        # ret is already assigned the first element
        # because we're not multiplying to it anyways
        ret = nums[0]

        for num in nums:
            vals = [num, cur_min*num, cur_max*num]
            cur_min, cur_max = min(vals), max(vals)
            ret = max(ret, cur_max)
        
        return ret




            
