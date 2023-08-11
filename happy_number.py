class Solution:
    def isHappy(self, n: int) -> bool:
        new_set = set()
        while n != 1:
            if n in new_set : return False
            new_set.add(n)
            n = sum([int(t) ** 2 for t in str(n)])
        else:
            return True