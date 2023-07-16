class Solution:

    # Alternatively you could just compare the length of the 
    # element and its set

    # return not len(nums) == len(set(nums))

    def containsDuplicate(self, nums: List[int]) -> bool:
        contain_set = set()

        for x in nums:
            if x in contain_set:
                return True
            else:
                contain_set.add(x)

        return False            