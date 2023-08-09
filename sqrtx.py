class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, 1000000
        mid = (left+right)//2
        while True:
            temp = mid
            if mid*mid > x:
                right = mid + 1
            else:
                left = mid
            mid = (left+right)//2
            if temp == mid:
                break
        return left
