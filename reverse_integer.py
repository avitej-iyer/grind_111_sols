class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0].isnumeric():
            y = str(x)[::-1]
        else:
            y = "-"+str(x)[:0:-1]    
        if int(y) not in range(-2**31, 2**31-1):
            return 0
        return int(y)
