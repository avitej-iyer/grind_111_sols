# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# basically just binary search through
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        res = 1

        while start <= end:
            mid = (start+end)//2
            if not isBadVersion(mid):
                start = mid+1
            else:
                end = mid-1
                res = mid
        return res        