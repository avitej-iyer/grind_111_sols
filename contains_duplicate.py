class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contain_set = set()

        for x in nums:
            if x in contain_set:
                return True
            else:
                contain_set.add(x)

        return False            