class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start to beg -> contains 0
        # beg to mid -> contains 1
        # mid to end -> contains unknown elements
        # end to len(nums) -> contains 2

        beg = mid = 0
        end = len(nums)-1

        while mid <= end:
            if nums[mid] == 0:
                nums[beg], nums[mid] = nums[mid], nums[beg]
                beg += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1    