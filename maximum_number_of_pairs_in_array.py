from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = sum(cnt//2 for cnt in Counter(nums).values())
        return [pairs, len(nums) - pairs*2]