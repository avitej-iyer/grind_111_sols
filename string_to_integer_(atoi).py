class Solution:
    def myAtoi(self, s: str) -> int:
        white_rem = s.lstrip()
        if not white_rem:
            return 0
        sign = -1 if white_rem[0] == "-" else +1

        white_rem = white_rem[1:] if (white_rem[0] =="+" or white_rem[0] =="-") else white_rem

        i, length, nums = 0, len(white_rem), ""

        while i < length and white_rem[i].isdigit():
            nums, i = nums+white_rem[i], i+1
        
        return max(-2**31, min(sign*int(nums or 0), 2**31 - 1))




        